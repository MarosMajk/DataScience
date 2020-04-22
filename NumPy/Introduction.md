# Numpy


NumPy reprezentuje jeden zo základných (fundamentálnych) stavebných kameňov datascience. Jedná sa o knižnicu jazyka Python ktorá/ rozširuje funkcie klasického listu.

Využíva sa najmä kvôli

N-dimenzionálnym maticiam ktoré vytvára ako objekty
sofistikovaných (breadcasting) funkcií
nástrojom ktoré umožnujú integráciu kódu C/C++ a Fortrain
funkciám pre lineárnu algebru, Fourier-ové transformácie a mnoho dalších


Prečo používať Numpy namiesto vstavaného Listu?

Hlavným dôvodom použitia packpage Numpy je jeho rýchlosť, oproti Listu ktorý je pomalý.




## 1. Python ako dynamický typový jazyk
Dynamický programovací jazyk popisuje triedu vyšších programovacích jazykov, ktorý "za behu" vykonávajú množstvo operácií, interpretér jazyka nevie typ premennej ktorá je definovaná. Rozdiel medzi premennou v kompilovanom jazyku a premennou v Pythone je znázornená nižšie.

![image](images/cint_vs_pyint.png)

Pre premennú v C kompilátor pozná typ podľa jeho samotnej definície. Čo sa týka premennej v Pythone, všetko, čo viete v čase spustenia programu, je to, že ide o nejaký druh objektu Python.

Takže ak v jazyku C máme nasledovné

```
int a = 1;
int b = 3;
int c = a + b;
```
Kompilátor jazyka C vie už od začiatku že sa premenné <b>a</b> a <b>b</b> sú integer, s touto "znalosťou" alebo teda informáciou kompilátor zavolá funkciu "routine" ktorá pridá týmto dvom premenných  






