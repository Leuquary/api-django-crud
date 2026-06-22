# API Django

API em Python com o objetivo de buscar, cadastrar, alterar e excluir usuários. Este programa realiza operações CRUD simples, ele pode ser executado em um container docker, e implantado em um cluster local minikube.

## Tecnologias utilizadas

- Python 3
- Django 6
- DB SQLite 
- Docker
- Minikube
- WSL2 (Ubuntu 26.04)

## Funcionalidades

- Cadastrar usuários
- Buscar usuário
- Alterar cadastro
- Excluir usuário

## Pré-requisitos

Antes de iniciar, certifique-se de possuir as seguintes dependências:

- Recurso WSL2 ativado
- Distribuição Linux Ubuntu 26.04 (de preferência)
- Banco de dados SQLite 
- Python 3 
- django 6.0.6
- djangorestframework 3.17.1
- django-cors-headers 4.9.0

## Instalação

### 1. Ative o recurso WSL2 no Windows

### 2. Inicie sua distribuição Linux

### 3. Instale o Python3 pelo terminal do WSL

- sudo apt update
- sudo apt install python3

### 4. Instale o docker e suas dependências

sudo apt install -y certificates curl gnupg lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \ 
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo usermod -aG docker $USER

newgrp docker

sudo systemctl enable docker

sudo systemctl start docker

### 5. Instale o minikube e suas dependências 

curl -LO https://googleapis.com
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64

curl -LO "https://k8s.io(curl -L -s https://k8s.io)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
rm kubectl

### 6. Selecione um diretório e clone o repositório

git clone 

### 7. Crie um ambiente virtual venv

python3 -m venv .venv
source .venv/bin/activate

### 8. Instale as dependências do projeto

pip install -r requirements.txt

### 9. Inicie o cluster do minikube

minikube start

### 10. Crie o deployment no cluster

kubectl apply -f ./k8s/deployment.yaml
(certifique-se de estar na pasta raiz do projeto)

### 11. Crie o service no cluster

kubectl apply -f ./k8s/deployment.yaml
(certifique-se de estar na pasta raiz do projeto)

### 12. Disponibilize o serviço

minikube service django-service

