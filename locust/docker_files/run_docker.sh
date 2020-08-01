#!/usr/bin/env bash
# Build image
/usr/local/bin/docker_files build --tag=locust .

# List docker_files images
/usr/local/bin/docker_files image ls

# Run locust app
/usr/local/bin/docker_files run -p 8080:8080 locust