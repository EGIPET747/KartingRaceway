#!/bin/sh

SERVER_HOST="0.0.0.0"
SERVER_PORT=8000
SERVER_THREADS=4

# запуск сервера
exec uvicorn \
  --host ${SERVER_HOST} \
  --port ${SERVER_PORT} \
  --workers ${SERVER_THREADS} \
  backend.main:app
