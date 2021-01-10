Domain Specific Concept Drift Detectors for Predicting Financial Time Series


## Requirements 

- Python 3.6 or above

## Usage

from financial_cdd.mySD import mySDDD

from financial_cdd.myTanDD import myTanDD

from financial_cdd.minps import MINPS


my_tan_dd = myTanDD(20) # to instantiate the drift detector

mySD_dd = mySDDD(20)

my_minps = MINPS(20)


#example of call with the myTanDD drift detector

my_tan_dd.add_element(element) # adding data to the drift detector, usually the current accuracy or even the raw data from the financial time series

my_tan_dd.detected_warning_zone() #returns True if a warning point has been detected, possibly indicating the start of a drift

my_tan_dd.detected_change() #returns True if a detection point has been detected 


---------------
It is appreciated the citation of the author and the study.

Filippo Neri (2021). "Domain Specific Concept Drift Detectors for Predicting Financial Time Series", Preprint.
Available at: https://www.researchgate.net/publication/348371870_Domain_Specific_Concept_Drift_Detectors_for_Predicting_Financial_Time_Series

---------------

Code repository at https://github.com/filipponeri/financial_cdd  

Note it is developed by an academic researcher, thus it will be maintained with some delay...

---------------
    
Abstract
Concept drift detectors allow classifiers to maintain good classification accuracy on non-stationary data streams. Financial time series are an instance of non-stationary data streams whose concept drifts (market phases) are so important to affect investment decisions worldwide. This paper studies how concept drift detectors behave when applied to financial time series. General results are: a) concept drift detectors usually improve runtime over continuous learning, b) their computational cost is usually a fraction of the learning and prediction steps of even basic learners, c) it is important to study concept drift detectors in combination with the learning systems they will operate with, and d) concept drift detectors can be directly applied to the time series of raw financial data and not only to the model's accuracy one. Moreover, the study introduces three simple concept drift detectors, tailored to financial time series, and shows that they can be as effective as the most sophisticated ones in the state of the art when applied to financial time series. Impact Statement-The finance industry exploits machine learning for the analysis of financial data. Financial time series are affected by concept drifts: their most evident manifestations happen when a market rotates among its bear, bull or stag-nant/flat phases. The prompt detection of a new market phase could allows financial companies to timely retune the computational systems controlling their investment decisions. This study shows the ability of concept drift detectors to recognize market phases in several operating conditions and could impact on how the finance industry deploys learning systems. In particular, three simple concept drift detectors, tailored to financial time series, are introduced and it is shown that they can be as effective as those in the state of the art when applied to financial time series.
    
