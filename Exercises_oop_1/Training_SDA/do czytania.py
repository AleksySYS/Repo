# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:32:11 2021

@author: 48695
"""
import csv

def csv_read(users_list):
    users = []
    try:
        with open('./data.csv', 'r') as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:      
                    users.append(row)
                    
     except(IOError, Exception) as e
         print("noope")
     return users
     
def main():
    users = [
        ("John" , "Smith", 132421),
        ("Dihn" , "Amith", 222421),
        ]
    csv_write(users)
    returned_users = csv_read()
    print(returned_users)