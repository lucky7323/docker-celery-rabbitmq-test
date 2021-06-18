from fake_useragent import UserAgent
import requests

ua = UserAgent()
header = {'User-Agent': str(ua.random)}
base_url = "https://www.reddit.com"

subreddit = "/r/alpp/"
list_type = "new"
limit = 99

url = f"{base_url}{subreddit}{list_type}.json?limit={limit}"
response = requests.get(url, headers=header)

print(response.status_code)
print(header)
