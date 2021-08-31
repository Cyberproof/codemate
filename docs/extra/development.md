# Development

Use the following command to execute the linters and the unit tests.

Make sure that the linters and the unit tests pass and that the unit tests coverage
is above 90%:

`scripts/test.sh`

Use "pytest-cov" to only execute the unit tests:

`pytest --cov=codemate --cov=tests`

Use the following command to make sure that the linters are passing:

`scripts/lint.sh`

Use "pre-commit" to run the active and passive linters:

* `pre-commit install` - run on every commit.
* `pre-commit run --all-files` - run manually on the repository.
