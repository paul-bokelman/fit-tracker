import json
from termcolor import colored

config = json.load(open('config.json'))

def subfield(str: str):
    return input(colored(str, color="grey"))

def success(str: str):
    print(colored(str, color="green"))