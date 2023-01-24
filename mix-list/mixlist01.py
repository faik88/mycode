#!/usr/bin/env python3
my_list = [ 5060, "80", 55, "192.168.0.5", "10.10.10.1", "ssh" ]
print("The first item in the list (IP): " + str(my_list[0]) )
print("The second item in the list (port): " + my_list[1] )
print("The last item in the list (state): " + str(my_list[2]) )

print("ip addresses only: " + my_list[3] , my_list[4])


