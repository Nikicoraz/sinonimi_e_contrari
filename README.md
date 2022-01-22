# sinonimi_e_contrari

Modulo di python per trovare sinonimi e contrari di parole tramite il sito [Sapere Virgilio](https://sapere.virgilio.it/parole/sinonimi-e-contrari/)

# Come usarlo

- In un file python importa il modulo  
```py 
import sinonimi_e_contrari
```

- e poi per trovare le parole si utilizza la funzione richiedi che prende come primo paramentro la parola da cercare e come secondo parametro se cercare un sinonimo o un contrario in base all'Enum Request  
```py
sinonimi_e_contrari.richiedi("cane", sinonimi_e_contrari.Request.SINONIMI)
```
