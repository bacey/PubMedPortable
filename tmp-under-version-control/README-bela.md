conda create -n pubmedportable python=2

source activate pubmedportable

sudo apt install python-xapian
conda install sqlalchemy psycopg2 pytest

# https://github.com/KerstenDoering/PubMedPortable/issues/10
pip install xappy sqlalchemy==1.0.11


$ sudo su - postgres
$ createuser --interactive parser
Shall the new role be a superuser? (y/n) y
$ createdb import_using_pubmedportable
$ psql
postgres=# alter database import_using_pubmedportable owner to parser;
postgres=# alter user parser with password 'parser';
postgres=# \q

$ psql import_using_pubmedportable
import_using_pubmedportable=# \q

$ echo localhost:5432:import_using_pubmedportable:parser:parser >> ~/.pgpass
$ chmod 600 ~/.pgpass

psql -h localhost -d import_using_pubmedportable -U parser -f create_schema.sql

python PubMedDB.py -d import_using_pubmedportable

python PubMedParser.py -h
python PubMedParser.py -d import_using_pubmedportable -p 1 -i data-to-import/  # 1 process
python PubMedParser.py -d import_using_pubmedportable -p 4 -i data-to-import/  # 4 processes



sudo docker run -i -t -v /home/<user_name>/<folder_of_your_choice>/:/export/ -p 9998:5432 bgruening/pubmedportable /bin/bash"

sudo docker run -itv --rm bgruening/pubmedportable /bin/bash
