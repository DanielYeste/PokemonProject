import os

import pandas as pd
import sys

import model
from tkinter import *
from tkinter import ttk




if __name__ == '__main__':
    root = Tk()
    root.title("Pokemon database")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


    '''abilities
    
    # Pidgey sera una row solo, hayq ue sacar sus columnas type1 y type2
    # type1 #type2 #name
against_bug
against_dark
against_dragon
against_electric
against_fairy
against_fight
against_fire
against_flying
against_ghost
against_grass
against_ground
against_ice
against_normal
against_poison
against_psychic
against_rock
against_steel
against_water
attack
base_egg_steps
base_happiness
base_total
capture_rate
classfication
defense
experience_growth
height_m
hp
japanese_name
name
percentage_male
pokedex_number
sp_attack
sp_defense
speed

weight_kg
generation
is_legendary

'''
