
# API documentation - **Contact List**

This document presents the basic information of the **API - Contacts Lits**. For more information, contact the developers at [Contacts](#4-Contacts).

# Version control

| Date       | Version | Description          | Author                    |
|------------|---------|----------------------|---------------------------|
| 02/04/2023 | 0.1.0   | Project creation     | **Francisco de Assis** |

# Summary

1. [Product Overview](#1-Product-Overview)

2. [Endpoint List](#2-Endpoint-List)

3. [Environment Preparation](#3-Environment-Preparation)

4. [Contacts](#4-Contacts)

# 1. Product Overview 


# 2. Endpoints List

    URL: http://127.0.0.1:8000/docs


# 3. Environment Preparation
### Via Local 
1. Clone the api repository:
    ```shell
    git clone https://github.com/chicosilva/bravi.git
    ```

2. Install Poetry:
    > **_NOTE:_** Install Poetry (tool for dependency management and packaging)
    ```shell
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    > **_NOTE:_** Poetry basic usage - https://python-poetry.org/docs/basic-usage/

3. install the dependencies:
   > **_NOTE:_** poetry install -> create and activate the venv.
    ```shell
    poetry install
    ```
    Or
    ```shell
    make install
    ```

4. Configure environment variables:
    > **_NOTE:_** A local PostgreSQL database will be required, see the **.env-sample** file.
    ```shell
      create create a file .env and set the variables.
    ``

5. Run the application:
   - create postgres database (using Docker): 
     ```shell
     make localdb
     ```
   - run migrations:
     ``` make migrations ```

   - run the application
     ```shell
     poetry run uvicorn app.main:application --port 8000 --workers 3 --reload
     ```
     Or
     ```shell
     make run
     ```

6. For running unit tests locally:
   > **_NOTE:_** use the variable "TESTING=True" to run unit and integration tests.
   - Console coverage report:
     ```shell
     pytest --cov
     ```
   - Coverage report to html:
     ```shell
     pytest --cov-report html --cov
     ```

### Via docker-compose

1. Before uploading the environment with Docker, it is necessary to authenticate in GitHub Packages. Create a token by accessing
at [your GitHub profile settings](https://github.com/settings/profile) > Developer Settings >
Personal Access Tokens. To find out what permissions are required for the token, read the
[documentation](https://docs.github.com/en/packages/publishing-and-managing-packages/about-github-packages#about-tokens)
about GitHub Packages.

2. After creating the token, it is now possible to authenticate with GitHub Packages:
   ```
   echo "<personal_token>" | docker login ghcr.io -u <github_username> --password-stdin
   ```
   ### Minimum requirements   
   | requirement                                                   | release  |
   |---------------------------------------------------------------|----------|
   | [docker](https://docs.docker.com/get-docker/)                 | 19.03.0+ |
   | [docker-compose](https://github.com/docker/compose/releases/) | 1.26.0+  |

3. Copy the file [.env-sample](.env-sample) to a new file `.env` and set the required values in the environment variables. Then run the containers build:
   ```shell
   docker-compose up --build
   ```

   > **_NOTE:_** All dependencies on `pyproject.toml` will be installed in the build process.

   ### Exposed ports on the host system:
   
   | container             | port |
   |-----------------------|------|
   | todos_dev | 8000 |

# 4 Contacts

> Developer:
1. Francisco Silva - chicosilva1@gmail.com
