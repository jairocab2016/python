#!/usr/bin/env python
# -*-coding:utf-8-*-

import time

from time import sleep

import random


sus= "-" * 35
depo=["piedra","papel","tijera"]

while True:
    x= row_input("Que elijes? piedra, papel, tijera: ")
    if x not in depo:
        print ("No hagas Trampa!!!")
        continue

    pc=random.choice(depo)
    sleep(0.5)
    print (("computadora elijio{}.".format(pc)))


