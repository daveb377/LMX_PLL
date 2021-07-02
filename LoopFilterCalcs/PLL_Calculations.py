# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:21:32 2021

@author: Dave
Working through Dean Banerjee's PLL book to calculate the 
loop filter and performance parameters of a PLL based on the LMX2332
2021-06-26 Installed icecream to make debugging easier
"""
import math
from icecream import ic

# Constants

Fref=16.8e6
ChannelSpacing=25e3
Fmin = 380e6
NChannels = 2401


# VCO
VCOMin = 370e6
VCOMax = 460e6
VTuneMin = 0.5
VTuneMax = 4.5

# PLL Consts
Kpd = 1e-3 # in A
LoopBW = 10e3
Gamma = 1.024
PMDeg=49.2


# Start Calculations. 

Nmin = Fmin/ChannelSpacing
Nmax = Nmin + NChannels
Ndesign=math.sqrt(Nmin*Nmax)

Kvco = (VCOMax-VCOMin)/(VTuneMax-VTuneMin)
ic(Nmin)
ic (Nmax)
ic(Ndesign)


wc = LoopBW * 2 * math.pi
PMRad=math.radians(PMDeg)

ic(wc)
ic(PMRad)


# Calculate Poles and Zeros
#38.16
T1P1= (1+Gamma)*math.tan(math.radians(PMDeg))
T1P2 = math.sqrt(((1+Gamma)**2)*(math.tan(math.radians(PMDeg))**2)+4*Gamma)
T1 =(T1P2-T1P1)/(2*wc)
# Eq 38.17
T2 = Gamma/((wc**2)*T1)

# Eq 38.8
A0P1 = ((Kpd*Kvco)/(Ndesign*(wc**2)))*math.sqrt((1+(wc*T2)**2)/(1+(wc*T1)**2))




