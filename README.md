# mcb-lab
Coding task for mcb-lab involving Django restful

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)

## Requirements

- python3
- postgresql
  - https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3


## Installation

### Project

```bash
git clone https://github.com/DylanBartels/mcb-lab.git
cd mcb-lab
python3 -m venv env
source env/bin/activate
pip install requirements.txt
```

### Database

```sqlp
CREATE DATABASE mcb_lab_dylan_bartels;
CREATE USER admin WITH ENCRYPTED PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE mcb_lab_dylan_bartels TO admin;
ALTER USER admin CREATEDB;
```

```bash
python manage.py makemigrations pizza_ordering_service
python manage.py migrate
```

## Usage

```bash
pg_start
python manage.py runserver
pg_stop
```



## Tests

```bash
python manage.py test
```
