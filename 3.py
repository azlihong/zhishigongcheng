
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#coding=utf-8
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql/")
sparql.setQuery('''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
select ?scientist ?name ?birthDate ?description{
?scientist rdf:type dbo:Scientist;
   dbo:birthDate ?birthDate;
   rdfs:label ?name;
   dct:description ?description
   filter regex(?birthDate,'-11-8')
FILTER (LANG(?name)="zh")

}
    '''
)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:

    print(result["scientist"]["value"],result["name"]["value"],result["birthDate"]["value"],
           result["description"]["value"])

    b = open("a.txt", 'a')
    b.write(result["scientist"]["value"])
    b.write(result["name"]["value"])
    b.write(result["birthDate"]["value"])
    b.write(result["description"]["value"])

