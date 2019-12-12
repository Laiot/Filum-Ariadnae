FROM python:3.6
COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=main.py FLASK_ENV=development FLASK_DEBUG=1 PYTHONUNBUFFERED=0

CMD flask run --host 0.0.0.0 