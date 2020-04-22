# Numpy


NumPy reprezentuje jeden zo základných (fundamentálnych) stavebných kameňov datascience. Jedná sa o knižnicu jazyka Python ktorá rozširuje funkcie klasického listu a mnoho ďalšieho.

<b>Využíva sa najmä kvôli:</b>
- N-dimenzionálnym maticiam ktoré vytvára ako objekty
- sofistikovanýcm (breadcasting) funkciám
- nástrojom ktoré umožnujú integráciu kódu C/C++ a Fortrain
- funkciám pre lineárnu algebru, Fourier-ové transformácie a mnoho dalších


<u>Prečo používať Numpy namiesto vstavaného Listu?</u>
Hlavným dôvodom použitia balíka Numpy je jeho rýchlosť, naproti Listu ktorý je v porovnani s NumPyu pomalý.


## 1. Python ako dynamický typový jazyk
Dynamický programovací jazyk popisuje triedu vyšších programovacích jazykov, ktorý "za behu" vykonávajú množstvo operácií, interpretér jazyka nevie typ premennej ktorá je definovaná. Rozdiel medzi premennou v kompilovanom jazyku a premennou v Pythone je znázornená nižšie.

![image](images/cint_vs_pyint.png)

Pre premennú v jazyku C kompilátor pozná typ premennej podľa jej samotnej definície. Čo sa týka premennej v Pythone, všetko, čo viete v čase spustenia programu, je to, že ide o nejaký druh objektu Python.

Takže ak v jazyku C máme nasledovné

```
int a = 1;
int b = 3;
int c = a + b;
```
Kompilátor jazyka C vie už od začiatku že premenné <b>a</b> a <b>b</b> sú integer, s touto "znalosťou" alebo teda informáciou kompilátor zavolá funkciu "routine" ktorá pridá dva integer do pamäti a následne vráti další integer (c) čo reprezentuje len ďalšiu hodnotu v pamäti. Hrubá schéma takého to pridávania je znázornená nižššie:

### Priradzovanie v jazyku C
1. Priradenie ```<int> 1 ``` k premennej ```a```
2. Priradenie ```<int> 2 ``` k premennej ```b```
3. Volanie funkcie ```binary_add<int, int>(a,b)```
4. Priradzovanie výsledky do premennej C

Ekvivaletný kód takého to priradzovania by v Pythone vyzeral následovne:

```
a = 1
b = 3
c = a + b
```
V takomto priradzovaní/priradení interpretér vie len to že ```a```a ```b``` sú nejaké objekty, ale nevie o aký typ objektu sa jedná. Interpretér v takomto prípade musí zistiť ```PyObject_HEAD``` pre každú premennú a nájsť informáciu o tom o akú premennú sa jedná a až potom zavolá sumárnu funkciu ("routine") pre dva typy (a,b). Nakoniec musí vytvoriť a inicializovať nový objekt ktorý bude obsahovať návratovú hodnotu ```c```. Nižšie popísané priradzovanie v jazyku python popisuje celú sekvenciu / kroky ktoré sme si práve vysvetlili.

### Priradzovanie v jazyku Python
<b>1. Priradenie ```1``` k premennej ```a```</b>
  - <b>1a. </b> Nastaví ```a->PyObject_HEAD->typecode``` na integer
  - <b>1b. </b> Nastaví ```a->val = 1```
    
1. Priradenie - <b>1a.</b> vytvorí novú *premennú a.Kedže v jazyku Python je všetko reprezentované ako objekt tak - vytvorí nový objekt ```a``` ktorý zdeklaruje že sa jedná o objekt typu integer. <b>1b.</b> V druhom kroku vykoná referenciu objektu ```a``` na hodnotu 1.
<br>

<b>2. Priradenie ```3``` do premennej ```b```</b>
   - <b>2a. </b> Nastaví ```b->PyObject_HEAD->typecode``` na integer
   - <b>2b. </b> Nastaví ```b->val = 3```

Spôsob priradzovania je rovnaký ako v bode 1.
<br>

<b>3. Volanie funkcie ```binary_add(a,b)```</b>
   - <b>3a. </b> hľadá typecode pre premennú a ```a->PyObject_HEAD```
   - <b>3b. </b> funkcia identifikuje premennú ```a``` ako objekt typu integer, priradí hodnotu k objektu ```a->val```
   - <b>3c. </b> hľadá typecode pre premennú b ```b->PyObject_HEAD```
   - <b>3d. </b> funkcia identifikuje premennú ```b``` ako objekt typu integer, priradí hodnotu k objektu ```b->val```
   - <b>3e. </b> zavolá funkciu ```binary_add<int, int>(a->val, b->val)```
   - <b>3f. </b> vysledok tohto zapiše ako result, objekt result je typu integer
 
<b>4. Vytvorenie objektu ```C```</b>
   - <b>4a. </b> nastavi ```c->PyObject_HEAD->typecode```  na integer
   - <b>4b. </b> nastavi ```c->val``` ako ```result```
<br>

Ako je možné vidieť na proovnaní priradzovania pri jazyku C a priradzovania Python, máme rádovo viac operacií ktoré Interpreter musí vykonať ako pri kompilátore (jazyka C)  
Dynamicky typovým sa teda myslí to že je potrebné vykonať omnoho viac krokok / operácií. Toto je primárny dôvod prečo je programovací jazyk Python pomalý v porovnaní s jazykom C pre operácie na numerických dátach. 

## Python je interpretovaný namiesto toho aby bol kompilovaný
Vyššie sme videli jeden rozdiel medzi interpretovaným a kompilovaným kódom. "Smart" kompilátor sa dokáže pozerať dopredu a optimalizovať pre opakované alebo nepotrebné operície, čo môže viesť k úrýchleniu celého procesu.

## Objektový model Pythonu môže viesť k neefektívnemu prístupu k pamäti
