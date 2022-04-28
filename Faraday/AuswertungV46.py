import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


x = np.linspace(-0.03,0.03 , 1000)
mhub = const.value('Bohr magneton') #das gelibete Borhsche Magneton zeigt wie man Scipy Constants benutzt
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
def relf(l,m):  #in Prozent
    return (np.absolute(l-m)/l)*100
def fitf(x,a,b):
	return a*x**2 + b
z , B = np.genfromtxt("Messdaten/Feldmessung.txt", unpack=True)
z=z-116 #Zentrum des Magfeldes 
z*=10**-3
B*=10**-3

#Fit
params , cov = curve_fit(fitf, z ,B)
params = correlated_values(params, cov)
a = params[0]
b = params[1]
print(a,b)
#Tabelle
#np.savetxt('BFeldtab.txt',np.column_stack([B,z]), delimiter=' & ',newline= r'\\'+'\n' )

plt.plot(z, B,'ro', label='Mag. Feldstärke')
plt.plot(x, fitf(x,noms(a),noms(b)), 'b-', label='Parabel')
plt.xlabel(r'$z \:/\: m$')
plt.ylabel(r'$B \:/\: T$')
plt.ylim(0,0.55)
plt.grid()
plt.legend(loc='best')
plt.show()
plt.savefig('BFeld.pdf')
#.
#.
#.