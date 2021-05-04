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

