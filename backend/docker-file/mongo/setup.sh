#!/bin/bash
mongo <<EOF
use admin;
db.auth('root', '123456');
use dmx_aluminum;
db.createUser({user:'test',pwd:'test',roles:[{role:'readWrite',db:'Kanban'}]});
db.createCollection("user");
EOF
# create a user with username:test and password:test for r/w database Kanban