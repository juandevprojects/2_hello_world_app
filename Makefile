install:
	python -m pip install --upgrade pip &&\
		python -m pip install -r requirements.txt

lint:
	python -m pylint --disable=R,C app/ tests/

format:
	python -m black app/ tests/

test:
	python -m pytest -vv --cov=tests --cov=app
