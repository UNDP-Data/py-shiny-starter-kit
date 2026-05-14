install:
	pip install --upgrade pip && pip install ".[dev]"
lint:
	pylint src
format:
	isort . --profile black --multi-line 3 && black --target-version py313 .
test:
	pytest tests --headed --browser webkit
run:
	shiny run -r app.py