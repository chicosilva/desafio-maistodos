FROM python:3.10-slim-bullseye as prod

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    netcat git \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Create the /app/src directory
WORKDIR /app/src

# Copy the requirements.txt
COPY requirements.txt .

# run gcc
RUN apt-get purge -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY . .

CMD ["sh", "./startup.sh"]

FROM prod as dev

EXPOSE 8000