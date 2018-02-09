# coding: utf-8

import PubMedParser


def test_answer(capsys):
    """
    PubMedParser.py:133: Warning:
    Unbekannter Fehler:(raised as a result of Query-invoked autoflush; consider using a session.no_autoflush block if this flush is occu
    rring prematurely) (psycopg2.DataError) value too long for type character varying(500)
     [SQL: 'INSERT INTO pubmed.tbl_keyword (fk_pmid, keyword, keyword_major_yn) VALUES (%(fk_pmid)s, %(keyword)s, %(keyword_major_yn)s)'
    ] [parameters: ({'fk_pmid': 29163864, 'keyword': 'Veterans', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'barriers',
    'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'ex-service personnel', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'help-seeking', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'mental health', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'stigma', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': u'\u2022 This article aimed to understand why a vast majority of veterans suffering from mental health difficulties do not seek professional help. \u2022 Living with untreated mental health difficulties has significant negative implications for individuals, society and the economy. \u2022 During interviews with veterans suffering from mental health difficulties, we learned about a number of barriers which got in the way of them accessing help, and a number of enablers which allowed them to get the help that they required.', 'keyword_major_yn': 'N'})]        warnings.warn("\nUnbekannter Fehler:"+str(e), Warning)                                                                            Traceback (most recent call last):                                                                                                    File "PubMedParser.py", line 724, in <module>
        run(options.medline_path, options.clean, int(options.start), options.end, int(options.PROCESSES))                                 File "PubMedParser.py", line 687, in run
        res = result.get()
      File "/home/bacey/anaconda3/envs/pubmedportable/lib/python2.7/multiprocessing/pool.py", line 572, in get                              raise self._value
    sqlalchemy.exc.DataError: (psycopg2.DataError) value too long for type character varying(500)                                        [SQL: 'INSERT INTO pubmed.tbl_keyword (fk_pmid, keyword, keyword_major_yn) VALUES (%(fk_pmid)s, %(keyword)s, %(keyword_major_yn)s)'] [parameters: ({'fk_pmid': 29163864, 'keyword': 'Veterans', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'barriers', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'ex-service personnel', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'help-seeking', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'mental health', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': 'stigma', 'keyword_major_yn': 'N'}, {'fk_pmid': 29163864, 'keyword': u'\u2022 This article aimed to understand why a vast majority of veterans suffering from mental health difficulties do not seek professional help. \u2022 Living with untreated mental health difficulties has significant negative implications for individuals, society and the economy. \u2022 During interviews with veterans suffering from mental health difficulties, we learned about a number of barriers which got in the way of them accessing help, and a number of enablers which allowed them to get the help that they required.', 'keyword_major_yn': 'N'})]
    """

    # Name of that temporary test-database where the articles will be imported into, during the test-run.
    PubMedParser.db = 'pubmed_test_db'

    # Name of the folder containing those example XML files
    # which will be imported into the temporary test-database during the test-run.
    folder_with_example_xml_files = 'test/resources/article-with-long-keyword/'

    PubMedParser.run(folder_with_example_xml_files, clean=True, start=0, end=None, PROCESSES=1)

    std_output, std_error = capsys.readouterr()

    #assert 'Finished' in std_output
    #'value too long for type character varying(500)'

    assert std_error == ''
