# mcb-lab
Coding task for mcb-lab involving Django restful

## Table of Contents

- [Design](#designs)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)

## Design

The model / database structure is composed out of Order, Customer, Specification and Pizza. The Order has a one-on-one relation with the Customer, the Order has a many-to-many relationship with Pizza through Specification. This way the order can be composed of whatever is specified in the Pizza database and the quantity and size are attributes of Specification.

I chose for this structure because it sets the foundation for a robust service. Whoever has permission to write to the pizza database can decide what is being served, also extra future attributes can be included e.g. pizza base price. From the Specification the elements as size and quantity can decide what the effect on the pizza base price can be. This setup gives modularity where it is needed.

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

```bash
psql -d postgres
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
```

### Populate pizzas database

visit: http://localhost:8000/pizzas/

Put the three pizzas in the pizzas database using the html form.

### Coding Task Requirements

* Order pizzas: (http://localhost:8000/orders/)
    * should be possible to specify the desired flavors of pizza, the number of pizzas and their size.
        * An example of a raw data PUT can be found in the path /pizza_ordering_service/tests/input/orders.json
    * An order should contain information regarding the customer.
        * Nested under customer in the order
    * It should be possible to track the status of delivery.
        * In the order as property called status
    * It should be possible to order the same flavor of pizza but with different sizes multiple times
        * Can be tried by adapting the raw data PUT can be found in the path /pizza_ordering_service/tests/input/orders.json
* Update an order: (http://localhost:8000/orders/{id}/)
    * It should be possible to update the details — flavours, count, sizes — of an order
        *
    * It should not be possible to update an order for some statutes of delivery (e.g. delivered).
        * Once the status of delivered is reached it cannot be updated
    * It should be possible to change the status of delivery.
        * The five stages of delivery are: created, paid, preparing, delivering, delivered.
* Remove an order.
* Retrieve an order: (http://localhost:8000/orders/{id}/)
    * It should be possible to retrieve the order by its identifier.
        * Possible with http://localhost:8000/orders/{id}/
* List orders: (http://localhost:8000/orders/)
    * It should be possible to retrieve all the orders at once.
        * Possible with http://localhost:8000/orders/
    * Allow filtering by status / customer.
        * Possible with url and UI filter button in right top corner. (http://localhost:8000/orders/?status=created&customer__name=Dylan+Bartels)

### Example post

```json
{
    "customer": {
        "name": "Dylan Bartels",
        "address": "Kantstrasse 86",
        "city": "Berlin",
        "zip_code": "781644"
    },
    "pizzas": [
      {
        "flavor": "margherita",
        "size": "small",
        "quantity": 10
      },
      {
        "flavor": "pepperoni",
        "size": "large",
        "quantity": 4
      }
    ],
    "payment": true,
    "status": "created"
}
```

## Tests

```bash
python manage.py test
```
