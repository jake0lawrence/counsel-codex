#!/usr/bin/env bash
set -e

# Install Python dependencies
python -m pip install -r requirements.txt

# Optionally install dev tools or other packages
python -m pip install -r requirements-dev.txt
