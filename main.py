# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
###
# Project by Lucas Silva
# Date: 10/20/2022
# Subject : Cryptographic Sytem - Simple-DES implementation in python
# Not sure if I will manage to do it
#For the the table I'm following the data from Steven Gordon video you can find here https://www.youtube.com/watch?v=3jGMCyOXOV8&t=1349s
# ###


from sys import exit
from time import time
#All the lenght of the key, table
KeyLenght = 10
PlaintextLenght = 8
CipherLenght = 8
SubKeyLenght = 8
FLenght = 4

# We will define now all the table for permutation (a1,a2,a3,...,a10) we will use in key generation
BaseBit = (1,2,3,4,5,6,7,8,9,10)
P10 = (3,5,2,7,4,10,1,9,8,6) #Permutation of 10 bits to 10 bits define in advance
P8 = (6,3,7,4,8,5,10,9) #Permtutaion and we remove to bits
#For Enncryption and Decryption and Fk
IPermutation = (2,6,3,1,4,8,5,7) #Initial Permutation => 8 bits to 8 bits
EPermutation= (4,1,2,3,2,3,4,1) #Expension permutation => 4 bits to 8 bits
S0table = (1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2)
S1table = (0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3)
P4table = (2, 4, 3, 1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hello World')