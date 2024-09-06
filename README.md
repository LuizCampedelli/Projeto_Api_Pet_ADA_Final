# Projeto Api Pet ADA

## Sumario

### Este projeto é uma aplicação em Python 3.11, com a função de treinar o desenvolvimento de uma pipeline para o deploy de quaisquer mudanças realizadas na branch "main", com um gatilho para atualizar uma instancia EC2 na nuvem AWS.

## Resultado final

![ec2_app_1](docs/assets/Pet_info_index.png)

![ec2_app_2](docs/assets/Pet_info_results.png)

## App rodando na AWS

![ec2_app_3](docs/assets/pet_gif.gif)

## App rodando na CLI

### Caso queira, atraves de uma conexão SSH ou do Cloud Connect, em /home/ec2-user/app, rode o comando:

```bash
python3 pet_info.py
```
### Resultado

![ec2_app_4](docs/assets/ec2_cli.png)

## Arquitetura da implantação

![ec2_app_5](docs/assets/arquitetura.svg)

## Funcionalidades do app

- Adicionar novos pets com nome, raça, idade, peso e informação sobre vacinação.
- Visualizar a informação do pets cadastrado.

## Tecnologias utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.
- **Flask**: Framework web utilizado para criar a aplicação.
- **Gunicorn**: Servidor HTTP WSGI para servir a aplicação.
- **AWS**: Nuvem utilizada para hospedar a aplicação.
- **Github Actions**: Ferramenta utilizada para criar a pipeline de deploy.

## Como utilizar

### Pré-requisitos

- Python 3.11
- Pip
- Virtualenv

### Instalação

1. Clone o repositório

```bash
git clone git@github.com:LuizCampedelli/Projeto_Api_Pet_ADA_Final.git
```

2. Crie um ambiente virtual

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```


3. Instale as dependências

```bash
pip install -r requirements.txt
```


4. Execute a aplicação no CLI

```bash
python3 pet_info.py
```


5. Acesse a aplicação no navegador

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```


6. Acesse a aplicação no navegador

```bash
http://localhost:5000
```

## Como implantar na AWS usando Github Actions

1. Crie uma conta na AWS e configure o acesso programático.
2. Crie uma EC2, com chave de SSH, baixe a chave para um local seguro.
3. Crie um Security Group para a EC2, com as portas 22 e 5000 abertas.
4. Adicione os segredos em varias e segredos do actions na aba Settings do repositório, com as seguintes chaves:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
  - AWS_REGION
  - EC2_IP
  - EC2_PRIVATE_KEY

5. Faça um push na branch "main" e veja a pipeline de deploy ser executada.

## Observações

- Caso queira fazer modificações sem dar gatilho no deploy, faça commits assim:

  ```bash
  git commit -m 'feat/nome_da_feature [skip actions]'
  ```

  ### São suportados para dar skip actions os seguintes tipos no commit:

  - [skip ci]
  - [ci skip]
  - [no ci]
  - [skip actions]
  - [actions skip]

  ### Exemplo de commit com skip actions:

  ```bash
  git commit -m "Update docs [skip ci]"
  git commit -m "Fix typo [ci skip]"
  git commit -m "Minor change [no ci]"
  git commit -m "Change config [skip actions]"
  git commit -m "Update dependencies [actions skip]"
  ```

### Boas práticas

- Caso não queira enviar os arquivos de README e docs para o deploy, adicone no seu deploy:

```bash
  on:
    push:
      branches:
        - main
      paths-ignore:
        - 'docs/**'
        - 'README.md'
```

## Licença

Este projeto está sob a licença do MIT. Consulte a [LICENSE](LICENSE) para obter mais informações.


## Como contribuir

1. Siga as diretivas do [CONTRIBUTING.md](docs/CONTRIBUTING.md)

## Autores

- [Luiz Campedelli](https://github.com/LuizCampedelli)

---
