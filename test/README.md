
# How to run the tests

1. Install pytest. For example, `conda install pytest` or `pip install pytest`.

1. Create the `pubmed_test_db` database. This temporary test-database will hold
   the articles which are created during the test-runs.

   One way to create this test database is like this
   (given that the PostgreSQL `parser` user already exists
   with the `parser` password):

   ```bash
   $ sudo su - postgres
   $ createdb pubmed_test_db
   $ psql
   postgres=# alter database pubmed_test_db owner to parser;
   postgres=# \q
   $ exit
   $ psql -h localhost -d pubmed_test_db -U parser -f create_schema.sql
   $ python PubMedDB.py -d pubmed_test_db
   ```

1. Execute the `py.test` command
   (probably from the root folder, that is, where the `PubMedParser.py` is located).
