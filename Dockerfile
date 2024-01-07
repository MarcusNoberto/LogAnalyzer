FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /LogAnalyzer
RUN apk --no-cache add build-base
COPY . .

EXPOSE 8000

RUN pip install --upgrade pip setuptools && \
    pip install -r requirements.txt 

CMD python3.8 /LogAnalyzer/manage.py makemigrations && \
    python3.8 /LogAnalyzer/manage.py migrate && \
    python3.8 /LogAnalyzer/manage.py runserver 0.0.0.0:8000