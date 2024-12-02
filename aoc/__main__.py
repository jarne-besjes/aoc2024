from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-d', "--day", type=int, help="aocday")
args = parser.parse_args()

def main():
    day = args.day
    exec (f"from .days import day{day}")
    exec(f"day{day}.run()")
    return 0


if __name__ == "__main__":
    exit(main())