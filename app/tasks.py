from celery import Celery
from app.proxy import get_session
import requests


app = Celery("tasks")
app.config_from_object("app.config:CelerySettings")


@app.task
def say_hello(name: str):
    return f"Hello {name}"


@app.task
def read_reddit(subreddit: str):
    base_url = "https://www.reddit.com"
    url = f"{base_url}/r/{subreddit}/new.json?limit=100"
    print(f">>> request to {url}")
    session = get_session()
    response = session.get(url)
    print(response.status_code)
    print(response.text)

