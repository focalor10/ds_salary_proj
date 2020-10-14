# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:20:12 2020

@author: Nete
"""


import glassdoorscraper as gs
import pandas as pd

path="C:/Users/Nete/Documents/ds_salary_proj/chromedriver"
slp_time=8

df=gs.get_jobs('data scientist',15,False, path,slp_time,'buenos aires')