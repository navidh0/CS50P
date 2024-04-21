import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.match(r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"></iframe>', s):
        url = matches.group(1)
        return f"https://youtu.be/{url}"
    return None


if __name__ == "__main__":
    main()
