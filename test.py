from tasks import say_hello
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="eunho")
args = parser.parse_args()


result = say_hello.delay(f"{args.name}")
print(result)

