# Instalação de um cluster com kubeadm

## Container runtime

Habilitar o ipv4 forward: 

```bash
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system

# Verifying
sysctl net.ipv4.ip_forward

```

Instalar o containerd: 

```bash
wget https://github.com/containerd/containerd/releases/download/v1.7.23/containerd-1.7.23-linux-amd64.tar.gz

sudo tar Cxzvf /usr/local containerd-1.7.23-linux-amd64.tar.gz

wget https://raw.githubusercontent.com/containerd/containerd/main/containerd.service

sudo mkdir -p /usr/local/lib/systemd/system/

sudo cp containerd.service /usr/local/lib/systemd/system/containerd.service

sudo systemctl daemon-reload
sudo systemctl enable --now containerd

wget https://github.com/opencontainers/runc/releases/download/v1.1.15/runc.amd64

sudo install -m 755 runc.amd64 /usr/local/sbin/runc

wget https://github.com/containernetworking/plugins/releases/download/v1.6.0/cni-plugins-linux-amd64-v1.6.0.tgz

sudo mkdir -p /opt/cni/bin

sudo tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-<x>.tgz

sudo mkdir -p /etc/containerd

sudo containerd config default > /etc/containerd/config.toml

# Setar no config.toml 
# [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
#    SystemdCgroup = true

# reiniciar 
sudo systemctl restart containerd

```

## Instalar o kubectl 

[Instalação do kubectl](https://kubernetes.io/docs/tasks/tools/)

## Instalar o kubeadm
```bash
sudo apt-get update

sudo apt-get install -y apt-transport-https ca-certificates curl gpg

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm 
sudo apt-mark hold kubelet kubeadm 
sudo systemctl enable --now kubelet

```

## Criando o cluster

```bash
kubeadm init --apiserver-advertise-address <ip>
```
Guardar o comando de join

## Adicionando nós

Realizar todas as configurações acima exceto a criação do cluster e rodar o comando de join. 



## Instalação do CNI

### Instalação do client cillium

```bash
CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/main/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}

```

### Instalação do cilium

Com o kubectl configurado rodar 

```bash
cilium install --version 1.16.3
```


