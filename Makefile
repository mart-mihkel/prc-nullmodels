.PHONY: setup
setup:
	@uv sync

.PHONY: format
format: setup
	@uv run ruff format

.PHONY: lint
lint: setup
	@uv run ruff check

.PHONY: marimo
marimo: setup
	@uv run marimo edit
