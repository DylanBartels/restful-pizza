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

```bash
git clone https://github.com/DylanBartels/mcb-lab.git
cd mcb-lab
python3 -m venv env
source env/bin/activate
pip install requirements.txt
python manage.py makemigrations pizza_ordering_service
python manage.py migrate
```

todo:
- add installation psql

## Usage

```bash
python manage.py runserver
```

## Tests
