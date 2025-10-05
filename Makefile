SHELL := /bin/bash

install:
	pip install torch transformers yasem

activate:
	source .venv/bin/activate

venv:
	python3 -m venv .venv
