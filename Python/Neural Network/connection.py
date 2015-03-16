from neuron import Neuron
from neurons import *
from abc import ABCMeta, abstractproperty, abstractmethod
import random

class Connection(object): 
    __metaclass__ = ABCMeta
    stepMin = 0.0000016
    stepMax = 50
    stepInitial = 0.1
    stepIncrease = 1.2
    stepDecrease = 0.5 
    def __init__(self, anteriorNeuron, posteriorNeuron, weightInitial=None):
        if(weightInitial == None):
            self.nudgeWeight()
        else:
            self.weight=weightInitial
        self.anterior = anteriorNeuron
        self.posterior = posteriorNeuron
        self.gradient = 0
        self.finalizedGradient = 0
        self.network
    #I skipped over guassian randomness because I'm a lazy asshole
    def nudgeWeight(self):
        self.weight=random.random()*2-1
    def feedForward(self):
        self.posterior.net += self.anterior*self.weight
    #learning parameters is a list of doubles
    @abstractproperty
    def learningParameterCount(self):
        pass
    def tryUpdateWeight(self, learningParameters):
        if(self.learningParameterCount() > 0):
            if(not(learningParameters != None and len(learningParameters)>= self.learningParameterCount())):
                raise AttributeError("Missing or uneven learning parameters")
        self.updateWeight(learningParameters)
    #learning parameters is a list of doubles
    @abstractmethod
    def updateWeight(self, learningParameters):
        pass
    def updateGradient(self):
        self.gradient += self.posterior.error*self.anterior.output
    def finalizedGradient(self):
        self.finalizedGradient = self.gradient
        self.gradient = 0
    def getGradient(self):
        return self.finalizedGradient 