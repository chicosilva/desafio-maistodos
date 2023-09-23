# Clean .pyc
clean:
	@echo "Cleaning cache..."
	@find . | egrep '.pyc|.pyo|pycache' | xargs rm -rf
	@find . | egrep '.pyc|.pyo|pycache|pytest_cache' | xargs rm -rf
	@rm -rf ./pycache
	@rm -rf ./.pytest_cache
	@rm -rf ./.mypy_cache
	@echo "Cache cleared!"

# Tool For Style Guide Enforcement
format:
	@echo "Start isort execution:"
	@poetry run isort ./app ./tests
	@echo "Finished isort execution."
	@echo ""

	@echo "Start black execution:"
	@poetry run black ./app ./tests --target-version py310
	@echo "Finished black execution."
	@echo ""

checker:
	@echo "Start flake8 execution:"
	flake8 ./tests
	@echo "Finished flake8 execution."
	@echo ""

	@echo "Start pylint execution:"
	pylint ./app/
	@echo "Finished pylint execution."
	@echo ""

	@echo "Start mypy execution:"
	mypy ./app
	@echo "Finished pylint execution."
	@echo ""

	@echo "Start bandit execution:"
	bandit -v -r ./ -c "requirements.txt"
	@echo "Finished bandit execution."
	@echo ""

# Run app local
run:
	uvicorn app.main:application --port 8000 --workers 3 --reload

# Dev tools
localdb:
	@docker run --name basic-postgres --rm -e POSTGRES_USER=todos_dev -e POSTGRES_PASSWORD=todos_dev -p 5432:5432 -it postgres:14.1-alpine

docker-build:
	@docker build -t application .

docker-run:
	@docker run -it -p 8000:8000 application

# Tests Commands
test:
	@poetry run pytest --cov

test-report:
	@poetry run pytest --cov-report html --cov

# Migrations
migrations:
	@poetry run alembic upgrade heads


