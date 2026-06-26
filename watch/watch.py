import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'.*"(https|http)://(www\.)?youtube\.com/embed/(?P<embed_link>\w*).*', s)
    if match:
        return(f"https://youtu.be/{match.group('embed_link')}")

if __name__ == "__main__":
    main()