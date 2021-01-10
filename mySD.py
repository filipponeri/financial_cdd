import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

class mySDDD:
    def __init__(self, WindowSize = 40):
       self.WindowSize = WindowSize
       self.y = []
       self.minSD = 0
       self.det_change = 0
       self.det_warning = 0     

    def add_element(self, element):
        size_y = len(self.y)
        if (size_y == self.WindowSize):
            self.y = self.y[1:size_y]
        self.y = np.append(self.y, element)
        if (size_y == self.WindowSize):
            currSD = self.y.std()
            if currSD < self.minSD or self.minSD == 0:
                self.minSD = currSD
            warning_bound = self.minSD *2    
            if currSD > warning_bound:
                self.det_warning = 1     
            change_bound = self.minSD *3    
            if currSD > change_bound:
                self.det_change = 1     
 
    def detected_change(self):
        result = False 
        if self.det_change == 1:
            result = True
        else:
            result = False
        return(result)   
    
    def detected_warning_zone(self):
        result = False
        if self.det_warning == 1:
            result = True
        return (result)

    def reset(self):
        self.y = []  
        self.minSD = 0
        self.det_change = 0 
        self.det_warning = 0  
   
 