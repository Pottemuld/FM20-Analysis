#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

attribute_view = pd.read_html('file:///C:/Users/Pottemuld/Documents/Sports%20Interactive/Football%20Manager%202020/html/attributes_view.html')

# Most important stats are divided by 20
df = attribute_view[0]

#TODO add less important stats to calc.
# Calculate dna scores
df['Team_dna'] = (df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta'])

# Sweeper Keeper - Attack
df['sk_at'] = (df['Aer'] + df['Com'] + df['Fir'] + df['Han'] + df['Pas'] + df['Ref'] + df['TRO'] + df['Thr'] + df['Cmp'] + df['Dec'] + df['Vis'] + df['Acc'])

# Fullback - Support
df['fb_su'] = (df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Pac'] + df['Sta'] + df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'] + df['Wor'])

# Ballplaying Defender - Defend
df['bpd_def'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

# Inverted Wingback - Support
df['iwb_su'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

# Winger - Support
df['win_su'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

# Box-To-Box - Support
df['btb_su'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

# Deep-Lying Playmaker - Support
df['dlp_su'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

# Target Man - Support
df['tm_su'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

# Advanced Forward - Attack
df['af_at'] = ((df['Agg'] + df['Ant'] + df['Det'] + df['Tea'] + df['Wor'] + df['Acc'] + df['Sta']) / 140) * 100

print(df)





