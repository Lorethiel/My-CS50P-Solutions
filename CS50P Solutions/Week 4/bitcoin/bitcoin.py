import json
import requests
import sys

def main():
    if len(sys.argv) < 2:
        print('Missing command-line argument')
        sys.exit(1)
    number = get_number(sys.argv[1])
    op = btc_to_usd(number)
    print(op)


def get_number(arg):
        try:
            y = float(arg)
            return y
        except ValueError:
            print('Command-line argument is not a number')
            sys.exit(1)


def btc_to_usd(x):
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    rate = data['bpi']['USD']['rate_float']

    result = float(x*rate)

    return f"${result:,.4f}"



main()













