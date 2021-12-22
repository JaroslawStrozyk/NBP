#!/usr/bin/python3

import requests


GET_NBP = ('EUR', 'GBP', 'USD', 'CHF')
HIS_NBP = 60

def GetCurrencyNBP(GET_NBP, HIS_NBP):

    for W in GET_NBP:
        url = 'http://api.nbp.pl/api/exchangerates/rates/a/' + W + '/last/' + str(HIS_NBP) + '/?format=json'
        waluty = requests.get(url).json()
        print(waluty)


GetCurrencyNBP(GET_NBP, HIS_NBP)
