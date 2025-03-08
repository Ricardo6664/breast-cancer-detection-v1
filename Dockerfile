FROM python:3.11-alpine3.17

LABEL maintainer="ricardosantos130100@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./breast_cancer_detection_system /breast_cancer_detection_system
COPY ./scripts /scripts

WORKDIR /breast_cancer_detection_system

EXPOSE 8000

RUN apk update && apk add --no-cache python3 py3-virtualenv

RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /breast_cancer_detection_system/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]
