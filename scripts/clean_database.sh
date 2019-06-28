#!/bin/bash
psql -d postgres << EOF
DROP DATABASE mcb_lab;
CREATE DATABASE mcb_lab;
GRANT ALL PRIVILEGES ON DATABASE mcb_lab TO admin;
ALTER USER admin CREATEDB;
EOF

exit
