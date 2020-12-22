#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from scipy.interpolate import interp1d
from pandasgui import show
import numpy as np

pd.set_option('display.max_columns', 100)
pd.set_option('precision', 3)
file = ''

def choose_file():
    global file
    i = input("Please choose an option below: \n"
              "1: Own Team \n"
              "2: Shortlist \n")
    if (i == '1'):
        file = './own_team.html'
    elif (i == '2'):
        file = './shortlist.html'
    return file

file = choose_file()
attribute_view = pd.read_html(file)

map = interp1d([0, 7000], [0, 100])

df = attribute_view[0]

df = df.replace('-', 0)

with open('my_file.html', 'w') as fo:
    fo.write(df.to_html())

attribute_view = pd.read_html('my_file.html')

df = attribute_view[0]

df['Team_dna'] = (df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta'])

df['sk_at'] = map(((df['Aer'] + df['Com']) * 40))

# Sweeper Keeper - Attack
df['sk_at'] = map((df['Aer'] + df['Com'] + df['Fir'] + df['Han'] + df['Pas'] + df['Ref'] + df['TRO'] + df['Thr'] + df['Cmp'] + df['Dec'] + df['Vis'] + df['Acc']) * 40)

# Fullback - Support
df['fb_su'] = map((((df['Cro'] + df['Dri']) * 20) + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + ((df['Pac'] + df['Sta']) * 20) + (df['Mar'] + df['Tck'] * 40) + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'] + df['Wor']))

# Ballplaying Defender - Defend
df['bpd_def'] = map((((df['Mar'] + df['Tck'] + df['Pas'] + df['Jum']) * 40) + df['Fir'] + df['Cmp'] + df['Dec']))

# Inverted Wingback - Support
df['iwb_su'] = map((((df['Mar'] + df['Tck'] + df['Pas']) * 40) + df['Pos'] + df['Tec'] + df['Fir'] + df['Pac'] + df['Cro']))

# Winger - Support
df['win_su'] = map((((df['Cro'] + df['Dri'] + df['Fir'] + df['Tec'] + df['OtB'] + df['Acc'] + df['Pac']) * 40) + df['Sta']))

# Box-To-Box - Support
df['btb_su'] = map((((df['Pas'] + df['Tck'] + df['Tec'] + df['OtB'] + df['Wor'] + df['Tea'] + df['Dec']) * 40) + df['Lon'] + df['Fin']))

# Deep-Lying Playmaker - Support
df['dlp_su'] = map((((df['Pas'] + df['Fir'] + df['Tec'] + df['OtB'] + df['Vis'] + df['Tea'] + df['Dec'] + df['Cmp']) * 40) + df['Ant']))

# Target Man - Support
df['tm_su'] = map((((df['Hea'] + df['Fin'] + df['Fir'] + df['Bra'] + df['Cmp'] + df['OtB'] + df['Bal'] + df['Jum'] + df['Str']) * 40) + df['Dec']))

# Advanced Forward - Attack
df['af_at'] = map(((df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['Cmp'] + df['OtB'] + df['Acc'] + df['Dec'] + df['Pac']) * 40))

show(df, settings={'block': True})





