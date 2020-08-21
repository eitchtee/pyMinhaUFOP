<div align="center">
	<a href="https://pypi.org/project/pyminhaufop/" target="_blank">
    	<img alt="Exemplo pyminhaufop" title="pyminhaufop" src="./.github/images/header.png" />
    </a>
    </div>

<h3 align="center">pyMinhaUFOP</h3>
<p align="center">Wrapper não-oficial para a API mobile da MinhaUFOP</p>

<div align="center">
  <img alt="PyPI - License" src="https://img.shields.io/pypi/l/pyminhaufop?label=LICEN%C3%87A&style=for-the-badge">
  <a href="https://pypi.org/project/pyminhaufop/" target="_blank"><img alt="PyPI" src="https://img.shields.io/pypi/v/pyminhaufop?style=for-the-badge"></a>
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pyminhaufop?style=for-the-badge">
  <img alt="PyPI - Downloads" src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=303f9f&maxAge=86400&label=downloads&query=$.total_downloads&url=https://api.pepy.tech/api/projects/pyminhaufop">
</div>

<br/>

<h5 align="center"> 
🚧 Em desenvolvimento 🚧
</h5>

---

<p align="center">
    <a href="#o-que-é">❓ O que é?</a> •
    <a href="#instalação">💻 Instalação</a> • 
    <a href="#uso-e-exemplos">✍️ Uso e Exemplos</a> •
    <a href="#roadmap">🗺️ Roadmap</a>
</p>

## O que é?
Este wrapper expõe a API Mobile do Aplicativo [Minha UFOP](https://play.google.com/store/apps/details?id=br.ufop.app).

## Instalação


#### Automático (recomendado)

```
$ pip install pyminhaufop --upgrade
```

#### Manual

1. Clone este repositório
2. ```$ python setup.py install```

<br/>

> Lembre-se de manter a biblioteca sempre atuaizada.

## Uso e Exemplos

### Documentação
Você pode acessar a documentação adicional por meio do parâmetro ``__doc__``.

```python
>> from pyminhaufop import MinhaUFOP
>> print(MinhaUFOP.cardapio_do_ru.__doc__)
```

### Login e Inicialização
#### Simples
```python
from pyminhaufop import MinhaUFOP

# inicializa a classe
api = MinhaUFOP()

# Logue e gere o token
api.login('123.456.789-10', 'sua_senha')

# acesse as funções da API
saldo = api.saldo_do_ru()
print(saldo['saldo'])
```

#### Com senha hasheada
```python
from pyminhaufop import MinhaUFOP

# inicializa a classe
api = MinhaUFOP()

# Logue usando uma senha hasheada em MD5
api.login('123.456.789-10', 'sua_senha_em_MD5', encode=False)

# acesse as funções da API
saldo = api.saldo_do_ru()
print(saldo['saldo'])
```

#### Utilizando conta com mais de um perfil
```python
# Você pode passar os dados de forma direta
# identificacao = matrícula com pontos
# perfil = 
#        - "G" - Alunos de Graduação
api.login('123.456.789-10', 'sua_senha', identificacao="20.1.0000", perfil="G")
```

<p align="center">ou</p>

Indique o index do perfil. O mais recente é o index 0.
```python
api.login('123.456.789-10', 'sua_senha', perfil_num=0)
```

### RU
#### Saldo
```python
saldo = api.saldo_do_ru()
```

#### Cardápio
Acessar cardápio da semana
```python
cardapio = api.cardapio_do_ru()
```
<p align="center">ou</p>

Acessar cardápio de um dia específico na semana
````python
cardapio = api.cardapio_do_ru(dia_da_semana=0) # 0 (segunda) a 4 (sexta)
````

#### Extrato
```python

extrato = api.extrato_ru(inicio='2020-01-01', fim='2020-08-01')

print(extrato)
```

### Salvar foto de um CPF
```python
# Retorna a foto em bytes
foto = api.foto('123.456.789-10')

# Salvar a foto em um arquivo .png
with open('ex.png', 'wb') as file:
    file.write(foto)
```

### Atestado de Matrícula
```python
print(api.atestado())
```

### Boleto

#### Listagem

```python
print(api.listar_boletos())
```

#### Gerar
````python
from pyminhaufop import MinhaUFOP
from pyminhaufop.exceptions import MinhaUFOPHTTPError

api = MinhaUFOP()

a = api.login("123.456.789-10", "hunter2")

try:
    api.gerar_boleto(valor=12.0, matricula="20.1.1234", perfil="G")
except MinhaUFOPHTTPError as err:
    if err.status_code == 500:
        print("Já existe um boleto com pagamento pendente.")
````

## Roadmap

### Funções nativas

- [x] Login `v0.0.1`
- [x] Consulta de Saldo do RU `v0.0.1`
- [x] Consulta de foto pelo CPF `v0.0.2`
- [x] Consulta ao Cardápio do RU `v0.1.0`
- [ ] Boletos
    - [x] Emissão `v.0.3.0`
    - [ ] Download
    - [x] Listagem `v.0.3.0`
- [x] Consulta ao Atestado de Matrícula `v0.2.0`
- [x] Consulta ao Extrato do RU `v0.2.0`