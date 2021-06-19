from app.tasks import read_reddit, say_hello
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sub", default="alpp")
args = parser.parse_args()


result = say_hello.delay(f"{args.sub}")
print(result.get(), flush=True)

