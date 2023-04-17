from flask import Flask,render_template,redirect,request
import rdflib
app = Flask(__name__)
g = rdflib.Graph()
g.parse("KMSWT.rdf")

@app.route('/subscriber',methods=['POST'])
def Subsriber():
    # First_Name = request.form.get('First_Name')
    # Last_Name = request.form.get('Last_Name')
    # Email = request.form.get('Email')
    # Password = request.form.get('Password')
    Genre = request.form.get('Genre')
    Artist = request.form.get('Artist')
    q1 = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ab: <http://www.semanticweb.org/dell/ontologies/2023/3/untitled-ontology-33#>
        SELECT ?title ?genre ?popu
        WHERE {
           
            ?song ab:producedBy ?artist;
                  ab:hasGenre ?genre;
            FILTER regex(str(?genre), \"""" + Genre + """\").
            ?song ab:hasPopularity ?popu;
                  ab:hasTitle ?title.
            ?artist ab:hasName ?artistname.
        } ORDER BY DESC (?popu) LIMIT 605
        """
    q2 = """
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ab: <http://www.semanticweb.org/dell/ontologies/2023/3/untitled-ontology-33#>
        SELECT ?title ?genre ?popu
        WHERE {
           
            ?song ab:producedBy ?artist.
            FILTER regex(str(?artist), \"""" + Artist + """\").
            ?song ab:hasGenre ?genre;
                  ab:hasPopularity ?popu;
                  ab:hasTitle ?title.
            ?artist ab:hasName ?artistname.
        } ORDER BY DESC (?popu) LIMIT 605
        """
    songs_names = []
    for r in g.query(q1):
        Endpoint_1 = r['title']
        songs_names.append(Endpoint_1[ : ])
    artist_names = []
    for r in g.query(q2):
        Endpoint_2 = r['title']
        artist_names.append(Endpoint_2[ : ])
    return render_template('subscriber.html',songs_names=songs_names,artist_names=artist_names,Genre=Genre,Artist=Artist)

@app.route('/index')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/')
def Main_Redirection():
    return redirect('/index')

@app.route('/<string:url>')
def Routes_Redirection(url):
    return redirect('/index')

if __name__ == '__main__':
    app.run()
