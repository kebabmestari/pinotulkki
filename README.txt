PINOTULKKI
OHJEET
***********

Ohjelma tulkkaa pinokielta joka perustuu Forth-kieleen ja sen syntaksiin, komentoihin ym
Kieli on postfix-muodossa eli argumentit ensin, kasky sitten
Kaikki argumentit ovat kunkin scopen omassa pinossa ja argumentit otetaan pinon paalta jarjestyksessa
Tulokset, jos niita on, tyonnetaan pinon paalle
Lisaksi eri scopejen valilla voi lahettaa arvoja siirtamalla ne erilliseen globaaliin pinoon, stashiin komennoilla push ja pull
Muuten scopet ovat lokaaleja ja ne eivat voi vaikuttaa toisiinsa

Esimerkki:
1 5 + . drop
Summaa kaksi lukua, tulostaa tuloksen ja pudottaa arvon
# alkavat rivit ovat kommentteja

Tulkki ajetaan komennolla
python src/stacklang.py tiedostonimi.txt
TAI
python3 src/stacklang.py tiedostonimi.txt
riippuen ajajan jarjestelmasta

Loki tallentuu logs-kansioon

KURSSIN VAATIMA DEMO-OHJELMA ON TIEDOSTOSSA demo.txt JA AJETAAN KOMENNOLLA
python src/stacklang.py demo.txt

Tulkki toimii vain Python3:lla!

**********************************************
Kontrollirakenteet:

( jotain ) on LOOP
Looppia toistetaan jos pinon paallimmainen arvo on True loopin tullessa loppuun

{ jotain } on IF ehtolause
Blokkiin mennaan mikali pinon paallimmaisin arvo on True siihen tullessa
Mikali arvo on False blokki skipataan

**********************************************
Komennot:

Komento Argumentteja Kuvaus
+       2            Summa 
-       2            Vahennys
*       2            Kertolasku
/       2            Jakolasku

and     2            Looginen AND
or      2            Looginen OR
not     1            Looginen NOT

<       2            Pienempi kuin -> tulos boolean
>       2            Suurempi kuin  -> tulos boolean
==      2            Yhta suuri kuin -> tulos boolean, toimii myos stringeilla
!=      2            Erisuuri kuin -> tulos boolean, toimii myos stringeilla

dup     1            Kopioi paallimmaisen alkion ja siirtaa sen paalle
rot     3            Siirtaa kolmannen alkion paalle
rot-    3            Siirtaa paallimmaisen alkion kolmanneksi
roll4   4            Siirtaa neljannen alkion paalle
roll4-  4            Siirtaa paallimmaisen alkion neljanneksi
swap    2            Vaihtaa kahden paallimmaisen paikkaa
drop    1            Poistaa paallimmaisen alkion
over    2            Kopioi toisen alkion paallimmaiseksi
nip     2            Poistaa toisen alkion
tuck    2            Kopioi paallimmaisen alkion kolmanneksi

.       1            Tulostaa paallimmaisen alkion -> EI POISTA PINOSTA
read    0            Kysyy kayttajalta syotetta ja laittaa sen pinoon oikeaan kohtaan -> pinossa 'placeholder' komennon kohdalla

push    2            Siirtaa alkion 'stashiin' eli erilliseen pinoon missa se on nimetty toisen argumentin mukaisesti
pull    1            Hakee 'stashista' argumentin mukaisesti nimetyn arvon ja tyontaa sen pinoon oikeaan kohtaan

gfxinit  0           Luo graafisen ikkunan ja canvasin piirtoa varten
color    1           Vaihtaa piirtovaria esm white black blue jne
circle   3           Piirtaa ympyran argumentteina x, y, halkaisija
box      3           Piirtaa nelion argumentteina x, y, sivun pituus
rect     4           Piirtaa nelikulmion argumentteija x, y, vaakasivun pituus, pystysivun pituus
triangle 3           Piirtaa kolmion argumentteina x, y, sivun kohtisuora pituus
line     4           Piirtaa suoran argumentteina x1, y1, x2, y2
