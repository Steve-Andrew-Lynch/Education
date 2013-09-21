# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

from ps8b_precompiled_26 import *
from ps8b_precompiled_27 import * 

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
 
    timeSteps150 = 150
    timeSteps300 = 300
    timeSteps75 = 75
    timeSteps0 = 0
    #300, 150, 75, and 0
    

    def runSimAndPlot(timeStepsVar, numTrials):
        """Runs the simluation for a given number of trials. Returns the trial results for a given timestep combination"""
        viruses = []
        for nv in range(100):
            viruses.append(ResistantVirus( 0.1, 0.05, {'guttagonol': False}, 0.005))

        totalOutcomes = []
        
        for nt in range(numTrials):
            patient = TreatedPatient(viruses[:], 1000)

            for ts in range(timeStepsVar):
                patient.update()
            
            patient.addPrescription('guttagonol')
        
            for ts in range(timeSteps150):
                patient.update()

            totalOutcomes.append(patient.getTotalPop())
    
        return totalOutcomes

    hist300 = runSimAndPlot(timeSteps300, numTrials)
    print '300 done!'
    hist150 = runSimAndPlot(timeSteps150, numTrials)
    print '150 done!'
    hist75 = runSimAndPlot(timeSteps75, numTrials)
    print '75 done!'
    hist0 = runSimAndPlot(timeSteps0, numTrials)
    print '0 done!'

    pylab.figure(1)
    pylab.hist(hist300, 100)
    pylab.figure(2)
    pylab.hist(hist150, 100)
    pylab.figure(3)
    pylab.hist(hist75, 100)
    pylab.figure(4)
    pylab.hist(hist0, 100)
    pylab.show()


simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
