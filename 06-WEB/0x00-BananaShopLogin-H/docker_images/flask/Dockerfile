FROM python:3.8

WORKDIR /CTF/flask/app

COPY . /CTF/flask/app

COPY flag.txt /

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
