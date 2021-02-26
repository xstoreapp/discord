FROM python:latest

ARG TOKEN

ENV TOKEN=${TOKEN}

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]