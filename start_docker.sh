sudo docker build -t env_django \
    --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/id_ed25519)" \
    --build-arg SSH_PUBLIC_KEY="$(cat ~/.ssh/id_ed25519.pub)" .


sudo docker run -it -p 8000:8000 --mount type=bind,source="$(pwd)/Website_for_Breast_Cancer_Detection",target=/cancer_detection/ env_django
