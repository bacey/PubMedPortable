# coding: utf-8

"""
This was the error message which was received during
the parsing of the article (with PMID=29163864) which is in the
ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/pubmed18n0931.xml.gz file:

PubMedParser.py:133: Warning:
(psycopg2.DataError) value too long for type character varying(500)

[SQL: 'INSERT INTO pubmed.tbl_keyword (fk_pmid, keyword, keyword_major_yn)
VALUES (%(fk_pmid)s, %(keyword)s, %(keyword_major_yn)s)']
[parameters: ({'fk_pmid': 29163864, 'keyword': 'Veterans', 'keyword_major_yn': 'N'},
{'fk_pmid': 29163864, 'keyword': u'\u2022 This article... LOTS OF CHARACTERS.', 'keyword_major_yn': 'N'})]

Traceback (most recent call last):
File "PubMedParser.py", line 724, in <module>
    run(options.medline_path, options.clean, int(options.start), options.end, int(options.PROCESSES))
    File "PubMedParser.py", line 687, in run
    res = result.get()

sqlalchemy.exc.DataError: (psycopg2.DataError) value too long for type character varying(500)
"""

import PubMedParser


def test_article_with_long_keyword_can_be_imported(capsys):
    # Name of that temporary test-database where the articles will be imported into, during the test-run.
    PubMedParser.db = 'pubmed_test_db'

    # Name of the folder containing those example XML files
    # which will be imported into the temporary test-database during the test-run.
    folder_with_example_xml_files = 'test/resources/article-with-long-keyword/'

    PubMedParser.run(folder_with_example_xml_files, clean=True, start=0, end=None, PROCESSES=1)

    std_output, std_error = capsys.readouterr()

    assert 'Finished' in std_output
    assert std_error == ''
