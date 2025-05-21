PYTHON=python
PIP=pip

install:
$(PIP) install -r requirements-dev.txt

lint:
ruff src tests

type:
pyright

test:
pytest -q

lock:
pip-compile requirements.in
pip-compile requirements-dev.in
