# pyjamas2019-django

Live para o Pyjamas 2019 - Introdução a Arquitetura do Django

https://pyjamas.live

## Video

[link do video no YouTube]()

## Tutorial

[tutorial aqui](tutorial.md)

## Como roda o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/pyjamas2019-django.git
cd pyjamas2019-django
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```