"""Data Ingestion Module."""

import logging

import pandas as pd
import pymongo


class DataIngestion:
    """Ingest data from MongoDB."""

    def __init__(self, mongo_uri: str, database_name: str, collection_name: str,) -> None:
        """Initialize the ingestion component."""

        self.mongo_uri = mongo_uri
        self.database_name = database_name
        self.collection_name = collection_name

    def read_data(self) -> pd.DataFrame:
        """Read data from MongoDB and return it as a DataFrame."""

        client = pymongo.MongoClient(self.mongo_uri)

        try:
            db = client[self.database_name]
            collection = db[self.collection_name]

            data = list(collection.find({}, {"_id": 0}))

            df = pd.DataFrame(data)

            logging.info("Data successfully retrieved from MongoDB.")
            logging.info("Dataset shape: %s", df.shape)

            return df

        except Exception as e:
            logging.exception("Error while reading data from MongoDB.")
            raise e

        finally:
            client.close()
