FROM python:3.6-alpine
MAINTAINER Mikalai Charopkin (ncherepkin@live.com)

ADD . /opt/app/

WORKDIR /opt/app/

RUN pip install -r requirements.txt \
&& apk add --no-cache curl

EXPOSE 5000

ENV FLASK_APP=/opt/app/main.py

ENTRYPOINT ["flask", "run"]
CMD ["--host=0.0.0.0"]

HEALTHCHECK --interval=5s --timeout=1s --start-period=60s --retries=1\
  CMD curl -s -f localhost:5000 || exit 1
