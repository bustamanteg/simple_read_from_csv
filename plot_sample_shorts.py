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
Ir=data[:,2]
I_g=data[:,3]
I_ng=data[:,4]


fig1=plt.figure(1)
fig1.set_figheight(7)
fig1.set_figwidth(9)

ax0=fig1.add_subplot(1,1,1)
#ax0.plot(Vs,Vr,label='Vr [V]')
ax0.plot(Vs,Ir,'o',label='Ir=Vr/R')
ax0.plot(Vs,I_g,'o',label='I, shunt resistor connected to ground')
ax0.plot(Vs,I_ng,'o',label='I, all sample connections together')
ax0.set_title('Current on sample under various conditions')
ax0.set_xlabel('Vs [V]')
ax0.set_ylabel('I [uA]')
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
