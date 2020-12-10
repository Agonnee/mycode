#!/usr/bin/env python3

import requests

jigglypuff = requests.get('https://pokeapi.co/api/v2/pokemon/jigglypuff/')
print(jigglypuff)

