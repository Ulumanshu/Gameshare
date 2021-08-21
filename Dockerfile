# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN chown -R root:root /code/
RUN chmod 755  /code/entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
RUN pwd | cat
# run entrypoint.sh
ENTRYPOINT ["sh", "/code/entrypoint.sh"]