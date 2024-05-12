install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --break-system-packages --user dist/*.whl

prompt:
	poetry add prompt

lint:
	poetry run flake8 gendiff