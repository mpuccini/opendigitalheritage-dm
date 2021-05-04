# Documentazione  
## Definizione  
L'obiettivo è realizzare un'applicazione client-server composta da un sito web dinamico che dialoga con un db che memorizza i dati.  
## Approccio:  
### Flask
Volendo realizzare un sito web dinamico, è stato scelto di scrivere il codice in python utlilizzando le  
librerie del framework Flask.  
Flask è un micro-web Framework Python che offre la possibilità di sviluppare applicazioni web semplici come  
blog o wiki, ma anche più complesse come un e-commerce. E' basato su:  
 - Jinja, un engine template che permette la creazione di file HTML, XML o in altri formati di markup, che  vengono restituiti all'utente mediante una risposta HTTP.  
 - Werkzeug WSGI, un toolkit per stabilire la comunicazione e le interazioni tre il server e le applicazioni web.    
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
    "grades": [{
        "date": {
            "$date": "2014-06-10T00:00:00.000Z"
        },
        "grade": "A",
        "score": 5
    }, {
        "date": {
            "$date": "2013-06-05T00:00:00.000Z"
        },
        "grade": "A",
        "score": 7
    }, {
        "date": {
            "$date": "2012-04-13T00:00:00.000Z"
        },
        "grade": "A",
        "score": 12
    }, {
        "date": {
            "$date": "2011-10-12T00:00:00.000Z"
        },
        "grade": "A",
        "score": 12
    }],
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

