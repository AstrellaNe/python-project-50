install:
	poetry install
	
help:	
	poetry run gendiff -h

build:
	poetry build

publish: 
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
	
package-reinstall:
	pip install --user --force-reinstall dist/*.whl

generate-diff:
	poetry run gendiff

lint:	
	poetry run flake8

selfcheck:
	poetry check

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
	cc-test-reporter after-build -t coverage.py

git-prepare:
	make build
	make package-reinstall
	git add .
