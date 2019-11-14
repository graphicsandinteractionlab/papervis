#!/usr/bin/env python3

import tika
from tika import parser

from papervis.bibparser import BibParser

import yaml

config = yaml.safe_load(open("config/config.yml"))

def parse_pdf_to_raw(pdf_file_path):
    """converts pdf file to raw and returns contents"""
    raw = parser.from_file(pdf_file_path)
    return raw['content']

def main ():
    """"""
    bp = BibParser()
    
    bp.open(config['path'])
    
    pass

if __name__  == "__main__":
    main()
