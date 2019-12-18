"""
This script will take pull crypto coin data
from different APIs as they are added to this project.

These scripts will be called via a bash script
on a Google compute engines.
"""

import argparse
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd


####################
# Helper Functions #
####################


def grabber():
    ## create parser object
    parser = argparse.ArgumentParser(description='Pull crypto prices')

    ## the add argument method tells AP how to take the strings on the command line and turn them into objects
    parser.add_argument(
        '--coin',
        default='bitcoin',
        type=str,
        help='Choices include either BTC, ETH, ALL')

    ## optional argument from
    parser.add_argument(
        '--from',
        # dest='api',
        action='store_const',
        const=sum,
        default='coinmarket',
        help='either coinmarket or coingecko')

    ## parse_args will return an object with two attributes, bitcoin and accumulate. The bitcoin attribute will be a list of one or more strings.
    ## and the destination attribute will be either the



    return parser


def pull_prices():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'not the key',
        ## the real key is 08ee4031-d7f6-4d1a-92a7-6ada2cadfca1
    }

    session = Session()
    session.headers.update(headers)

    try:
        ## to get coin market cap api with the key you have
        ## on this session and assign it to a variable
        response = session.get(url, params=parameters)
        ## load the text as a string using json
        d = json.loads(response.text)
        for coin in d["data"]:
            ## why is flat_coin_data a variable???
            ## and why is it allowed to only pass in one variable
            ## when the function specifies two
            ## if you save a method call in a variable
            ## the method still gets called?
            flat_coin_data = massage_data(coin)
            break
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

def massage_data(d, key=''):

    msgd_data = []
    ds = d.items() # items() returns a list of all the keys and values in a Dictionary

    for k, v in ds:
        new_key = key + '_' + k if key else k
        bulky = isinstance(v, dict)

        if bulky: ## if v is a dict

            layer = massage_data(v, key=new_key).items() # recursion
            print(layer)
            msgd_data.extend(layer) ## extend list with list
        ## not able to make this an elif "is v an instance of a tuple
        else:  # not a dict, append tuple pair
            msgd_data.append((new_key, v)) # add item to list

    return dict(msgd_data)

def main():
    # args = grabber().parse_args()
    # print(args)
    # pull_prices(args.coin)
    # print(args)
    pull_prices()

if __name__ == "__main__":
    main()
