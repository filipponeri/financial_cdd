import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression

class MINPS:
    def __init__(self, WindowSize=40):
        self.WindowSize = WindowSize
        self.min_std = -1
        self.mean = -1
        self.ts = []
        self.change_detected = 0
        self.warning_detected = 0

    def detected_change(self):
        result = False   
        if self.change_detected == 1:
            result = True
        else:
            result = False
        return(result)   
    
    def detected_warning_zone(self):
        result = False       
        if self.warning_detected == 1:   
            result = True
        else:
            result = False
        return(result)  
   
    def add_element(self, element):
        if self.detected_change(): 
            self.reset()        
        size_ts = len(self.ts)
        if (size_ts < self.WindowSize):
            self.ts = np.append(self.ts, element)
            curr_mean = self.ts.mean()
            curr_std = self.ts.std()
            self.mean = curr_mean
            self.min_std = curr_std 

        if (size_ts == self.WindowSize):
            self.ts = np.append(self.ts[1:size_ts], element)
     
            # warning detection
            error = abs(self.mean - element)
            bound = 2 * self.min_std
            if error > bound: 
                self.warning_detected = 1

            # change detection
            error = abs(self.mean - element)
            bound = 3 * self.min_std
            if error > bound: 
                self.change_detected = 1
      
            curr_mean = self.ts.mean()
            curr_std = self.ts.std()
                 
            # # update mean
            #if (curr_mean < self.mean or self.mean == -1):
            #    self.mean = curr_mean
            
            # update std
            if (curr_std < self.min_std or self.min_std == -1):
                self.min_std = curr_std  

            #print('input ', element)
            #print('mean', self.mean )    
            #print('lower bound', self.mean - bound)    
            #print('higher bound', self.mean + bound)
            #print()    

    
    def reset(self):
        self.ts = []
        self.min_std = -1
        self.mean = -1
        self.change_detected = 0
        self.warning_detected = 0
      
        