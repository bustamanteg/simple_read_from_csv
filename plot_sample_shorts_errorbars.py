# 


import numpy as np
import matplotlib.pyplot as plt

dir='/data/20230228_run18/short_circuit_sample'
file='data_I_V.csv'

dir_file=dir+'/'+file

data = np.genfromtxt(dir_file, delimiter=',',comments='#',skip_header=1)

print(data)

Vs=data[:,0]
Vr=data[:,1]
Ir=data[:,2]*1e-6 # uA
I_g=data[:,3]*1e-6 # uA
I_ng=data[:,4]*1e-6 # uA


R_shunt=109.9*1e3 #kOhm measured with the multimeter
dR_shunt=0.1*1e3 # smallest difference in multimeter 


fig1=plt.figure(1)
fig1.set_figheight(7)
fig1.set_figwidth(9)

#-------------------uncertainties
dVs=0.001*np.ones(len(Vs))
dVr=0.001*np.ones(len(Vr))
dI_g=0.2e-6*np.ones(len(I_g))
dI_ng=0.2e-6*np.ones(len(I_ng))

#for i in range()
# Ir=Vr/R_shunt
dIr=np.abs(Ir)*np.sqrt((dVr/Vr)**2+(dR_shunt/R_shunt)**2)


#-------------------


ax0=fig1.add_subplot(1,1,1)
#ax0.plot(Vs,Vr,label='Vr [V]')
ax0.errorbar(Vs,Ir,xerr=dVs,yerr=dIr,fmt='.',label='Ir=Vr/R')#,'o',label='Ir=Vr/R')
ax0.errorbar(Vs,I_g,xerr=dVs,yerr=dI_g,fmt='.',label='I, shunt resistor connected to ground')
ax0.errorbar(Vs,I_ng,xerr=dVs,yerr=dI_ng,fmt='.',label='I, all sample connections together')
ax0.set_title('Current on sample under various conditions')
ax0.set_xlabel('Vs [V]')
ax0.set_ylabel('I [A]')
ax0.legend()



#plt.show()

fig2=plt.figure(2)
fig2.set_figheight(7)
fig2.set_figwidth(9)

ax1=fig2.add_subplot(1,1,1)
ax1.plot(Vs,Vr,'ob',label='Vr')
ax1.set_xlabel('Vsample [V]')
ax1.set_ylabel('V resistor [V]')
ax1.set_title('Voltage on shunt resistor as a function of Voltage on sample')


fig1.savefig(dir+'/'+'IvsVs_fig1.png')
fig2.savefig(dir+'/'+'VrvsVs_fig2.png')
plt.show()
