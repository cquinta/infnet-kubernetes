# Criando o Primeiro POD

## Rodando Pods

Para criar um pod são necessários 2 parâmetros
* Nome: 
* Imagem:

```bash
kubectl run simpleapp-pod --image carlosquintanilha/simpleapp:v0.1

```
Verificando os pods: 
```bash
kubectl get pods
kubectl get pods -o wide

```

Criando o pod com sintaxe declarativa

Criar o arquivo simpleapp-pod.yaml
```bash

apiVersion: v1
kind: Pod
metadata:
  name: simplaapp-pod
spec:
  containers:
    - name: simpleapp-container
      image: carlosquintanilha/simpleapp:v0.1

```
Criar o pod através do arquivo

```bash
kubectl apply -f simpleapp-pod.yaml
```

Obtendo informações sobre o pod

```bash
kubectl describe pod simpleapp-pod

kubectl get pod <pod-name> -o yaml
kubectl get pod <pod-name> -o json

```

Acessando o pod

Por enquanto vamos utilizar o port-forward para fazer este acesso
```bash

kubectl port-forward pod/simpleapp-pod 8000:8000
```
