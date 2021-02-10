# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:55:23 2021

@author: 48695
"""

from datetime import date

from sda_exercises_oop_2_mz.person import Person


class Employee(Person):
    Number = int(input("Enter your birthday date: "))
    if Number > 2020 or Number < 1920:
        birthday = 0
        
    