# coding: utf-8

import PubMedParser


def test_too_many_conflicts(capsys):
    # Name of that temporary test-database where the articles will be imported into, during the test-run.
    PubMedParser.db = 'import_using_pubmedportable'

    # Name of the folder containing those example XML files
    # which will be imported into the temporary test-database during the test-run.
    folder_with_example_xml_files = '../tmp/pubmed-2018-updatefiles/'

    PubMedParser.run(folder_with_example_xml_files, clean=False, start=0, end=None, PROCESSES=1)

    std_output, std_error = capsys.readouterr()

    assert 'Finished' in std_output
    assert std_error == ''
