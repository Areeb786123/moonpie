# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:12:32 2020

@author: Legedith
"""
from time import sleep
import os


def launch():
    rocket = ['                                                                                ',
     '                                                                                ',
     '                                      ((//.                                     ',
     '                                    ((((////                                    ',
     '                                  ((((((//////                                  ',
     '                                 (((((((///////.                                ',
     '                               ,@@@@@@@@@&&&&&&&#                               ',
     '                              #@@@@@@@((/(&&&&&&&*                              ',
     '                              @@@@@(....... /&&&&&                              ',
     '                             @@@@@(........../&&&@&                             ',
     '                            #@@@@&(/........,/&&&&&,                            ',
     '                            @@@@@@&@((....//&#&&&&&&                            ',
     '                            @@@@@@@@@@%&%#@&&&&&&&&&,                           ',
     '                           (@@@@@@@@@@@@&&&&&&&&&&&&                            ',
     '                           .@@@@@@@@@@@@&&&&&&&&&&&&,                           ',
     '                           .@@@@@@@@@@@@&&&&&&&&&&&&,                           ',
     '                           (@@@@@@@@@@@@&&&&&&&&&&&&                            ',
     '                           .@@@@@@@@@@@@&&&&&&&&&&&&&#                          ',
     '                          @@@@@@@@@@@@@@&&&&&&&&&&&&&&&                         ',
     '                        @@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&#                       ',
     '                      (@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&                      ',
     '                     ,@@@@@@&@@@@@@@@@@@&&&@@@&&&&&&%&&&&&&                     ',
     '                     ,@@@@@%(//(((((((((/////////////&&&%&&*                    ',
     '                     ,@(((((((   ..............    (//////&                     ',
     '                      (((         *..........           ///                     ',
     '                                  *###&&&&&###                                  ',
     '                                  ###@@@@@@@##/                                 ',
     '                                  ####@@@@@####                                 ',
     '                                  *###########/                                 ',
     '                                    #########                                   ',
     '                                      ####.                                     ',
     '                                                                                ',
     '']
    os.system('git push -u origin master')
    for i in rocket:
        print()
        print(i)
        sleep(0.2)


def choice():
    os.system('figlet -c Mission Control')
    print("     1. Set destination (upstream)")
    print("     2. Set Mission Statement (commit message")
    print("     3. Launch! (push code to GitHub)")    
    print()
    cmd = int(input("     Astronaut's choice: "))

    if cmd == 1:
        destination()
    elif cmd == 2:
        commit()
    elif cmd == 3:
        launch()
    else:
        print("You entered a worng command!")
    
def commit():
    print()
    msg = input('     Enter mission statement: ')
    os.system('git add .')
    os.system('git commit -m "'+msg+'"')
    os.system('figlet -c Mission Statement Added')

def destination():
    print()
    msg = input('     Enter Destination: ')
    os.system('git remote add origin '+msg)
    #git remote add origin https://github.com/Legedith/moonpie.git
    os.system('figlet -c Destination Added')
choice()