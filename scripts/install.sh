#!/bin/bash

# Start Minikube
minikube start

# Apply Redis Deployment
kubectl apply -f ../k8s/redis-deployment.yaml

# Apply Flask Deployment
kubectl apply -f ../k8s/flask-deployment.yaml
