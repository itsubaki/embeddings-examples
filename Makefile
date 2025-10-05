SHELL := /bin/bash

install:
	pip install torch transformers yasem fugashi unidic_lite

activate:
	source .venv/bin/activate

venv:
	python3 -m venv .venv

hello:
	python3 hello.py
