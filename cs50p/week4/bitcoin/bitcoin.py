import requests
import sys

def main():
    if len (sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            price(n)

        except ValueError:
            sys.exit('Command-line argument is not a number')


    else:
        sys.exit('Missing command-line argument')



def price(i):
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        price = response['bpi']['USD']['rate_float']
        total = price * i
        print (f'${total:,.4f}')

    except requests.RequestException:
        return None



main()
