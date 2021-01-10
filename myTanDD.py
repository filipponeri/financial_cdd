import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
from time import time


class myTanDD:
    def __init__(self, WindowSize = 40):
       self.WindowSize = WindowSize
       self.changed_MarketType = 0
       self.previousMarketType = ''
       self.x = np.array(range(0, WindowSize))
       self.y = []
       self.intercept = 0
       self.coeff = 0
       self.angle = 0
       
    def add_element(self, element):
        size_y = len(self.y)
        if (size_y == self.WindowSize):
            self.y = self.y[1:size_y]
            
        self.y = np.append(self.y, element)
        if (size_y == self.WindowSize):
            self.model = LinearRegression()
            self.model.fit(self.x.reshape(-1, 1), self.y)
            self.coeff = self.model.coef_
            self.intercept = self.model.intercept_
            #print('intercept:', self.intercept)
            #print('slope:', self.coeff)
            r2d = 180/np.pi
            self.angle = np.arctan(self.coeff)*r2d
            #print('angle: ', self.angle)
            #print(self.y)
            
            angle_level = 6  #degree wrt x axis
            if (self.angle > angle_level and self.angle >= 0): 
                #print('Bull')
                self.marketType = 'Bull'
            if (self.angle < 0 and self.angle <= -angle_level ):
                #print ('Bear')
                self.marketType = 'Bear'
            if (self.angle > -angle_level and self.angle < 0 ) or  \
                  (self.angle <= angle_level and self.angle >= 0):
                    #print('Stagnant')
                    self.marketType = 'Flat' #Stagnant

            if (self.previousMarketType != self.marketType):
                self.previousMarketType = self.marketType
                self.changed_MarketType = 1 
        return
        
 

    def detected_change(self):
        result = False 
        if self.changed_MarketType == 1:
            result = True
        else:
            result = False
        return(result)   
    
    def detected_warning_zone(self):
        return (False)

    def reset(self):
        self.y = []  
        self.changed_MarketType = 0   
   
    def get_x_y(self):
        return self.x, self.y

    def lr_params(self):
        return self.intercept, self.coeff, self.angle, self.marketType

 