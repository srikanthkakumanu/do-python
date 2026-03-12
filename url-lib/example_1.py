# Fetching data from URL
import urllib.request
import urllib.error
import json
from rich import print_json

def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            parsed_json = json.loads(data)
            return parsed_json
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None

def main():
    posts = get_posts()
    print_json(data=posts)

if __name__ == '__main__':
    main()