
# API documentation - ** Mais Todos CardCredit **

This document presents the basic information of the **API - Mais Todos CardCredit **. For more information, contact the developers at [Cards](#4-Cards).

# Version control

| Date       | Version | Description          | Author                    |
|------------|---------|----------------------|---------------------------|
| 02/04/2023 | 0.1.0   | Project creation     | **Francisco de Assis** |

# Summary

1. [Product Overview](#1-Product-Overview)

2. [Endpoint List](#2-Endpoint-List)

3. [Environment Preparation](#3-Environment-Preparation)

4. [Cards](#4-Cards)

# 1. Product Overview 


# 2. Endpoints List

    URL: http://127.0.0.1:8000/docs


# 3. Environment Preparation
### Via Local 
1. Clone the api repository:
    ```shell
    git clone git@github.com:chicosilva/desafio-maistodos.git
    ```

2. Create Virtual Env:
    > **_NOTE:_** Install Pip (tool for dependency management and packaging)
    ```shell
    python3 -m venv .venv
    ```

3. install the dependencies:
   > **_NOTE:_** active the virtualenv: source .venv/bin/activate  
    ```shell
    pip install -r requirements.txt
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

   ### Exposed ports on the host system:
   
   | container             | port |
   |-----------------------|------|
   | maistodos-app | 8000 |

# 4 Contacts

> Developer:
1. Francisco Silva - chicosilva1@gmail.com
