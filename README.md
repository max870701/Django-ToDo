# Django Todo App

A simple Todo application built with Django and Docker.

## Requirements

- Docker
- Python 3.10

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installation

1. Clone the repository
```bash
git clone https://github.com/max870701/Django-ToDo.git 
```

2. Build up the Dockerfile
```bash
docker build -t django-todo:latest .
```

3. Run the Docker Image
```bash
docker run -p 8001:8001 django-todo:latest
```