# Testando liveness Probes

## Iniciando o minikube com 3 nós e containerd e cilium

```bash
minikube start --nodes 3 --cni calico --container-runtime=containerd 
```

Clonando o repositorio

```bash
git clone 

https://github.com/cquinta/infnet-kubernetes.git

```

Iniciando as duas livenessprobes 

* pod-simpleapp-liveness.yaml
* pod-simpleapp-liveness_v1.yaml

```bash
kubectl apply -f manifestos/pod-simpleapp-liveness.yaml

kubectl apply -f manifestos/pod-simpleapp-liveness_v1.yaml

```

