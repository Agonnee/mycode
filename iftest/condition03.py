#!/usr/bin/env python3

# Collect input
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string

## Inform user of config
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("Hostname matches expected config")

## Notify End
print("Exiting...")
