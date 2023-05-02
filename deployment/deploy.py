from flask import Flask, render_template , request
import joblib
import pandas as pd
import numpy as np
import pickle
import time


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/edit' , methods = ['post'])
def function_execute():
    a = request.form.get('product')
    b = request.form.get('stock')
    d = request.form.get('add_remove')
    c = request.form.get('items')
    df = pd.read_csv("https://raw.githubusercontent.com/mohammedisrar/army_project/main/DATA.csv")
    if d == 'remove':
        if b == 'new':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_new'].values[0]
                except:
                    data = 'First add the product in the list'
                    return render_template('output.html',data = data)
                exist -= c
                df.at[df.loc[df['available_items'] == a].index[0], 'available_amount_new'] = exist
                data = 'Task complete'
                return render_template('output.html',data = data)
            else:
                data = 'The product not avaliable'
                return render_template('output.html',data = data)
        elif b == 'old':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_old'].values[0]
                except:
                    data = 'First add the product in the list'
                    return render_template('output.html',data = data)
                exist -= c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_old']  = exist
                data = 'Task complete'
                return render_template('output.html',data = data)
            else:
                data = 'The product not avaliable'
                return render_template('output.html',data = data)
        else:
            data = 'enter valid stock'
            return render_template('output.html',data = data)
    elif d == 'add':
        if b == 'new':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_new'].values[0]
                except:
                    data = 'First add the product in the list'
                    return render_template('output.html',data = data)
                exist += c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_new']  = exist
                data = 'Task complete'
                return render_template('output.html',data = data)
            else:
                data = 'The product not avaliable'
                return render_template('output.html',data = data)
        elif b == 'old':
            if a in df['available_items'].values:
                try:
                    exist = df.loc[(df['available_items'] == a)]['available_amount_old'].values[0]
                except:
                    data = 'First add the product in the list'
                    return render_template('output.html',data = data)
                exist += c
                df.at[df.loc[df['available_items'] == a].index[0] , 'available_amount_old']  = exist
                data = 'Task complete'
                return render_template('output.html',data = data)
            else:
                data = 'The product not avaliable'
                return render_template('output.html',data = data)
        else:
            data = 'enter valid stock'
            return render_template('output.html',data = data)


app.run(debug = True)