FROM python:3.7

ENV PYTHONUNBUFFERED 1

ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt

CMD ["echo", "celery-dockerfile-is-loaded!"]
