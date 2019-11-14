#!/usr/bin/env python3

import bibtexparser
from bibtexparser.bparser import BibTexParser

class BibParser:
    def __init__(self):
        pass
        
    def open(self,bibfile):
        
        with open(bibfile) as bibtex_file:
            bibtex_str = bibtex_file.read()
        
        # tune the parser
        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = True
        parser.homogenise_fields = True
        
        self.bib_database = bibtexparser.loads(bibtex_str, parser)

        # print(self.bib_database.entries)
        
        # get all PDFs and store them as a dictionary with the id as index
        for e in self.bib_database.entries:
            # print(e['ID'] + " " + e['file'].split(':')[1])
            self.pdf_files[e['ID']] = e['file'].split(':')[1]