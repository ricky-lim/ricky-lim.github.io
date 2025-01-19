# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "numpy~=2.0",
# ]
# ///

import numpy as np
import time
import os
import argparse

CURRENCIES = {
    'dollar': '$',
    'euro': '€'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def money_rain(currency='euro', width=50, height=10):
    money_symbol = CURRENCIES[currency]
    print(f"Starting {currency.title()} Rain...")
    try:
        screen = np.random.choice([' '] * 9 + [money_symbol], size=(height, width))
        while True:
            clear_screen()
            print('\n'.join(''.join(row) for row in screen))
            screen = np.roll(screen, 1, axis=0)
            screen[0] = np.random.choice([' '] * 9 + [money_symbol], size=width)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{currency.title()} Rain Terminated!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Money Rain Visualization')
    parser.add_argument('--currency', choices=['euro', 'dollar'], default='euro', help='Currency symbol to display')
    args = parser.parse_args()
    money_rain(currency=args.currency)