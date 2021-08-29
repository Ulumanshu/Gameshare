# -*- coding: utf-8 -*-

import json
import os

import flask
from gevent.pywsgi import WSGIServer

jsonify = flask.jsonify

app = flask.Flask(__name__)
app.debug = True
ROOT = str(app.root_path)


@app.route("/", methods=["POST"])
def deploy_app():
    script_path = ROOT + '/../' + 'deploy.sh'
    server_github_key = ''
    with open(ROOT + '/' + "github_webhook_key.json") as f:
        file = json.load(f)
        server_github_key = file.get("github_webhook_secret")

    data = flask.request.get_json()
    secret_key = data.get('secret_key', '') or ''

    if secret_key == server_github_key:
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
            error='Webhook key %s is wrong' % secret_key,
        )


server = WSGIServer(("", 5000), app)
server.serve_forever()
