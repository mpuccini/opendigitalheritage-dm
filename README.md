# Documentazione
## Introduzione 

## Definizione  
L'obiettivo è realizzare proof of concept di un'applicazione client-server con lo scopo di memorizzare informazioni sui  
beni culturali mediante:  
 - Immagini  
 - Documenti in formato PDF  
 - Modellazioni 3D    
## Approccio
### Piattaforma ENEA  
ENEAGRID è l'infrastruttura che fornisce l'accesso alle risorse di calcolo della Divisione ICT dell'ENEA.  
Le principali risorse di calcolo di ENEAGRID sono i cluster CRESCO.  
Il cluster CRESCO6 di Portici è un sistema di calcolo costituito da 434 nodi. Ogni nodo ha:  
 - 2 socket da 24 core con processore Intel(R) Xeon(R) Platinum 8160 con frequenza di clock pari 2.10GHz e 192 GB di RAM
 - Una interfaccia Intel Omni-Path 100 Gb/s
 Due interfacce GbE
 - Supporto BMC/IPMI 1.8 e software per la gestione remota della console
Si hanno quindi a disposizione 20832 core connessi tra loro da una rete a larga banda e bassa latenza basata su Intel Omni-Path a 100 Gb/s.
L'utilizzo del cluster avviene facendo il login su uno dei nodi di front-end. I nodi di front-end servono semplicemente  
per il lancio delle applicazioni tramite LSF, per editare i propri script di lancio o per le compilazioni.  
file system disponibili su CRESCO6 sono:  
 - AFS filesystem geografico e accessibile da qualsiasi nodo in ENEA e nel  “mondo” che installa il client AFS. Quota di Default per user: 10GB  
 - GPFS il file system di IBM ad alte prestazioni per l'I/O parallelo.    
### Python 
Python è un linguaggio di programmazione di alto livello orientato agli oggetti   adatto, tra gli altri usi, a svilluppare applicazioni distribuite, scripting, computazione numerica e system testing.  
 - E' un linguaggio multi-paradigma che ha fra i principali obiettivi la dinamicità,  semplicità e flessibilità. Supporta il paradigma OO e molte  caratteristiche di programmazione funzionale e riflessione.  
 - Le caratteristiche puù immediatamente riconoscibili di Python sono le variabili  non tipizzate e l'uso dell'indentazione per la sintassi delle specifiche al posto delle più comuni parentesi.  
 - Altre caratteristiche distintive sono l'overloading di operatori e funzioni   tramite delegati la presenza di un ricco assortimento di tipi e funzioni di base  e librerie standard, sintassi avanzate quali slicing e list comprension.  
 - Il controllo dei tipi è forte e viene eseguito in runtime (dynamic typing):  
 una variabile è un contenitore a cui viene associata un'etichetta che può  essere associata a diversi contenitori anche di tipo diverso durante il suo tempo  di vita.  
Fa parte di Python un sistema garbage collector per liberazione e recupero automatico della memoria di lavoro  
```python
a= 5
#qui a è un intero
a= "ciao mondo"
#qui a è una stringa
```  
#### Flask
Volendo realizzare un sito web dinamico, è stato scelto di scrivere il codice in python utlilizzando le  
librerie del framework Flask.  
Flask è un micro-web Framework Python che offre la possibilità di sviluppare applicazioni web semplici come  
blog o wiki, ma anche più complesse come un e-commerce. E' basato su:  
 - Jinja, un engine template che permette la creazione di file HTML, XML o in altri formati di markup, che  vengono restituiti all'utente mediante una risposta HTTP.  
 - Werkzeug WSGI, un toolkit per stabilire la comunicazione e le interazioni tre il server e le applicazioni web.  
