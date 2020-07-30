#!/usr/bin/env bash
# Build image
/usr/local/bin/docker build --tag=face_recognition4gcp .

# List docker images
/usr/local/bin/docker image ls

# Run flask app
/usr/local/bin/docker run -p 8080:8080 face_whirecognition4gcp