import datetime
# Read an integer:
# a = int(input())
# Print a value:
# print(a)
seconds1 = int(input())
minutes1 = int(input())
hours1 = int(input()) 
seconds2 = int(input()) 
minutes2 = int(input()) 
hours2 = int(input())

total1 = minutes1 * 60 + hours1 * 3600 + seconds1

total2 = minutes2 * 60 + hours2 * 3600 + seconds2
print(total2 - total1)