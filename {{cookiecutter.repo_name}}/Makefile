code-lint:
	poetry run isort */*.py */*/*.py tests/*.py
	poetry run black */*.py */*/*.py tests/*.py
	poetry run flake8 */*.py */*/*.py tests/*.py

install:
	poetry install

run-test:
	poetry run pytest tests/

requirements-file:
	poetry export -f requirements.txt --without-hashes > requirements.txt

