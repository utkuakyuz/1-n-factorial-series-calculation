# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:40:04 2020

@author: msi
"""
n = input("Enter the value of n: ")
def estimateE (n):
    E = 0
    factorial = 1  
    realvalue = 2.71828182845905
    tupl = []
    
    for i in range(1,(int(n)+1)):
        factorial = factorial*i
        E = E + (1/factorial)
        tupl.append(E)
        
    tupl = tuple(tupl)
    return "E = 1 + " + str(tupl).replace(","," +") + "\nEstimated Value : " + str(E + 1) + "\n" + "Error : " + str(realvalue - (E+1))


print(estimateE(n))