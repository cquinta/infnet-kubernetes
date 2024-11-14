# Aprovisionamento dinâmico no Kubernetes

Criação da Storage Class com o Minikube

```bash
minikube addons enable storage-provisioner-rancher
```

Criação da PVC

```bash
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 64Mi
```