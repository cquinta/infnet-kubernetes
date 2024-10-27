# Testando liveness Probes

## Iniciando o minikube com 3 nós e containerd e cilium

```bash
minikube start --nodes 3 --cni calico --container-runtime=containerd 
```

Iniciar a probe readiness

