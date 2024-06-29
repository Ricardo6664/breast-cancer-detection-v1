FROM python:3.8

RUN python -m pip install --upgrade pip && \
    pip install Django

RUN mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh

ARG SSH_PRIVATE_KEY
ARG SSH_PUBLIC_KEY

RUN echo "$SSH_PRIVATE_KEY" > /root/.ssh/id_ed25519 && \
    echo "$SSH_PUBLIC_KEY" > /root/.ssh/id_ed25519.pub && \
    chmod 600 /root/.ssh/id_ed25519 && \
    touch /root/.ssh/known_hosts && \
    ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /cancer_detection/breast_cancer_detection_system
# 0.0.0.0:8000
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

