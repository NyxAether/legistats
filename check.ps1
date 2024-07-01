black legistats tests
autoflake -r --in-place legistats tests
isort legistats tests
mypy legistats tests
flake8 legistats tests
pylint legistats tests