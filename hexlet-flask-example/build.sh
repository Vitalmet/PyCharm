#!/usr/bin/env bash

# Если DATABASE_URL не задан, используем стандартное подключение
if [ -z "$DATABASE_URL" ]; then
    echo "Ошибка: переменная DATABASE_URL не установлена"
    echo "Пример: export DATABASE_URL=postgresql://username:password@localhost:5432/dbname"
    exit 1
fi

# Более простой и надёжный способ - использовать psql с URL напрямую
# psql поддерживает формат URL начиная с версии 9.2

# Просто передаём URL напрямую в psql
psql "$DATABASE_URL" -a -f init.sql

if [ $? -eq 0 ]; then
    echo "База данных успешно инициализирована"
else
    echo "Ошибка при инициализации базы данных"
    exit 1
fi