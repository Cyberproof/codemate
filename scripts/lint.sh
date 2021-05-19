#!/usr/bin/env bash

set -e
set -x

mypy codemate
flake8 codemate
black codemate --check
isort codemate --check-only
pylint codemate