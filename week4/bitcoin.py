import sys
import requests


try:
    if len(sys.argv) == 2:
        n = float(sys.argv[1])
    elif len(sys.argv) < 2:
        raise Exception('Missing command-line argument')
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
    rate = response['bpi']['USD']['rate_float']
    amount = rate * n
    print(f"${amount:,.4f}")

except ValueError:
    sys.exit('Command-line argument is not a number')

except requests.RequestException:
    sys.exit()