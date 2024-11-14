# Labels

```bash
kubectl get pods --show-labels
kubectl label pods shell-pod "canary=true"
kubectl get pods -L canary
kubectl label pods shell-pod "canary-"
kubectl get pods --selector="ver=2"
kubectl get pods --selector="app in (alpaca,bandicoot)
kubectl get deployments --selector="canary"
```
