# PaperVis

PaperVis is a project of the Graphics and Interaction Laboratory for the lecture Information Visualization.


## Note

Exporting from Zotero will add fields for months like: aug or feb - these need to be defined in your BibTeX file like this
```bibtex
@STRING{ jan = "January" }
@STRING{ feb = "February" }
@STRING{ mar = "March" }
@STRING{ apr = "April" }
@STRING{ may = "May" }
@STRING{ jun = "June" }
@STRING{ jul = "July" }
@STRING{ aug = "August" }
@STRING{ sep = "September" }
@STRING{ oct = "October" }
@STRING{ nov = "November" }
@STRING{ dec = "December" }
```
or in whatever language you plan to use the parser


## Dependencies

```
* python-yaml
* python-nltk
* python-json
* tika
* scikit-learn
* scipy
* numpy

```

## ToDo

* port PDF reader over to python-pdfrw 
* cache results in a SQLite database
* add web interface