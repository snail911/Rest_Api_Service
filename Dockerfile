# Базовый образ Python
FROM python:3.10

# Установка зависимостей
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Копирование исходного кода приложения
COPY ./app /code/app



# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5555"]

