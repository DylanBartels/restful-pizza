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

## Usage

```bash
python manage.py runserver
```

## Tests
