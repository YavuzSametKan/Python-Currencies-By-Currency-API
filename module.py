import json

import requests
from bs4 import BeautifulSoup

countries = ('AED', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CHF', 'CLP', 'CNY', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ETB', 'EUR', 'FJD', 'GBP', 'GEL', 'GHS', 'GMD', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SEK', 'SGD', 'SLL', 'SRD', 'SVC', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VND', 'XAF', 'XCD', 'XOF', 'XPF', 'ZAR', 'ZMW')
mainCurrency = "USD"
result = {}

def currencyRequest(mainCurrency, oppositeCurrency):
    if oppositeCurrency != mainCurrency:
        currencyRequests = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=" + mainCurrency + "&To=" + oppositeCurrency)
        currencySoup = BeautifulSoup(currencyRequests.text, "html.parser")
        price = float(currencySoup.find("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod").text.split()[0].replace(",",""))
        return price

for country in countries:
    if mainCurrency != country:
        result[country] = currencyRequest(mainCurrency, country)

result = json.dumps(result,sort_keys=True, indent=4)
doc = open("jsonDoc.txt","w")
doc.write("""*********************
{} TO ALL CURRENCIES
*********************
{}""".format(mainCurrency, result))











