#!/usr/bin/env python
# coding: utf-8

# In[5]:

import Play_in_loop
from Var_n_Val import TREBLENOTES_BASIC,TREBLENOTES_ADV,BASSNOTES_BASIC,BASSNOTES_ADV
from Sheetdetails import TrebleClefBasic,TrebleClefAdv,BassClefBasic,BassClefAdv

class MusicSheetPractice:
    
    def ClefDifficultyInput(num=2,var='Clef'):
        
        global variable, numchoice
        
        variable=var

        while True:
            
            try:
                numchoice=int(input("Please enter your choice here : "))

                if numchoice > 0 and numchoice <= int(num):
                    break
                else:
                    print(f"Please enter your choice as integer and in between 0 and {num}")
            except:
                print("Please enter your choice as integer")

    print("\nTreble Clef Training : 1\nBass Clef Traning : 2\n")
    ClefDifficultyInput(2,'Clef')
    print("Your Choice for {} is {}\n".format(variable,str(numchoice)))

    clef_choice=numchoice

    print("\nBeginer mode : 1\nIntermediate mode: 2\nAdvanced mode:3")
    ClefDifficultyInput(3,'difficulty')
    print("Your Choice for {} is {}\n".format(variable,str(numchoice)))

    difficulty=numchoice

    if clef_choice == 1:

        if difficulty==1:

            Play_in_loop(TREBLENOTES_BASIC,TrebleClefBasic,4)

        elif difficulty==2:

            Play_in_loop(TREBLENOTES_BASIC,TrebleClefBasic,6,2)
        else:

            Play_in_loop(TREBLENOTES_ADV,TrebleClefAdv,11,4)

    else:

        if difficulty==1:

            Play_in_loop(BASSNOTES_BASIC,BassClefBasic,4)

        elif difficulty==2:

            Play_in_loop(BASSNOTES_BASIC,BassClefBasic,6,2)
        else:

            Play_in_loop(BASSNOTES_ADV,BassClefAdv,11,4)


if __name__=='__main__':

    #from Play_in_loop import *

    MusicSheetPractice()

