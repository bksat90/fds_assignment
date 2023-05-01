# -*- coding: utf-8 -*-
"""
Created on Mon May  1 11:49:24 2023

@author: bksat
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df_file = pd.read_csv('data0.csv')

df_file.head(5)

df_file.plot(type='hist')