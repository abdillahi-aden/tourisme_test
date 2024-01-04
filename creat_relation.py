from neo4j import GraphDatabase

driver = GraphDatabase.driver('bolt://3.254.142.186:7687', auth=('neo4j', 'neo4j'))

query = '''
LOAD CSV WITH HEADERS FROM '/home/ubuntu/donnee_mongo/datatourisme-tour-20231215.csv' AS line
CREATE (:POI { 
    name: line.Nom_du_POI, 
    category: line.Categories_de_POI, 
    latitude: toFloat(line.Latitude), 
    longitude: toFloat(line.Longitude), 
    description: line.Description 
})
'''

with driver.session() as session:
    result = session.run(query).data()
