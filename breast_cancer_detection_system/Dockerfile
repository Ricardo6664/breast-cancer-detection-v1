FROM python:3.11-alpine3.18

LABEL maintainer="ricardosantos130100@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /breast_cancer_detection_system
COPY ./scripts /scripts

RUN apk update && \
    apk add --no-cache openssh-client && \
    python -m pip install --upgrade pip && \
    pip install virtualenv

WORKDIR /breast_cancer_detection_system

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

RUN addgroup -S dgroup && \
    adduser -S -G dgroup duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:dgroup /venv /data/web/static /data/web/media && \
    chmod -R 755 /data/web/static /data/web/media && \
    chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]
