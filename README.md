# FastAPI URL Shortener

[![Python checks](https://img.shields.io/github/actions/workflow/status/UstinovichYaroslav/fastapi-url-shortener/python-checks.yaml?branch=main&style=for-the-badge&logo=githubactions&logoColor=white&label=Python%20checks)](https://github.com/UstinovichYaroslav/fastapi-url-shortener/actions/workflows/python-checks.yaml)
![Python 3.13](https://img.shields.io/badge/python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Code style: Black](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://black.readthedocs.io/en/stable/)
[![Linted with Ruff](https://img.shields.io/badge/linted%20with-ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![Checked with mypy](https://img.shields.io/badge/type%20checked-mypy-2A6DB2?style=for-the-badge&logo=python&logoColor=white)](https://mypy.readthedocs.io/en/stable/)
[![Managed with uv](https://img.shields.io/badge/managed%20with-uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white)](https://docs.astral.sh/uv/)

## Develop

### Setup

Right click `url-shortener` -> Mark Directory as -> Sources Root

### Configure pre-commit

Install pre-commit hook:

```shell
pre-commit install
```

### Install

Install packages:

```shell
uv install
```

### Run

Go to workdir:

```shell
cd url-shortener
```

Run dev server:

```shell
fastapi dev
```

## Snippets

```shell
python -c 'import secrets;print(secrets.token_urlsafe(16))'
```
