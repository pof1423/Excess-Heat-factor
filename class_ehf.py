import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import stat
import glob
import os
import time

class EHF_cal():
    def __init__(self,short_window=3, longterm_window=30, ehf_percentile=95, sever_percentile=85):
        self.short_window = short_window
        self.longterm_window = longterm_window
        self.ehf_percentile = ehf_percentile
        self.sever_percentile = sever_percentile
        
        
    def ehi_sig(self, short_window, ehf_percentile, data)-> pd.DataFrame:
        avg_mw_3 = data.rolling(window=short_window).mean()
        avg_mw_3 = pd.DataFrame({'avg_mw_3' : avg_mw_3})
        ehf_data = avg_mw_3.dropna()
        avg_percen = np.percentile(data, ehf_percentile)
        ehi_sig = ehf_data['avg_mw_3'] - avg_percen
        return ehi_sig
    
    def ehf_accl(self, short_window, ehf_percentile, longterm_window,data)-> pd.DataFrame:
        avg_mw_3 = data.rolling(window=short_window).mean()
        avg_mw_3 = pd.DataFrame({'avg_mw_3' : avg_mw_3})
        avg_mw_month = data.rolling(window=longterm_window).mean()
        avg_mw_month = pd.DataFrame({'avg_mw_month' : avg_mw_month})
        ehf_data = pd.concat([avg_mw_3, avg_mw_month], axis = 1)
        ehf_data = ehf_data.dropna()
        ehi_accl = ehf_data['avg_mw_3'] - ehf_data['avg_mw_month']
        ehi_accl = pd.DataFrame({'ehi_accl' : ehi_accl})
        return ehi_accl
    
        
        
    def EHF(self, short_window, ehf_percentile, longterm_window, data) -> pd.DataFrame:
    
        avg_mw_3 = data.rolling(window=short_window).mean()
        avg_mw_3 = pd.DataFrame({'avg_mw_3' : avg_mw_3})
        avg_mw_month = data.rolling(window=longterm_window).mean()
        avg_mw_month = pd.DataFrame({'avg_mw_month' : avg_mw_month})
        
        ehf_data = pd.concat([avg_mw_3, avg_mw_month], axis = 1)
        ehf_data = ehf_data.dropna()
        avg_percen = np.percentile(data, ehf_percentile)
        
        ehi_sig = ehf_data['avg_mw_3'] - avg_percen
        ehi_accl = ehf_data['avg_mw_3'] - ehf_data['avg_mw_month']
        
        
        ehf_1 = pd.DataFrame(columns={'ehf'})
        
        for i in range(len(ehf_data)):
            sig_ehi = ehi_sig.iloc[i:i+1].values[0]
            accl_ehi = ehi_accl.iloc[i:i+1].values[0]
            ef = max(0,sig_ehi) * max(1,accl_ehi)
            ehf_1 = ehf_1.append({'ehf': ef},ignore_index=True) 
            
        return ehf_1
    