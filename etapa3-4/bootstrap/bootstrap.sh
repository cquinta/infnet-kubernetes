#!/bin/bash
apt-get update -y 
apt-get install -y curl wget
curl -fsSL https://get.docker.com | bash

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64