#!/bin/bash

#Update and install curl and wget
apt-get update -y 
apt-get install -y curl wget

#Install Docker
curl -fsSL https://get.docker.com | bash

#Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

#Install minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64