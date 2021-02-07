# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:12:41 2021

@author: 48695
"""
import pickle

def pickle_write(items: list):
    try:
        with open("./data.pickle" , "wb") as fd:
             pickle.dump(items , fd)
             print(pickle.dumps(items))
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format info: {e.args}')