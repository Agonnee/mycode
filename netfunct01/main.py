#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import json
from colorama import init, Fore, Back, Style
init(autoreset=True)

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print(Fore.RED + 'Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print(Fore.GREEN + 'Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here


# reboot func
def devicereboot(iplist):
    for i in iplist:
        print(Fore.GREEN + "Connecting to.. " + i)
        print(Fore.BLUE + "REBOOTING NOW!")


# start our main script
def main():
    
    infileask = input("Do you have a an input file for me? (Y/N):  ")
    
    if infileask.lower() == "n":
         work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1": ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    else:
        filetoread = input("What is the Input File?")
        with open(filetoread, "r") as inputfile:
            work2do = json.load(inputfile)
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()

