from pymongo import MongoClient
import json
import requests
import sys

print ('Argument List:', str(sys.argv[1]))
dburi = sys.argv[1]
dbname = "nihtrial"
c = MongoClient( dburi )
# db = c[ dbname ]
# pubchem_cluster = db['chemical_cluster'].find_one({'name': 'pubchem_cluster'})['data']

x = requests.get(str(sys.argv[2]))
# print (pubchem_cluster)

def main():              
    with open('chem_cluster.json', 'wb') as outf:
        outf.write(x.content)

if __name__ == "__main__":
    main()
