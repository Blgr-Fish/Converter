# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:20:28 2022

@author: zijja
"""

import tkinter 
from typing import Union



#centimeters_to :

def cm_mm(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' centimeter(s) is equal to ' + str(value*10) +' millimeter(s)'

def cm_m(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' centimeter(s) is equal to ' + str(value/100) +' meter(s)'

def cm_km(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' centimeter(s) is equal to ' + str(format((value/100000),'4f')) +' kilometer(s)'

def cm_mile(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' centimeter(s) is equal to ' + str(format((value/160934),'f')) + ' mile(s)'

    #meters_to :
    
def m_mm(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' meter(s) is equal to ' + str(value*1000) +' millimeter(s)'

def m_cm(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' meter(s) is equal to ' + str(value*100) +' centimeter(s)'

def m_km(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' meter(s) is equal to ' + str(value/1000) +' kilometer(s)'

def m_mile(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' meter(s) is equal to ' + str(value/1609) + ' mile(s)'


#kilometers_to :
    
def km_mm(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' kilometer(s) is equal to ' + str(value*1000000) +' millimeter(s)'

def km_cm(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' kilometer(s) is equal to ' + str(value*100000) +' centimeter(s)'

def km_m(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' kilometer(s) is equal to ' + str(value*1000) +' meter(s)'

def km_mile(value:Union[int,float]) -> Union[int,float] :
    assert value >= 0
    return str(value) + ' centimeter(s) is equal to ' + str(value/1.609) + ' mile(s)'


