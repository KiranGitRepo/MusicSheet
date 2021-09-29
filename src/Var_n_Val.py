#!/usr/bin/env python
# coding: utf-8

# In[3]:
  
TREBLENOTES_BASIC  = [['E',''],['F',''],['G',''],['A',''],['B',''],['C',''],['D',''],['E','O'],['F','']]
BASSNOTES_BASIC    = [['G',''],['A',''],['B',''],['C',''],['D',''],['E',''],['F',''],['G',''],['A','']]
TREBLENOTES_ADV = [['C',''],['D',''],['E',''],['F',''],['G',''],['A',''],['B',''],['C',''],['D',''],['E',''],['F',''],['G',''],['A','']]
BASSNOTES_ADV   = [['E',''],['F',''],['G',''],['A',''],['B',''],['C',''],['D',''],['E',''],['F',''],['G',''],['A',''],['B',''],['C','']]
    

def validation(note_position):
    
    while True:
        for x,y in note_position:
            if y != '':
                if x!=y:
                    raise Exception('Validation Error') 
        break