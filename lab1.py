#Program to demonstrate how to convert a decimal number into a binary number
#and to also convert a binary number to decimal afterwards.
# Name: Paul Moran
# Student No.: C12370211
# 19/09/2013


num_str = input("Enter an Integer  ")
my_int = int(num_str)
zero = ("The number entered was 0.")
invalid = ("You've entered a negative number.")

binstr = ""
import math
if my_int > 0:
    while my_int > 0:
        temp = my_int
        my_int = my_int//2
        binstr = str(temp%2) + binstr
    print (num_str,' converted to binary is ',binstr)
    print ("\n")

elif my_int ==0:
    print (zero)
    print ("\n")

elif my_int < 0:
    print (invalid)
    print ("\n")

print
print ("Now, time to do the opposite. ")

bin_str = input("Please enter a binary number ")
number_int = str(bin_str)

new_int = 0
power = 0

temp_bin = bin_str

while len(temp_bin)>0:
    bit=int(temp_bin[-1])
    new_int= (new_int + bit*(2**power))
    temp_bin = temp_bin[:-1]
    power+=1
            
print (bin_str,' converted to an integer is ',new_int)
print ("\n")

print ("Press enter to exit!")
input ("")
