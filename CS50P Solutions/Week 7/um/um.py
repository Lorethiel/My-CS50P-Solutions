import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    times = 0
    words = re.findall(r'\bum\b', s)
    times = len(words)
    return times




if __name__ == "__main__":
    main()
