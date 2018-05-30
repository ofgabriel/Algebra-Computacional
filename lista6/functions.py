from math import *
import sys
sys.path.append('../lista1/')
from DecomposicaoLU import resolveSystem
sys.path.append('../lista2/')
from mathMethods import multiMM, multiMS

def euler(funcDifX, deltaT, tI, funcTIResult, tF):
    NITER = 1 + (tF-tI)/deltaT
    if NITER != int(NITER):
        print 'Exception: supposed to be integer'
        sys.exit()
    NITER = int(NITER)

    funcResults = [None for i in range(NITER)]
    funcResults[0] = funcTIResult

    for i in range(1, NITER):
        t = tI + (i-1)*deltaT
        funcResults[i] = funcResults[i-1] + funcDifX(t, funcResults[i-1]) * deltaT
    return funcResults

def rungeKutta2(funcDifX, deltaT, tI, funcTIResult, tF):
    NITER = 1 + (tF-tI)/deltaT
    if NITER != int(NITER):
        print 'Exception: supposed to be integer'
        sys.exit()
    NITER = int(NITER)

    funcResults = [None for i in range(NITER)]
    funcResults[0] = funcTIResult

    for i in range(1, NITER):
        t = tI + (i-1)*deltaT
        K1 = funcDifX(t, funcResults[i-1])
        K2 = funcDifX(t + deltaT, funcResults[i-1] + deltaT*K1)
        funcResults[i] = funcResults[i-1] + (deltaT/2) * (K1 + K2)
    return funcResults

def rungeKutta4(funcDifX, deltaT, tI, funcTIResult, tF):
    NITER = 1 + (tF-tI)/deltaT
    if NITER != int(NITER):
        print 'Exception: supposed to be integer'
        sys.exit()
    NITER = int(NITER)

    funcResults = [None for i in range(NITER)]
    funcResults[0] = funcTIResult

    for i in range(1, NITER):
        t = tI + (i-1)*deltaT
        K1 = funcDifX(t, funcResults[i-1])
        K2 = funcDifX(t + deltaT/2, funcResults[i-1] + (deltaT/2)*K1)
        K3 = funcDifX(t + deltaT/2, funcResults[i-1] + (deltaT/2)*K2)
        K4 = funcDifX(t + deltaT, funcResults[i-1] + deltaT*K3)
        funcResults[i] = funcResults[i-1] + (deltaT/6) * (K1 + 2*K2 + 2*K3 + K4)
    return funcResults

def enum(**enums):
    return type('Enum', (), enums)

INTEGRAL_METHOD = enum(EULER=1, RUNGE_KUTTA_2=2, RUNGE_KUTTA_4='three')

def integral(method, funcDifX, deltaT, tI, funcTIResult, tF):
    if(method == INTEGRAL_METHOD.EULER):
        derivateResults = euler(funcDifX, deltaT, tI, funcTIResult, tF)
    elif(method == INTEGRAL_METHOD.RUNGE_KUTTA_2):
        derivateResults = rungeKutta2(funcDifX, deltaT, tI, funcTIResult, tF)
    elif(method == INTEGRAL_METHOD.RUNGE_KUTTA_4):
        derivateResults = rungeKutta4(funcDifX, deltaT, tI, funcTIResult, tF)

    print derivateResults
    return derivateResults[-1] - derivateResults[0]