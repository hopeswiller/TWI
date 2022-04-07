# Date Generator

> An application to generate an expiration date for products

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Features](#features)
- [Status](#status)

## General info

This project is primarily developed to generated expiration dates given a production date.


## Technologies

- Python - version 3.8
- Flask
#### Resources
- https://pyfpdf.readthedocs.io/en/latest/reference/cell/index.html
- https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f

## Setup

Setup can be done manually or via Docker which is recommended
#### Manual

> - pip install -r requirements.txt
> - export FLASK_APP=src
> - export FLASK_ENV=development
> - flask run

#### Docker

> - docker compose up


## Features

List of features ready and TODOs for future development

- [x] Choose a production a date over a period
- [x] Download PDF file with production dates and their respective expiration dates
- [x] Added pre-commit hooks


TODOs:

- [ ] Sends an email with PDF attachment
- [ ] Configure sphinx docs
- [ ] Add more tests


## Status

Project is: _in progress_
