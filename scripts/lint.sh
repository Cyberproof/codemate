#!/usr/bin/env bash

set -e
set -x

mypy codemate tests
flake8 codemate tests
black codemate tests --check
isort codemate tests --check-only
pylint codemate tests