set shell := ["bash", "-eEuo", "pipefail", "-c"]

uvx := require("uvx")

fmt: prettier ruff

[group("fmt")]
prettier:
    npx prettier . --write

[group("fmt")]
ruff:
    ruff format .claude/*/*.py

[group("test")]
test:
    uv run --frozen pytest
