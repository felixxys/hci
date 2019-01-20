import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd
import scipy.stats as st

dane = pd.read_csv(r"sub1.csv", delimiter=',', engine='python')
sygnal1=dane['syg1']
sygnal5=dane['syg5']#cyfry

t = np.linspace (0, 38, 200*38)
plt.plot(t, sygnal1)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.title('sygnał')
plt.show()

#zaporowy i przepustowy
przefiltrowany1=ag.pasmowozaporowy(sygnal1, 200, 49, 51)
przefiltrowany2=ag.pasmowoprzepustowy(przefiltrowany1, 200, 1, 50)

#wykresy
plt.plot(t, przefiltrowany2, color = 'g')
plt.ylabel('Amplituda [-]')
plt.xlabel('Czas [s]')
plt.title("sygnał przefiltorwany - pasmowoprzepustowy i pasmowozaporowym")
plt.show()

#dekodowanie
lista=[]
cos=0
poprzednie = 0
for i in przefiltrowany2:
    if i>=0.1 and poprzednie<0.1:
        lista.append(dane['syg5'][cos])
    poprzednie = i
    cos+=1
print("Wymrugany kod to:", lista)
