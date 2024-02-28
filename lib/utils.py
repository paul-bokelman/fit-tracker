import os
import json
from termcolor import colored

config = json.load(open(os.path.join(os.path.dirname(__file__).replace("/lib",""), "config.json")))

def subfield(str: str):
    return input(colored(str, color="grey"))

def success(str: str):
    print(colored(str, color="green"))