dockerpath="haoqiu/facerecognition4gcp"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag face_recognition4gcp $dockerpath

# Push Image
docker image push $dockerpath