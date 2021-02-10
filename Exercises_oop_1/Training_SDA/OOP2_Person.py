# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:26:54 2021

@author: 48695
"""

from datetime import date

class Person():
    
    def __init__(self, name: str, surname: str, birthday: date):
        self._name = name
        self._surname = surname
        self._birthday = birthday
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
        
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, value: str):
        self._surname = value
    
    @property
    def birthday(self):
        return self._birthday
    
    @birthday.setter
    def birthday(self, value: date):
        self._birthday = value
        
        
class Employee(Person):
    Number = int(input("Enter your birthday date: "))
    if Number > 2020 or Number < 1920:
        print(birthday = 0)
        
    