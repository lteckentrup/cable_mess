import parameters as p
from farq import FarquharC3
import numpy as np
import matplotlib.pyplot as plt

"""
Default values:
Jmax25 = p.Vcmax25 * 1.67
Tleaf = 25.
Cs = 400.
par = 1800.
dleaf = 1.5
"""

# Create array for temperature
Tleaf = np.arange(0,26,1)
Tleaf_K = Tleaf + 273.15

F = FarquharC3(peaked_Jmax=True, peaked_Vcmax=True, model_Q10=True,
               gs_model="medlyn")

An_x = np.zeros(len(Tleaf))
gsc_x = np.zeros(len(Tleaf))

## Calculate An and gsc for varying temperature
def photo(Cs_val, par_val, dleaf_val):
    for i in range(len(Tleaf_K)):
        (An, gsc) = F.photosynthesis(p, Cs=Cs_val, Tleaf=Tleaf_K[i],
                    Par=par_val, vpd=dleaf_val)
        An_x[i] = An
        gsc_x[i] = gsc     

## Create plot

fig = plt.figure(figsize=(20,10))
fig.subplots_adjust(hspace=0.1)
fig.subplots_adjust(wspace=0.2)
plt.rcParams['text.usetex'] = False
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Helvetica"
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['font.size'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

almost_black = '#262626'
# change the tick colors also to the almost black
plt.rcParams['ytick.color'] = almost_black
plt.rcParams['xtick.color'] = almost_black

# change the text colors also to the almost black
plt.rcParams['text.color'] = almost_black

# Change the default axis colors from black to a slightly lighter black,
# and a little thinner (0.5 instead of 1)
plt.rcParams['axes.edgecolor'] = almost_black
plt.rcParams['axes.labelcolor'] = almost_black

ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(242)
ax3 = fig.add_subplot(243)
ax4 = fig.add_subplot(244)
ax5 = fig.add_subplot(245)
ax6 = fig.add_subplot(246)
ax7 = fig.add_subplot(247)
ax8 = fig.add_subplot(248)

## vary CO2 concentration (Cs)
Cs = [0,200,400,600,800]

for i in Cs:
    photo(i,1800,1.5)
    ax1.plot(Tleaf, An_x, label="Cs="+str(i))
    ax5.plot(Tleaf, gsc_x, label="Cs="+str(i))

## vary photosynthetically active radiation (par)
par = [0,900,1800,2700,3600]

for i in par:
    photo(400,i,1.5)
    ax2.plot(Tleaf, An_x, label="par="+str(i))
    ax6.plot(Tleaf, gsc_x, label="par="+str(i))

## vary vapour pressure deficit (vpd)
vpd = [0,0.75,1.5,2.25,3]

for i in vpd:
    photo(400,1800,i)
    ax3.plot(Tleaf, An_x, label="vpd="+str(i))
    ax7.plot(Tleaf, gsc_x, label="vpd="+str(i))

## vary Vcmax-value
Vcmax = [0, 30, 60, 120]

for i in Vcmax:
    p.Vcmax25 = i
    photo(400,1800,1.5)
    ax4.plot(Tleaf, An_x, label="Vcmax="+str(i))
    ax8.plot(Tleaf, gsc_x, label="Vcmax="+str(i))

ax1.legend(numpoints=1, loc="best")
ax2.legend(numpoints=1, loc="best")
ax3.legend(numpoints=1, loc="best")
ax4.legend(numpoints=1, loc="best")
ax5.legend(numpoints=1, loc="best")
ax6.legend(numpoints=1, loc="best")
ax7.legend(numpoints=1, loc="best")
ax8.legend(numpoints=1, loc="best")

## only y-label for two left panels
ax1.set_ylabel("$A_{\mathrm{n}}$ ($\mathrm{\mu}$mol m$^{-2}$ s$^{-1}$)")
ax5.set_ylabel("$g_{\mathrm{sc}}$ ($\mathrm{\mu}$mol m$^{-2}$ s$^{-1}$)")

## only x-label for bottom panels
ax5.set_xlabel("Temperature [$^\circ$C]")
ax6.set_xlabel("Temperature [$^\circ$C]")
ax7.set_xlabel("Temperature [$^\circ$C]")
ax8.set_xlabel("Temperature [$^\circ$C]")