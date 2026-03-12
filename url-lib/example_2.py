# Fetching data from URL
from rich import print_json
import requests


def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    parsed_json = response.json()
    return parsed_json

def get_posts_with_errors():
    url = 'https://jsonplaceholder.typicode.com/xyz'
    try:
        response = requests.get(url)
        response.raise_for_status()
        parsed_json = response.json()
        return parsed_json
    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error: {e}')
    except requests.exceptions.RequestException as e:
        print(f'Request Error: {e}')

def get_posts_with_query_params(user_id=1):
    url = 'https://jsonplaceholder.typicode.com/posts'
    params = {'userId': user_id}
    response = requests.get(url, params=params)
    parsed_json = response.json()
    return parsed_json

def save_post(data):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.post(url, json=data)
    parsed_json = response.json()
    return parsed_json


def main():
    posts = get_posts()
    print_json(data=posts)

    posts_by_user = get_posts_with_query_params(user_id=1)
    print_json(data=posts_by_user)

    response = save_post({
        'title': 'Mario Party!',
        'body': 'Okie Dokie!',
        'userId': 1
    })
    print_json(data=response)

    posts_with_errors = get_posts_with_errors()
    print_json(data=posts_with_errors)

if __name__ == '__main__':
    main()