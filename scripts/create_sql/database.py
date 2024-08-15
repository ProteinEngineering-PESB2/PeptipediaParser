"""Database functionalities module"""
# pylint: disable=not-callable
import os
import pandas as pd
from sqlalchemy import create_engine, text,select, func
from sqlalchemy.orm import Session
from table_models import *
from materialized_views import *
from table_models import Base as BaseTables
import networkx as nx
from networkx.readwrite import json_graph
from itertools import combinations
import os
from dotenv import load_dotenv


class Database:
    """Database class"""
    def __init__(self):
        # Config connection

        load_dotenv()
        user = os.getenv("DB_USER")
        db_name = os.getenv("DB_NAME")
        host = os.getenv("DB_HOST")
        password = os.getenv("DB_PASS")
        port = os.getenv("DB_PORT")
        self.engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
        )
        self.conn = self.engine.connect()
        # Config max items for selects
        self.session = Session(self.engine, future=True)
    
    def get_table(self, query):
        return pd.read_sql(text(query), con=self.conn)
    
    def get_table_query(self, stmt):
        """Applies a select for a previous stmt"""
        return pd.read_sql(stmt, con = self.conn)

    def insert_data(self, data_file, model, chunk):
        """Insert data from csv files"""
        tablename = model.__tablename__
        data = pd.read_csv(data_file, low_memory=False)
        data.to_sql(tablename,
            con = self.engine,
            if_exists = "append",
            method = "multi",
            chunksize = chunk,
            index = False,
            schema="public")
    def insert_big_data(self, data_file, model, chunk):
        """Insert data from csv files"""
        tablename = model.__tablename__
        header = pd.read_csv(data_file, nrows=1).columns
        for i in range(1, 200):
            data = pd.read_csv(data_file, low_memory=False, nrows=10**6, skiprows = i*10**6+2 + 104000000, header=None)
            data.columns = header
            print(data)
            #else:
            #    #data = pd.read_csv(data_file, low_memory=False, nrows=10**6)
            if len(data) > 0:
                data.to_sql(tablename,
                    con = self.engine,
                    if_exists = "append",
                    method = "multi",
                    chunksize = chunk,
                    index = False,
                    schema="public")
            else:
                break

    def create_tables(self):
        """Create tables from ddl"""
        BaseTables.metadata.create_all(self.engine)


if __name__ == "__main__":
    path_to_tables = "../../tables/"
    db = Database()
    db.create_tables()
    """db.insert_data(f"{path_to_tables}peptide.csv", Peptide, chunk=100)
    print("peptide")
    db.insert_data(f"{path_to_tables}source.csv", Source, chunk=100)
    print("source")
    db.insert_data(f"{path_to_tables}peptide_has_source.csv", PeptideHasSource, chunk=1000)
    print("peptide_has_source")
    db.insert_data(f"{path_to_tables}activity.csv", Activity, chunk=300)
    print("activity")
    db.insert_data(f"{path_to_tables}peptide_has_activity.csv", PeptideHasActivity, chunk=1000)
    print("peptide_has_activity")
    db.insert_data(f"{path_to_tables}pfam.csv", Pfam, chunk=1000)
    print("pfam")
    db.insert_data(f"{path_to_tables}peptide_has_pfam.csv", PeptideHasPfam, chunk=1000)
    print("peptide_has_pfam")
    db.insert_data(f"{path_to_tables}gene_ontology.csv", GeneOntology, chunk=1000)
    print("go")
    db.insert_data(f"{path_to_tables}peptide_has_go.csv", PeptideHasGO, chunk=1000)
    print("peptide_has_go")
    db.insert_data(f"{path_to_tables}predictive_model.csv", PredictiveModel, chunk=1000)
    print("predictive_model")"""