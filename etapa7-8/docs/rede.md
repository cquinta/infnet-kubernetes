# Colocando um aplicação de 2 camadas para funcionar

## Camanda de frontend

### Deploy da aplicação

Manifesto de deploy da aplicação

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
  labels:
    app: simpleapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: simpleapp 
  template:
    metadata:
      labels:
        app: simpleapp
    spec:
      containers:
      - name: simpleapp-container
        image: carlosquintanilha/simpleapp:redis
        ports:
        - containerPort: 8000
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 2
          successThreshold: 1
          failureThreshold: 3

```
Criar o arquivo .yaml e colocar a aplicação para rodar através do ```kubectl apply -f <path-do-manifesto> ```


### Expondo a camada web

Criar um serviço do tipo nodeport através do manifesto: 

```bash
apiVersion: v1
kind: Service
metadata:
  name: app
spec:
  selector:
    app: simpleapp
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  type: NodePort
```

Criar um arquivo yaml com o manifesto e colocar para rodar através do comando ```kubectl apply -f <path-do-arquivo>```

Verificar a disponibilidade do serviço através do comando ```kubectl get svc``` a resposta deve ser parecida com 

```bash

 kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
app          NodePort    10.98.242.254   <none>        8000:31771/TCP   92s
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          4m13s
```

Caso se esteja utilizando um cluster minikube é preciso rodar o comando ```minikube service app --url``` para receber a url exposta para fora do cluster. 
Caso esteja rodando um cluster normal a url será o IP de um dos nós e a porta exposta, que no caso do exemplo acima seria 31771.

## Camada de Cache
### Deploy do Redis
Criar um manifesto do redis conforme abaixo: 

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  labels:
    app: redis
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis
        ports:
        - containerPort: 6379
```

Criar o arquivo yaml e fazer o deploy através do comando ```kubectl apply -f <path-do-manifesto>```

### Expondo o Redis para o cluster

Criar o serviço redis conforme abaixo: 

```bash
apiVersion: v1
kind: Service
metadata:
  name: redis
spec:
  selector:
    app: redis
  ports:
    - protocol: TCP
      port: 6379
      targetPort: 6379

```
Caso esteja utilizando um cluster kubernetes gerado através do minikube é preciso utilizar o ```minikube tunnel" e usar o comando ```curl --resolve "simpleapp.example:80:$( minikube ip )" -i http://simpleapp.example ``` para o acesso ao ingress.

Caso esteja utilizando o minikube no wsl com o docker desktop substitua o "minikube ip" por 127.0.0.1 da seguinte maneira: 
```curl --resolve "simpleapp.example:80:127.0.0.1" -i http://simpleapp.example```

Comandos para debug

```bash
kubectl get endpoints

kubectl get pods --selector=app=simpleapp
