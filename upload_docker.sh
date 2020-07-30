dockerpath="tim2000/facerecognition4gpu"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag facerecognition4gpu $dockerpath

# Push Image
docker image push $dockerpath