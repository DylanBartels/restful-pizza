#!/bin/bash
psql -d postgres << EOF
DROP DATABASE mcb_lab_dylan_bartels;
CREATE DATABASE mcb_lab_dylan_bartels;
GRANT ALL PRIVILEGES ON DATABASE mcb_lab_dylan_bartels TO admin;
ALTER USER admin CREATEDB;
EOF
python manage.py makemigrations pizza_ordering_service
python manage.py migrate
exit
