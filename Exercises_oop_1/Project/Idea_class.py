# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:20:07 2021

@author: 48695
"""

class Employee:
    def __init__(self, first, last, pay, hours):
        self.first = first
        self.last = last
        self.pay = pay
        self.hours = hours

   

your_employee = Employee(input("First name: "), input("Last name: "),
    int(input("Pay: ")), int(input("Hours: ")))
