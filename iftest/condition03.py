#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be :"+hostname)
    print("hostname matches expected config")
else:
    print("hostname is "+hostname+", you didn't enter the correct value")


## Always print out to the user
print("Exiting the script")

