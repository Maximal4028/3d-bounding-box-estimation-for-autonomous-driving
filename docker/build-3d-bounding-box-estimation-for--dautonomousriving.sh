#!/bin/bash

docker build . \
    -f docker/Dockerfile.3d-bounding-box-estimation-for-autonomous-driving \
    -t deep3dbox:latest \
