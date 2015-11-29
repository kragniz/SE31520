supplier-api
============

This is the API for the wine service.

To install, cd to this directory and run:

```bash
$ pip install .
```

API
---

- `/api`

    - `GET` - get the list of endpoints

- `/api/wines`

    - `GET` - get the list of wines

- `/api/wines/<id>`

    - `GET` - get the details for a particular wine

- `/api/orders`

    - `GET` - get the id for a particular order transaction

- `/api/orders/<id>`

    - `GET` - get the details about an order

    - `POST` - add details and complete the order
