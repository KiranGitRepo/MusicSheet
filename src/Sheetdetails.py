#!/usr/bin/env python
# coding: utf-8

"""
Created on Sun Sep 26 12:06:35 2021
@author: kiran
Version: 0.1
This script contains display functions for each note type
"""

from Notes import TREBLENOTES_BASIC,BASSNOTES_BASIC,TREBLENOTES_ADV,BASSNOTES_ADV


def TrebleClefBasic(x,y):
    notes=TREBLENOTES_BASIC
    print("\n")
    print("------------------------------------------------------------"+notes[x+7][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+6][y])
    print("------------------------------------------------"+notes[x+5][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+4][y]+"\t\t")
    print("------------------------------------"+notes[x+3][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+2][y]+"\t\t\t")
    print("------------------------"+notes[x+1][y]+"--------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("------------"+notes[x-1][y]+"--------------------------------------------------------")
    print("\n")


def BassClefBasic(x,y):
    notes=BASSNOTES_BASIC
    print("\n")
    print("------------------------------------------------------------"+notes[x+7][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+6][y])
    print("------------------------------------------------"+notes[x+5][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+4][y]+"\t\t")
    print("------------------------------------"+notes[x+3][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+2][y]+"\t\t\t")
    print("------------------------"+notes[x+1][y]+"--------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("------------"+notes[x-1][y]+"--------------------------------------------------------")
    print("\n")

     
def TrebleClefAdv(x,y):
    notes=TREBLENOTES_ADV
    print("\n")
    print("                                                              -----"+notes[x+11][y]+"----")
    print("\t\t\t\t\t\t\t \t"+notes[x+10][y])
    print("------------------------------------------------------------"+notes[x+9][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+8][y])
    print("------------------------------------------------"+notes[x+7][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+6][y]+"\t\t")
    print("------------------------------------"+notes[x+5][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+4][y]+"\t\t\t")
    print("------------------------"+notes[x+3][y]+"--------------------------------------------")
    print("\t\t  "+notes[x+2][y]+"\t\t\t")
    print("------------"+notes[x+1][y]+"--------------------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("                  ------"+notes[x-1][y]+"-------                  ")
    print("\n")
    
    
def BassClefAdv(x,y):
    notes=BASSNOTES_ADV
    print("\n")
    print("                                                              -----"+notes[x+11][y]+"----")
    print("\t\t\t\t\t\t\t \t"+notes[x+10][y])
    print("------------------------------------------------------------"+notes[x+9][y]+"--------")
    print("\t\t\t\t\t\t      "+notes[x+8][y])
    print("------------------------------------------------"+notes[x+7][y]+"--------------------")
    print("\t\t\t\t\t  "+notes[x+6][y]+"\t\t")
    print("------------------------------------"+notes[x+5][y]+"--------------------------------")
    print("\t\t\t      "+notes[x+4][y]+"\t\t\t")
    print("------------------------"+notes[x+3][y]+"--------------------------------------------")
    print("\t\t  "+notes[x+2][y]+"\t\t\t")
    print("------------"+notes[x+1][y]+"--------------------------------------------------------")
    print("\t\t  "+notes[x][y]+"\t\t\t")
    print("                  ------"+notes[x-1][y]+"-------                  ")
    print("\n")