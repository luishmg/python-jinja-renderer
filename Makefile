.PHONY: install test

default: lint test

install:
	pipenv install --dev --skip-lock

lint:
	flake8 ./pyrender

test:
	PYTHONPATH=. pytest --verbose --color=yes -s
