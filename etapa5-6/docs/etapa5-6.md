# Limitando Recursos e Usando Probes


## Iniciando o minikube com 3 nós e containerd e cilium

```bash
minikube start --nodes 3 --cni calico --container-runtime=containerd
minikube addons enable metrics-server 
```

Clonando o repositorio

```bash
git clone https://github.com/cquinta/infnet-kubernetes.git

```

## Testando o limite de cpus

Criando o namespace
```bash
kubectl create namespace cpu-example
```

Rodando o pod 

```bash
kubectl apply -f manifesto/pod-cpu-example.yaml

watch kubectl top pods -n cpu-example
```

Agora rode o deployment

```bash
kubectl apply -f manifesto/deployment-cpu.yaml
```

Agora modifique os limites e requests para testar o comportamento. 
Tente com um request maior que a quantidade de cpus do host para ver o que ocorre. 



Iniciando as duas livenessprobes 

* pod-simpleapp-liveness.yaml
* pod-simpleapp-liveness_v1.yaml

```bash
kubectl apply -f manifestos/pod-simpleapp-liveness.yaml

kubectl apply -f manifestos/pod-simpleapp-liveness_v1.yaml

kubectl logs -f pod/simpleapp-liveness-pod 
kubectl logs -f pod/simpleapp-liveness-v1-pod 

```



