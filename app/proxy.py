from fake_useragent import UserAgent
import requests


def get_session():
    session = requests.session()
    session.proxies = {'http': 'rproxy:5566', 'https': 'rproxy:5566'}
    session.headers = get_header()
    return session


def get_header():
    ua = UserAgent()
    header = {'User-Agent': str(ua.random)}
    return header

