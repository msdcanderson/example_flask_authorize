# example_flask_authorize

## Instructions to run

```bash
pipenv run python .\src\app.py
```

The script creates Area Manager 1 and Store Manager 1

## Flask-Authorize example app

Use this as an example to test the RBAC / ACL provided by the extension [flask-authorize](https://github.com/bprinty/Flask-Authorize).

Requirements for store permissions:

- Users
    - Area Manager, can add/update/delete/view all stores
    - Store 1 Manager, can view all stores in area 1, and update store 1 details
    - Store 1 Employee, can view store 1 details in area 1
    - Store 2 Manager, can view all stores in area 1, and update store 2 details
    - Store 2 Employee, can view store 2 details in area 1
    - Store 3 Manager, can view all stores in area 2, and update store 3 details
    - Store 3 Employee, can view store 1 details in area 2

- Groups
    - Store 1
    - Store 2
    - Store 3

- Roles
    - add
    - update
    - delete
    - view