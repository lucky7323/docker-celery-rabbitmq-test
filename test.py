from tasks import read_reddit
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sub", default="alpp")
args = parser.parse_args()


result = read_reddit.delay(f"{args.sub}")
print(result.get())

