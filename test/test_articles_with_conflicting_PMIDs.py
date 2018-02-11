# coding: utf-8

"""
This was the error message which was received during the import of the
ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/pubmed18n0949.xml.gz and the
ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/pubmed18n0952.xml.gz files:

PubMedParser.py:137: Warning:
IntegrityError: (raised as a result of Query-invoked autoflush;
consider using a session.no_autoflush block if this flush is occurring prematurely)
(psycopg2.IntegrityError) duplicate key value violates unique constraint "tbl_medline_citation_pkey"
DETAIL:  Key (pmid)=(9402755) already exists.

[SQL: 'INSERT INTO pubmed.tbl_medline_citation
(pmid, date_created, date_completed, date_revised, number_of_references, keyword_list_owner,
citation_owner, citation_status, article_title, start_page, end_page, medline_pgn,
article_affiliation, article_author_list_comp_yn, data_bank_list_complete_yn,
grant_list_complete_yn, vernacular_title) VALUES
(%(pmid)s, %(date_created)s, %(date_completed)s, %(date_revised)s, %(number_of_references)s, %(keyword_list_owner)s,
%(citation_owner)s, %(citation_status)s, %(article_title)s, %(start_page)s, %(end_page)s, %(medline_pgn)s,
%(article_affiliation)s, %(article_author_list_comp_yn)s, %(data_bank_list_complete_yn)s,
%(grant_list_complete_yn)s, %(vernacular_title)s)']

[parameters: {'article_title': 'Mechanism of formation of novel covalent drug.DNA interstrand
cross-links and monoadducts by enediyne antitumor antibiotics.', 'citation_owner': 'NLM',
'keyword_list_owner': None, 'date_completed': datetime.date(1998, 1, 8), 'number_of_references': '0',
'data_bank_list_complete_yn': 'Y', 'start_page': None, 'article_author_list_comp_yn': 'Y',
'medline_pgn': '14975-84', 'date_revised': datetime.date(2017, 12, 11),
'article_affiliation': 'Department of Biological Chemistry and Molecular Pharmacology.',
'grant_list_complete_yn': 'Y', 'date_created': None,
'pmid': 9402755,
'citation_status': 'MEDLINE', 'vernacular_title': None, 'end_page': None}]

These are the two conflicting PubmedArticles:
  zfgrep -B 5 -A 250 9402755 pubmed18n0949.xml.gz > pmid-9402755-from-pubmed18n0949-xml-gz
  zfgrep -B 5 -A 250 9402755 pubmed18n0952.xml.gz > pmid-9402755-from-pubmed18n0952-xml-gz
"""

import PubMedParser2


def test_when_two_articles_have_the_same_PMIDs_then_the_revised_one_overwrites_the_older(capsys):
    # Name of that temporary test-database where the articles will be imported into, during the test-run.
    PubMedParser2.db = 'pubmed_test_db'

    # Name of the folder containing those example XML files
    # which will be imported into the temporary test-database during the test-run.
    folder_with_example_xml_files = 'test/resources/articles_with_conflicting_PMIDs/'

    PubMedParser2.run(folder_with_example_xml_files, clean=True, start=0, end=None, PROCESSES=1)

    std_output, std_error = capsys.readouterr()

    assert 'Finished' in std_output
    assert std_error == ''

