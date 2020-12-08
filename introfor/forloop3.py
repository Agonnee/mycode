#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]}, {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}, {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for i in farms:
    for k,v in i.items():
        if type(v) is list:
            for j in v:
                print(j)
        else:
            print(k,v)