```python
#esempio di hello word
from flask import Flask
app = Flask(name)

@app.route("/")
def hello():
    return "Hello World"


if name == "main":
    app.run(debug=False)
```
### MongoDB
E' stato scelto di gestire i dati in maniera persistente con sfruttando l'infrastrutture offerte da MongoDB.  
MongoDB è un DBMS, Data Management System, NoSQL e doc-oriented. Per memorizzare e gestire i dati, al posto  
di tabelle come nei DBMS SQL, MongoDB utilizza dei documenti in stile JSON con schema dinamico chiamati BSON.  
Ecco un esempio di documento per memorizzare dati di un ristorante:  
```JSON
{
    "address": {
        "building": "2780",
        "coord": [-73.98241999999999, 40.579505],
        "street": "Stillwell Avenue",
        "zipcode": "11224"
    },
    "borough": "Brooklyn",
    "cuisine": "American",
    "name": "Riviera Caterer",
    "restaurant_id": "40356018"
}
```  
E' utilizzato da siti web come Ebay, Craigslist e The Ney York times, ed è il piu popolare DBMS NoSQL.  
Alcune delle caratteristiche principali sono:  
 - **Query ad hoc**:  
 MongoDB supporta ricerche per campi, intervalli e regular expression. Le query possono   restituire campi specifici del documento e anche includere funzioni definite dall'utente in JavaScript.  
 - **Indicizzazione**:  
 qualunque campo in MongoDB può essere indicizzato (gli indici in MongoDB sono   concettualmente similari a quelli dei tradizionali RDBMS).  
 - **Alta affidabilità**:  
 MongoDB fornisce alta disponibilità e aumento del carico gestito attraverso i replica set.  Un replica set consiste in due o più copie dei dati.Ogni replica può avere il ruolo di copia   primaria o secondaria in qualunque momento.  La replica primaria effettua tutte le scritture e le letture. Le repliche secondarie mantengono una copia dei dati della replica primaria attraverso un meccanismo di replicazione incluso nel prodotto.  Quando una replica primaria fallisce, il replica set inizia automaticamente un processo di elezione per determinare quale replica secondaria deve diventare primaria.  Le copie secondarie possono anche effettuare letture, con dati eventualmente consistenti di default.  
 - **Sharding e bilanciamento dei dati**:  
 MongoDB scala orizzontalmente usando lo sharding. L'utente deve scegliere una chiave di sharding, che  determina come i dati di una collection saranno distribuiti tra i vari nodi.  
 I dati sono divisi in intervalli (basati sulla chiave di shard) e distribuiti su molteplici shard  
 (uno shard è un replica set, quindi con una replica primaria e due o più repliche secondarie).  
 MongoDB include un meccanismo di bilanciamento dei dati, spostando gli intervalli di dati da uno shard troppo  carico a uno shard meno carico, in modo da bilanciare la distribuzione dei dati all'interno del cluster.  
 - **File storage**:  
 MongoDB può essere usato anche come un file system, traendo vantaggio dalla caratteristiche di replicazione e  di bilanciamento su più server per memorizzare file, anche di grandi dimensioni(funzione GridFS).  
 Invece di memorizzare il file in un singolo documento, GridFS divide il file in tante parti più piccole,  chiamate chunks, e memorizza ognuno di questi chunk in un documento separato.  
 - **Aggregazione**:  
 MongoDB supporta due modalità di aggregazione dei dati: il MapReduce e l'Aggregration Framework.  
 Quest'ultimo lavora come una pipeline e permette di ottenere risultati molto più rapidamente del MapReduce  grazie all'implementazione in C++.
 - **Capped Collection**:  
 MongoDB supporta collection a dimensioni fisse chiamate capped collection.  
 Questo tipo di collection mantiene l'ordine di inserimento e una volta raggiunta la dimensione definita, si comporta come una coda circolare.

## Architettura del sistema  
Le operazioni principali che il sistema dovrà offrire sono le seguenti:
 - Inserimento nel DB di nuovi dati relativi ai beni culturali. Dovrà quindi consentire l'aggiunta di nuove  
 immagini, nuovi documenti PDF e nuove modellazioni 3D.
 - Ricerca di informazioni gia presenti nella Banca Dati.  
### Interfaccia Utente
L'UI sarà composta da input grafici che guideranno l'utente a compiere le operazioni desiderate.  
L'HomePage avrà offrirà tre diverse opzioni di interazione. L'utente potrà:
 - scegliere di inserire un nuovo dato nel DB tramite l'interazione con un input grafico che lo condurra ad una pagina web che consentirà di proseguire con questa operazione.
 - scegliere di cercare un dato nel DB tramite l'interazione con un input grafico che lo condurra ad una pagina  web che consentirà di proseguie con questa operazione. In questo caso l'utente dovra necessariamente  
 conoscere il valore di alcuni campi del documento o dei documenti che vuole ottere.  
 - scegliere di cercare un dato nel DB tramite una ricerca testuale. Questa attività sarà agevolata dal sistema  poichè MongoDB offre la possibilità di effettuare Full Text Search.    
 ```python
 #Full Text Search:
 text = 'Douro River and Ribeira Square'
 text_results = airbnb.listingsAndReviews.find({"$text": {"$search": text}},{"_id":0, "name":1})
 ```
 ### Operazione di Inserimento
 Dopo che l'utente avra scelto l'operazione "Inserisci", verrà proiettata una pagina web che presenterà  le seguenti opzioni gestite tramite input grafico:
 - Inserimento PDF  
 - Inserimento Immagine  
 - Inserimento Modello 3D  
Qualunque sia la scelta dell'utente, questo verrà condotto ad una pagine web ad hoc per compilare i campi di una form.  
```HTML
<!--Form per inserire un documento testuale--> 
<form  method="post" enctype="multipart/form-data">
  CAMPO TESTO <input type="text" name="testo1">
  FILE <input type="file" name="file1">
  <input type="submit" value="Upload">
</form>
```  
### Operazione di Ricerca
Dopo che l'utente avra scelto l'operazione "Ricerca", verrà proiettata una pagina web che presenterà  le seguenti opzioni gestite tramite input grafico:
 - Ricerca PDF  
 - Ricerca Immagine  
 - Ricerca Modello 3D  
Qualunque sia la scelta dell'utente, questo verrà condotto ad una pagine web ad hoc per compilare i campi di una form. Successivamente i valori inseriti verranno utilizzati per realizzare una Query ad hoc con lo scopo di estrapolare i dati dal DB.  
Se l'utente vorrà cercare un'informazione tramite la ricerca testuale dovrà selezionare l'apposita barra di   ricerca e scrivere le parole chiave presenti nei documenti che vuole ottenere.  
## Note markdown







 - primo
 - secondo
 * terzo
   - sottolista

 1. primo
 2. secondo
   1. sottolista

Protrebbe essere evidenziare del codice: `git push`   
```
git pull
```

```python
import pandas as pd

data = pd.readCSV("example.csv")
```

## Esempi di testo

**Scrive testo in grassetto**  
*oppure in corsivo*

[link esterni](https://www.intranet.enea.it/acl_users/credentials_cookie_auth/require_login?came_from=https%3A//www.intranet.enea.it/)   

[link interni](esempio.md)

