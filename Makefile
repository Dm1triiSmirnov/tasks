install:
	poetry install

test_task1:
	poetry run pytest task1/tests.py -vvv


test_task2:
	poetry run pytest task1/tests.py -vvv
