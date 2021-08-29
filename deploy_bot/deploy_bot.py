# -*- coding: utf-8 -*-

import json
import os

import flask
from gevent.pywsgi import WSGIServer
from hmac import HMAC, compare_digest
from hashlib import sha1

jsonify = flask.jsonify

app = flask.Flask(__name__)
app.debug = True
ROOT = str(app.root_path)


def verify_github_signature(req):
    received_sign = req.headers.get('X-Hub-Signature').split('sha1=')[-1].strip()
    server_github_key = ''
    with open(ROOT + '/' + "github_webhook_key.json") as f:
        file = json.load(f)
        server_github_key = file.get("github_webhook_secret")

    expected_sign = HMAC(key=server_github_key, msg=req.data, digestmod=sha1).hexdigest()

    return compare_digest(received_sign, expected_sign)


@app.route("/", methods=["POST"])
def deploy_app():
    script_path = ROOT + '/../' + 'deploy.sh'
    if verify_github_signature(flask.request):
        try:
            os.system(script_path)

        except Exception as err:
            return jsonify(
                success=False,
                error='%s' % str(err),
            )

        return jsonify(
            success=True,
            error=False,
        )

    else:
        return jsonify(
            success=False,
            error='Webhook signature is wrong',
        )


server = WSGIServer(("", 5000), app)
server.serve_forever()
