# enter_player


## Prerequisites
[python 3](https://www.python.org/downloads/)

## Library
[pygame](https://www.pygame.org/news)

## Installation
Per l'installazione della libreria pygmae si procede con il comando da terminale per: `pip install pygame` oppure eseguendo il file [setup.bat](\etc\setup.bat).

**SI CONSIGLIA DI ESEGUIRE IL PROGRAMMA PRIMA DELL'USO** per creare i file e le cartelle necessarie

## Program
Il programma apre in input il file [playlist.csv](\bin\playlist.csv) ed esegue il comando delle tracce audio a seconda del parametro impostato, procede sequenzialmente nella playlist dando "INVIO"

Si può navigare nella playlist NON lasciando vuoto il campo quando si passa alla traccia successiva, ma inserendo il numero della traccia nella playlist a cui andare, qualsiasi altro input può essere usato per mandare avanti nella playlist senza eseguire il comando preimpostato ed impostare la nuova traccia da eseguire

**ATTENZIONE** quando si è all'ultima traccia, per poter navigare nella playlist, non inserire valori più alti del numero di tracce. Per questo bisogna mettere sempre come ultima traccia lo STOP della traccia che conclude il file

## playlist.csv
Come inizio viene impostato il comando della traccia con:

`PLAY` Fa partire la traccia anche se la traccia precedente non presenta lo STOP

`STOP` Ferma la traccia e deve essere dato il PLAY per farla cominciare nuovamente

`PAUS` Mette in pausa la traccia e può essere subito fatta partire da dove ci si è femati

`UNPA` Continua la riproduzione dopo essere stata messa in pausas

`FOUT` Ferma la traccia con fade-out **UTILIZZABILE CON TRE ARGOMENTI NEL CSV** (valore in ms)

Sucessivamente **SEPARATO CON ","** inserire il nome del file da riprodurre con estensione compresa

Se il file presenta spazi, mettere il nome tra apici: **" "**

**Come ultima traccia mettere sempre lo STOP della traccia che conclude il file**

IL FILE DOVRÀ ESSERE SIMILE A QUESTO:

    PLAY,"Track 1.mp3"
    PAUS,"Track 1.mp3"
    UNPA,"Track 1.mp3"
    STOP,"Track 1.mp3"
    PLAY,Track_2.mp3
    PLAY,Track_3.mp3
    STOP,Track_3.mp3

### Tre argomenti
Il file può contenere tre argomenti, ad esempio:

    PLAY,01,"Track 1.mp3"
    PAUS,,"Track 1.mp3"
    UNPA,10,"Track 1.mp3"
    STOP,,"Track 1.mp3"
    PLAY,,"Track 1.mp3"
    FOUT,2000,"Track 1.mp3"
    PLAY,,Track_2.mp3
    PLAY,,Track_3.mp3
    STOP,,Track_3.mp3

#### Volume
Il secondo argomento per PLAY e UNPA funge da regolatore di volume da 1 a 10 (i numeri singoli possono essere preceduti dallo zero ma è ininfuente: 01 o 1).

Se non vengono impostati valori di default e 10

#### Fade-out
Il secondo argomento per FOUT funge da fade-out in millisecondi

## Problems
Se si riscontrano problemi con la libreria pygmae probabilmente bisogna aggiornarla con il comando: `pip install --upgrade pygame` oppure eseguendo il file [setup.bat](\etc\setup.bat).

## Author
Vicentini Tommaso

