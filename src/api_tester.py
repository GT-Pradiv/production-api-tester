import requests
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(
        description="A simple command-line API tester built for SaaS support."
    )

    parser.add_argument(
        'url',
        type=str,
        help="The URL of the API endpoint to test."
    )

    parser.add_argument(
        '-m','--method',
        default='GET',
        choices=['GET', 'POST', 'PUT', 'DELETE'],
        help="HTTP method to use (default: GET)."
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()
    print(f"Sending a {args.method.upper()} request to {args.url}...")
    try:
        response = requests.request(args.method, args.url)
        print("-" * 30)
        print(f"Status Code: {response.status_code}")
        print("Response Body: ")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
