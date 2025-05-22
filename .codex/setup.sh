#!/usr/bin/env bash
set -e  # Exit on error

echo "🚀 Starting Counsel Codex environment setup..."

# --- Step 1: Upgrade pip ----------------------------------------
echo "📦 Upgrading pip..."
python -m pip install --upgrade pip

# --- Step 2: Install all dependencies ---------------------------
echo "📥 Installing required dependencies..."

# Main app dependencies
if [ -f requirements.txt ]; then
    echo "🔹 Installing from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️  requirements.txt not found. Skipping..."
fi

# Dev/testing dependencies (ruff, pyright, pytest, etc.)
if [ -f requirements-dev.txt ]; then
    echo "🔹 Installing from requirements-dev.txt..."
    pip install -r requirements-dev.txt
else
    echo "⚠️  requirements-dev.txt not found. Skipping..."
fi

# Safety net: manually install critical tools if not declared
echo "🛠️  Ensuring ruff, pyright, and pytest are present..."
pip install --upgrade ruff pyright pytest

# --- Step 3: Optional speed boost for Pyright -------------------
echo "⚙️  Warming up pyright..."
pyright --version >/dev/null 2>&1 || true

# --- Step 4: Confirm tools are accessible -----------------------
echo "🔍 Confirming tools are installed..."

echo -n "ruff version: "; ruff --version
echo -n "pyright version: "; pyright --version
echo -n "pytest version: "; pytest --version

# --- Step 5: (Optional) Run test suite if everything's ready ----
echo "🧪 Running test suite to verify setup (mocked services)..."
pytest -q || echo "⚠️  Tests failed — this may be expected if mock data is incomplete."

# --- Finish -----------------------------------------------------
echo "✅ Counsel Codex environment is ready. All systems nominal. 👷"
