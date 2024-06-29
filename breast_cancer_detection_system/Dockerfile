FROM python:3.11-alpine3.18

LABEL maintainer="ricardosantos130100@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /breast_cancer_detection_system
COPY ./scripts /scripts

RUN apk update && \
    apk add --no-cache openssh-client && \
    python -m pip install --upgrade pip && \
    pip install virtualenv && \
    pip install django

WORKDIR /breast_cancer_detection_system

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

RUN addgroup -S dgroup && \
    adduser -S -G dgroup duser && \
    mkdir -p /data/web/static /data/web/media /breast_cancer_detection_system/users /data/web/static/admin && \
    chown -R duser:dgroup /venv /data/web /breast_cancer_detection_system && \
    chmod -R 755 /data/web /breast_cancer_detection_system && \
    chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]
