#!/bin/bash

echo POSTGRES_DB=$POSTGRES_DB >> .env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> .env
echo POSTGRES_USER=$POSTGRES_USER >> .env
echo PGDATA=$PGDATA >> .env
echo HOST=$HOST >> .env
echo USER=$USER >> .env
echo PASSWORD=$PASSWORD >> .env
