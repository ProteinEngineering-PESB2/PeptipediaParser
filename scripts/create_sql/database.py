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
            
    def create_mv(self, model):
        definition = text(model().definition())
        refresh = text(model().refresh())
        self.session.execute(definition)
        self.session.commit()
        self.session.execute(refresh)
        self.session.commit()

    def create_tables(self):
        """Create tables from ddl"""
        BaseTables.metadata.create_all(self.engine)


if __name__ == "__main__":
    path_to_tables = "../../tables/"
    db = Database()
    db.create_tables()
    db.insert_data(f"{path_to_tables}peptide.csv", Peptide, chunk=100)
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
    print("predictive_model")
    db.create_mv(MVPeptidesByDatabase)
    db.create_mv(MVPeptidesByActivity)
    db.create_mv(MVGeneralInformation)
    db.create_mv(MVPeptideWithActivity)
    db.create_mv(MVPeptidesGeneralCounts)
    db.create_mv(MVLabeledPeptidesGeneralCounts)
    db.create_mv(MVSequencesByActivity)
    db.create_mv(MVSequencesBySource)
    db.create_mv(MVActivitiesListed)
    db.create_mv(MVSourcesListed)
    db.create_mv(MVPeptideProfile)
    db.create_mv(MVPeptideParams)
    db.create_mv(MVSearchPeptide)
    db.create_mv(MVChordFirstLevel)
    db.create_mv(MVPfamByPeptide)
    db.create_mv(MVGoByPeptide)
    db.create_mv(MVChordTherapeutic)
    db.create_mv(MVChordAMP)
    db.create_mv(MVPredictedPeptidesGeneralCounts)
    db.create_mv(MVPredictedSequencesByActivity)
    db.create_mv(MVChordFirstLevelPredicted)