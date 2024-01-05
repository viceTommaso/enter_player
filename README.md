# enter_player


## Prerequisites
[python 3](https://www.python.org/downloads/)

## Library
[pygame](https://www.pygame.org/news) | [keyboard](https://github.com/boppreh/keyboard)

## Installation
Per l'installazione della libreria pygame si procede con il comando da terminale per: `pip install pygame`

Per l'installazione della libreria keyboard si procede con il comando da terminale per: `pip install keyboard`

Oppure (solo windows) eseguendo il file [setup.bat](\etc\setup.bat).

**SI CONSIGLIA DI ESEGUIRE IL PROGRAMMA PRIMA DELL'USO** per creare i file e le cartelle necessarie

## Program
Il programma apre in input il file [playlist.csv](\bin\playlist.csv) ed esegue il comando delle tracce audio a seconda del parametro impostato, procede sequenzialmente nella playlist dando `spazio`

Si può navigare nella playlist con le freccette: `sinistra`/`su` per tornare indietro, `destra`/`giù` per andare avanti, mentre `invio` per interrompere le  tracce di ogni canale

Se la lista dovesse risultare troppo lunga nello schermo, all'interno del programma alla riga 16 e 17 sono presenti due variabili:

`line_limit`: il numero di tracce che si vogliono visualizzare

`line_margin`: il numero di tracce che si vogliono visualizzare prima e dopo della traccia che verrà riprodotta.
(Viene corretto in automatico in caso fosse maggiore del numero di tracce che si vogliono visualizzare)

**IL PROGRAMMA PERCEPISCE I COMANDI ANCHE SE LA FINESTRA NON È SELEZIONATA**

## playlist.csv
Come inizio viene impostato il comando della traccia con:

`PLAY` Fa partire la traccia anche se la traccia precedente non presenta lo STOP

`STOP` Ferma la traccia e deve essere dato il PLAY per farla cominciare nuovamente

`PAUS` Mette in pausa la traccia e può essere subito fatta partire da dove ci si è femati

`UNPA` Continua la riproduzione dopo essere stata messa in pausas

`FOUTÙ Ferma la traccia con fade-out **UTILIZZABILE CON TRE ARGOMENTI NEL CSV** (valore in ms)

Sucessivamente **SEPARATO CON ","** inserire il nome del file da riprodurre con estensione compresa

Se il file presenta spazi, mettere il nome tra apici: **"no me.mp3"**

ESCLUSO PER IL `PLAY` non è necessario ripetere il nome della traccia per gli altri comandi, è sufficiente lasciare il campo vuoto o per comodità aggiungere un commento

**Come ultima traccia mettere sempre lo STOP della traccia che conclude il file**

IL FILE DOVRÀ ESSERE SIMILE A QUESTO:

    PLAY,"Track 1.mp3"
    PAUS,
    UNPA,"unpause traccia precedente"
    STOP,
    PLAY,Track_2.mp3
    PLAY,Track_3.mp3
    STOP,

### Tre argomenti
Il file può contenere tre argomenti, ad esempio:

    PLAY,01,"Track 1.mp3"
    PAUS,,
    UNPA,10,"unpause traccia precedente con volume più alto"
    STOP,,
    PLAY,,"Track 1.mp3"
    FOUT,2000,
    PLAY,,Track_2.mp3
    PLAY,,Track_3.mp3
    FOUT,50,
    STOP,,

#### Volume
Il secondo argomento per PLAY e UNPA funge da regolatore di volume da 1 a 10 (i numeri singoli possono essere preceduti dallo zero ma è ininfuente: 01 o 1).

Se non vengono impostati, il valore di default è 10

#### Fade-out
Il secondo argomento per FOUT funge da fade-out in millisecondi

### Quattro argomenti
Il file può contenere quattro argomenti, ad esempio:

    PLAY,01,,"Track 1.mp3"
    PAUS,,,
    UNPA,10,,
    STOP,,,
    PLAY,,1,Track_4.mp3
    PLAY,,,"Track 1.mp3"
    FOUT,2000,,
    PLAY,,,Track_2.mp3
    PLAY,,,Track_3.mp3
    FOUT,50,,
    FOUT,,1,"Fade out canale 1"
    STOP,,,

Il terzo argomento funge da canale (da `0` a `5`), in questo modo si possono controllare più tracce conemporaneamente ma su canali diversi

Se non viene impostato un valore il canale è `0`

Se si vogliono utilizzare i canali bisogna usare quattro argomenti, il secondo se non necessario può tranquillamente rimanere vuoto

## Problems/Bugs
Se si riscontrano problemi con la libreria pygame probabilmente bisogna aggiornarla con il comando: `pip install --upgrade pygame`

Se si riscontrano problemi con la libreria keyboard probabilmente bisogna aggiornarla con il comando: `pip install --upgrade keyboard`

Oppure (solo windows) eseguendo il file [setup.bat](\etc\setup.bat).

Se si naviga nella playlist è bene non posizionarsi su tracce al di fuori del "PLAY" per non esegure il comando su l'ultima traccia eseguita

Il file input essendo .csv non è variabile in argomenti, dunque non variare il numero di `,` per riga

Usare soltando `,` per separare gli argomenti nel flie di input

Per evitare eventuali lag, i nomi dei file audio devono essere puliti da `.` (al di fuori di quello prima dell'estensione), e da spazi

**SE POSSIBILE AVVIARE TUTTE LE TRACCE SEQUENZIALMENTE (TENENDO PREMUTO `spazio`) PER FARE IN MODO CHE IL COMPUTER LEGGA PIÙ VELOCEMENTE LE TRACCE ALL'OCCORENZA IN UN SECONDO MOMENTO**

Per escludere potenziali bugs, non lasciare linee vuote nel file di input


## Author
Vicentini Tommaso

