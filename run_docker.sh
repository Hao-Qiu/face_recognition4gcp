# Build image
docker build --tag=facerecognition4gpu .

# List docker images
docker image ls

# Run flask app
docker run -p 8080:8080 facerecognition4gpu