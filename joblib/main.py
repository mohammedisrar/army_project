import pandas as pd
import numpy as np
import pickle
import time

df = pd.read_csv("C://Users//MIT//IdeaProjects//army_project//deployment//DATA.csv")

def function_execute():
    a = input('Which product ? : ').upper()
    b = input('Which stock new or old? : ').lower()
    d = input('Do you want to remove or add the ? : ').lower()
    c = int(input('Enter how many are removed or added? : '))
    if d == 'remove':
        if b == 'new':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_new'].values[0]
                except:
                    print('First add the product in the list')
                    return None
                exist -= c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_new']  = exist
            else:
                print('The product not avaliable')
        elif b == 'old':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_old'].values[0]
                except:
                    print('First add the product in the list')
                    return None
                exist -= c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_old']  = exist
            else:
                print('The product not avaliable')
        else:
            print('enter valid stock')
    elif d == 'add':
        if b == 'new':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_new'].values[0]
                except:
                    print('First add the product in the list')
                    return None
                exist += c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_new']  = exist
            else:
                print('The product not avaliable')
        elif b == 'old':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_old'].values[0]
                except:
                    print('First add the product in the list')
                    return None
                exist += c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_old']  = exist
            else:
                print('The product not avaliable')
        else:
            print('enter valid stock')

print(function_execute())


df.to_csv("DATA.csv")