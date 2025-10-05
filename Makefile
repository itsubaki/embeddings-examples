SHELL := /bin/bash

install:
	pip install torch transformers
	pip install yasem fugashi unidic_lite

activate:
	source .venv/bin/activate

venv:
	python3 -m venv .venv

splade:
	python3 splade.py
