FROM python:3.9.5-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

WORKDIR /app
COPY /app /app

EXPOSE 5000

CMD ["sh", "gunicorn.sh"]


