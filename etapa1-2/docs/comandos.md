# Comandos realizados na etapa 1

## Kubectl 

Verificando a configuração

```bash
kubectl config view
```
Criando o primeiro POD

```bash
kubectl run nginx --restart Never --image nginx
```
Verificando os PODs
```bash
kubectl get pods
```
Verificando os nós
```bash
kubectl get nodes
```

## Minikube

```bash
minikube start --nodes 3
minikube addons enable metrics-server
```