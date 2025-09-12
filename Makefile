install:
	python -m pip install --upgrade pip &&\
		python -m pip install -r requirements.txt

lint:
	python -m pylint --disable=R,C hello_world.py

format:
	python -m black *.py

test:
	python -m pytest -vv --cov=hello_world test_hello_world.py
