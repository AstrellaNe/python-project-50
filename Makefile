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
	poetry run generate-diff

lint:	
	poetry run flake8

git-prepare:
	make build
	make package-reinstall
	git add .