from os import environ
from celery import Celery
import proxy
import requests


environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')


@app.task
def say_hello(name: str):
    return f"Hello {name}"


@app.task(bind=True)
def read_reddit(self, subreddit: str):
    base_url = "https://www.reddit.com"
    url = f"{base_url}/r/{subreddit}/new.json?limit=100"
    print(f">>> request to {url}")
    session = proxy.get_session()
    response = session.get(url)
    print(response.status_code)
    print(response.text)

