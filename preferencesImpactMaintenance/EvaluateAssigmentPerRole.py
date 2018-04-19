#!/usr/bin/python3
from timeit import default_timer as timer
import datetime        
import shutil
import time
import sys
import numpy as np
import math
import copy
from math import sqrt
import psutil as ps
import itertools
import os
import SatFormulaInjectorMaxSat as sfi
import timeit 
from timeit import default_timer as timer



############################SMALLCOMP180############################################
#dataset="SmallComp180"
#nExcs = 12
#inputFolder= "/home/marcomori/OnlineRBACTuning/Exp_CCEHC_LS_1Step_Compare_0404_180sec/OutputMaxSat/"
#inputTotSoft = "/home/marcomori/OnlineRBACTuning/SOFTDASODDISFARE_SmallComp/Results/softclauses.txt"
#inputSatSoft = "/home/marcomori/OnlineRBACTuning/Exp_CCEHC_LS_1Step_Compare_0404_180sec/OutputMaxSat/"



############################SMALLCOMP180############################################
#dataset="Domino180"
#nExcs = 19
#inputFolder= "/home/marcomori/OnlineRBACTuning/Exp_CCEHC_LS_TimeOut_CPUTime_2609_Domino180s/OutputMaxSat/"
#inputTotSoft = "/home/marcomori/OnlineRBACTuning/SOFTDASODDISFARE_Domino/Results/softclauses.txt"
#inputSatSoft = "/home/marcomori/OnlineRBACTuning/Exp_CCEHC_LS_TimeOut_CPUTime_2609_Domino180s/OutputMaxSat/"



############################University360############################################
dataset="University360"
nExcs = 10
inputFolder= "/home/marcomori/OnlineRBACTuning/Exp_CCEHC_LS_TimeOut_CPUTime_2609_University360s/OutputMaxSat/"
inputTotSoft = "/home/marcomori/OnlineRBACTuning/SOFTDASODDISFARE_University/Results/softclauses.txt"
inputSatSoft = "/home/marcomori/OnlineRBACTuning/Exp_CCEHC_LS_TimeOut_CPUTime_2609_University360s/OutputMaxSat/"



outputFile = "/home/marcomori/OnlineRBACTuning/ExpResults/C/Results/"

b_weights=np.array([0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1])


if not os.path.exists(outputFile): 
    os.makedirs(outputFile)


with open(outputFile+str(dataset)+"_numeExc"+str(nExcs)+".txt", "w") as outRes:
    outRes.write("b\taverageAssignmentsPerRole\tAverageSatisfaction\n") 


for b in b_weights:
    
    avgAss=0
    totAssPerRole=0
    
    avgRateSatisfation=0
    totalRate =0
    
    for indexE in range(0,nExcs):
        
        #Calcolo Rate
        totSoft = 0
        satisfied = 0
        rateSat = 0 
        #Totale soft per quell'eccezione e per quel b
        
        with open(inputTotSoft) as inputSoftClauses:
           
            for line in inputSoftClauses: 
                if (line.startswith(str(b)+"_"+str(indexE))):
                    totSoft = int(line[line.index('*')+1:])
                    print("totSoft="+str(totSoft))
                    break
            if (totSoft==0):
                print("ERORR")
                sys.exit(0)
        
        with open(inputSatSoft+"exc_"+str(indexE)+"_w_"+str(b)+"_MaxSatout.txt") as inputSatisfied:    
            
            for line in inputSatisfied: 
                if (line.startswith("c optUnsatWeightsTotal = ")):
                    satisfied = int(line[25:])
                    print("satisfied="+str(satisfied))
                    break     
            if (satisfied==0):
                print("ERORR")
                sys.exit(0)
                
        rateSat  = (float(totSoft)-float(satisfied))*100 / float(totSoft)
        
        totalRate = totalRate + rateSat
        
        
        
        #Calcolo la media assegnazioni per ruolo
        print(indexE)
        labelUA = inputFolder+ "exc_"+str(indexE)+"_w_"+str(b)+"_MaxSatout_UR.csv"
        labelPA = inputFolder+ "exc_"+str(indexE)+"_w_"+str(b)+"_MaxSatout_RP.csv"
        
        UA = np.genfromtxt(labelUA, delimiter=',') 
        PA = np.genfromtxt(labelPA, delimiter=',') 
        
        #UA = sfi.loadMatrix(labelUA)
        #PA = sfi.loadMatrix(labelPA)
        
        #print(UA)
        #print(PA)
        
        UA, PA = sfi.deleteZeroRoles(UA,PA) 
    
        ass=0
        ruoli = PA.shape[0]
        assPerRole = 0
        
        print(ruoli)
        print(PA.shape[1])
        for indexRow in range(0,PA.shape[0]):
            for indexCol in range(0,PA.shape[1]):
                if (PA[indexRow][indexCol]==1):
                    ass=ass+1
            for indiceAssegnazione in range(0,UA.shape[0]):
                if (UA[indiceAssegnazione][indexRow]==1):
                    ass=ass+1
        
        
        assPerRole= float(ass) /float(ruoli)
        
        totAssPerRole = float(totAssPerRole) + assPerRole
        
        
    avgAss = float(totAssPerRole) / float(nExcs)
     
    avgRateSatisfation = float(totalRate) / float(nExcs)    
        
    with open(outputFile+str(dataset)+"_numeExc"+str(nExcs)+".txt", "a") as outF:
        outF.write(str(b)+"\t"+str(avgAss)+"\t"+str(avgRateSatisfation)+"\n")         
    
    
    