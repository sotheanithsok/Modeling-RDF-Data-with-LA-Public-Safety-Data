from Backend.rdf import RDF
rdf = RDF()
rdf.add("https://data.lacity.org/resource/2nrs-mtv8")
rdf.add("https://data.lacity.org/resource/amvf-fr72")

#https://data.lacity.org/resource/amvf-fr72
#https://data.lacity.org/resource/2nrs-mtv8

rdf.export("output.txt")