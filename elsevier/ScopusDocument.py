from Connector import Connector
from elsapy.elsdoc import FullDoc, AbsDoc

class ScopusDocument:

    def __init__(self, scp_doc, connect):
        self.doi = scp_doc.data["coredata"]["prism:doi"]
        print("Analyzing document ", self.doi)
        self.sidentifier = scp_doc.data["coredata"]["dc:identifier"]
        self.authors_data = scp_doc.data["coredata"]["dc:creator"]["author"]
        self.len_authors = len(self.authors_data)
        self.retrieve_authors()
        self.retrieve_fulldoc(connect)

    def retrieve_authors(self):
        print("Document has ", self.len_authors)
        authors = []
        for author in self.authors_data:
            author_dic = {}
            author_dic["indexed-name"] = author["preferred-name"]["ce:indexed-name"]
            author_dic["author_url"] = author["author-url"]
            authors.append(author_dic)
        self.authors = authors

    def retrieve_fulldoc(self, connect):
        doi_doc = FullDoc(doi = self.doi)
        if doi_doc.read(connect.client):
            print ("doi_doc.title: ", doi_doc.title)
            doi_doc.write()   
            ##### Stuff to explore
            # print(doi_doc.data["originalText"])
            ### ABSTRACT !!!!
            # print(doi_doc.data["coredata"]["dc:description"])
        else:
            print ("Read document failed.")