from Connector import Connector
from elsapy.elssearch import ElsSearch
from elsapy.elsdoc import FullDoc, AbsDoc
from ScopusDocument import ScopusDocument
import pickle


class Query:

    def __init__(self, query, dump = False):
        print("Starting query: ", query)
        self.connect = Connector()
        self.doc_search(query)
        if dump == True:
            self.dump(query)
        

    def doc_search(self, query):
        self.doc_srch = ElsSearch(query, 'scopus')
        self.doc_srch.execute(self.connect.client, get_all = True)
        print("Retrieved ", len(self.doc_srch.results), "documents.")
        self.documents = []
        for doc in self.doc_srch.results:
            document = self.prepare_doc(doc)
            self.documents.append( document )

    def prepare_doc(self, doc):
        scp_doc = AbsDoc(scp_id = doc["dc:identifier"])
        if scp_doc.read(self.connect.client):
            document = ScopusDocument( scp_doc, self.connect )
            return document
        else:
            print("Read document failed.")
            return None

    def dump(self, query):
        with open(query+'_data.pkl', 'wb') as output:
            pickle.dump(self.doc_srch, output, pickle.HIGHEST_PROTOCOL)