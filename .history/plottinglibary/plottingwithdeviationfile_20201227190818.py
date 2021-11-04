import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.patches as mpatches
import copy
import sys
import buildupfunctions



def plottingwithdeviation(Datasets):
    numberofdatasets = len(Datasets)

    nameofplot = input("What is the name of the plot! ")
    storagelocation = input("What is the location of the storage? ")
    xlabel = input("What is the label for the x axis? ")
    ylabel = input("What is the label for the y axis? ")
    titleofplot = input("What is the title of the plot? ") 
    startindex = int(input("What is the starting index of the functions you want to plot: "))
    endindex = int(input("what is the end index of functions U use? ")) # exklusiv

    plt.cla()
    plt.figure(figsize=(12,6)) # function to scale the plot how you want it
    #plt.axis([0, 35, 0.01, 0.05]) # manually scale the plotting
    plt.title(titleoftheplot)
    plt.grid(linewidth = "1", b=True, which='both', alpha=1)
    plt.xlabel(xl)
    plt.ylabel(yl, rotation=90) 

    j = 0
    while j < numberofdatasets:
            i = int(startindex)
            k = int(endindex)
            labelname = input("How do you want to label the dataset? ")
            while i < k :#numberofdifferentindicies
                ThreadDummy = Datasets[j]._Thread[i:(i+ 1)]
                TimeDummy = Datasets[j]._PlottingTime[i:(i + 1)]
                DeviationDummy = Datasets[j]._PlottingDeviation[i:(i+ 1)]
                Deviation2Dummy = DeviationDummy[0]
                Time2Dummy = TimeDummy[0]
                Thread2Dummy = ThreadDummy[0]
                plt.errorbar(Thread2Dummy, Time2Dummy, Deviation2Dummy, linestyle='None', fmt='o',  label = labelname)
                i += 1
            j += 1
    
    plt.legend(loc='upper right')#, handles = [Median_Plot, Deviations_Plot])
    plt.savefig( storagelocation + '.pdf' )