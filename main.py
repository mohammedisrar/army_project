import pandas as pd
import numpy as np
import pickle
import time


available_new = {'Table': 50,
 'Chair': 150,
 'Bed': 25.0,
 'Rack': 75.0,
 'Almirah': 70.0,
 'Fan': 70.0,
 'Geyser': 70.0,
 'AC': 70.0,
 'Refrigerator': 65.0,
 'Water cooler': 70.0}


available_old = {'Table': 50,
 'Chair': 150,
 'Bed': 25.0,
 'Rack': 75.0,
 'Almirah': 70.0,
 'Fan': 70.0,
 'Geyser': 70.0,
 'AC': 70.0,
 'Refrigerator': 65.0,
 'Water cooler': 70.0}

def function_execute():
    a = input('Which product ?').title()
    b = input('Which stock new or old? ')
    d = input('Do you want to remove or add the ? ')
    c = int(input('Enter how many are removed or added? '))
    if d == 'remove':
        if b == 'new':
            if a in available_new:
                try:
                    exist = available_new[a]
                except:
                    print('First add the product in the list')
                    return None
                exist -= c
                available_new.update({a:exist})
            else:
                print('The product not avaliable')
        elif b == 'old':
            if a in available_old:
                try:
                    exist = available_old[a]
                except:
                    print('First add the product in the list')
                    return None
                exist -= c
                available_old.update({a:exist})
            else:
                print('The product not avaliable')
        else:
            print('enter valid stock')
    elif d == 'add':
        if b == 'new':
            if a in available_new:
                try:
                    exist = available_new[a]
                except:
                    print('First add the product in the list')
                    return None
                exist += c
                available_new.update({a:exist})
            else:
                print('The product not avaliable')
        elif b == 'old':
            if a in available_old:
                try:
                    exist = available_old[a]
                except:
                    print('First add the product in the list')
                    return None
                exist += c
                available_old.update({a:exist})
            else:
                print('The product not avaliable')
        else:
            print('enter valid stock')

function_execute()

print(available_new)
print(available_old)