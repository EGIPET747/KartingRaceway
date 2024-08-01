#!/bin/sh

# запуск сервера
exec npm run build
exec npm run serve --omit=dev
