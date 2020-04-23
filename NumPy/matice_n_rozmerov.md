# Matice n-rozmerov

V balíku NumPy je hlavným objektom homogénne viacrozmerné pole. Predstavuje tabuľku prvkov (zvyčajne čísel) rovnakého typu. Takáto tabuľka reprezentuje indexovanú n-ticu nezáporných čísel. Podobne ako aj vo Fyzike, tak aj v NumPy jednotlivé rozmery nazývame osi.

Pre príklad, máme objekt ktorý je definovaný v trojdimenzionalnom priestore súradnicami X,Y,Z. Pre každú súradnicu sa vyskytuje v nejakom bode. Objekt X[2,3,5] teda vieme zakresliť takto:

![image](images/3d_dimension.jpeg)


Tento bod vieme zapísať aj pomocou vektora či jeho súradnice vložiť do matice kde súradnice bodu budú mať jednu os. Táto os obsahuje 3 prvky, takže hovoríme že má dĺžku 3. V príklade uvedenom nižšie má pole 2 osi. Prvá os má dĺžku 2, druhá os má dĺžku 3.

```
[[1., 0., 0.],
 [0., 1., 2.]]
```
Objekt pola v NumPy sa nazýva ```ndarray```. Taktiež sa označuje ```array```. Treba poznamenať že pole ```numpy.array``` nieje to isté ako objekt ```array.array``` v štandardnej Python knižnici, ktorá poskytuje len jedno rozmerné (dimenzionálne) pole a ponúka omnoho menej funkcionalít. 

Dôležité atribúty objektu ```ndarray```:

<b>ndarray.ndim</b>
 - vypíše počet osí (dimenzií) poľa

<b>ndarray.shape</b>
 - vypíše osi daného poľa. Táto n-tica zložené z integerov indikuje veľkosť poľa v každej jeho dimenzii (osi). Pre Maticu s <b>n</b> riadkami a <b>m</b> stĺpcami, ```shape``` - tvar bude ```(n,m)```. Dĺžka n-tice ``shape``` bude reprezentovať počet osi, ```ndim```.

<b>ndarray.size</b>
 - celkové číslo / počet elementov ktoré obsahuje dané pole. 

<b>ndarray.dtype</b>
 - objekt popisujúci typ elementu v poli. Využíva sa najmä v tedy ak máme dátové jednotky ktoré nezaberajú veľa bajtov v pamäti a chceme exaktne určit rozsah bunky ktorá bude držať dané číslo / premennú.


<b>ndarray.itemsize</b>
 - vráti veľkosť v byte každého elementu v poli. 

<ndarray.data>
 - reprezentuje buffer ktorý obsahuje aktuálnu premennu poľa. Bežne sa tento atribút nevyužíva pretože pristupujeme k elementu poľa cez jeho index.


## príklady sú uvedené v súboroch vyššie.
