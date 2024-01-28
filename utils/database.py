from pymongo import MongoClient
from . import constant
from typing import Dict, List

def get_total_records(table, filters):
    with MongoClient(host=constant.HOST, port=constant.PORT) as client:
        db = client[constant.DATABASE]
        total_records = db[table].count_documents(filters)
        return total_records

def fetch(table: str, filters: Dict = {}, limit: int = 0, skip: int = 0) -> List[Dict]:
    """
    Fetch data from MongoDB based on the provided table, filters, limit, and skip.

    Args:
        table (str): The name of the MongoDB collection.
        filters (Dict): The filters to be applied to the MongoDB query.
        limit (int): The maximum number of documents to be returned.
        skip (int): The number of documents to skip.

    Returns:
        List[Dict]: A list of documents matching the specified filters.
    """
    assert table, "Table not found"

    with MongoClient(host=constant.HOST, port=constant.PORT) as client:
        db = client[constant.DATABASE]
        rows = db[table].find(filters).limit(limit).skip(skip)
        return list(rows)

def insert(table: str, rows: List[Dict]):
    """
    Insert rows into MongoDB collection.

    Args:
        table (str): The name of the MongoDB collection.
        rows (List[Dict]): List of documents to be inserted.

    Returns:
        str: The result of the insert operation.
    """
    assert table, "Table not found"

    with MongoClient(host=constant.HOST, port=constant.PORT) as client:
        db = client[constant.DATABASE]
        results = db[table].insert_many(rows)
        return results.inserted_ids

# Example usage
# filters = {}
# table = constant.PRODUCT_TABLE
# query_result = fetch(table, filters, limit = 1, skip = 2)
# print(query_result)

# rows_to_insert = [
#     {"FirstName": "SS", "LastName": "Raj", "IsActive": True},
#     {"FirstName": "SS", "LastName": "Raj", "IsActive": True}
# ]

# insert_result = insert(constant.USER_TABLE, rows_to_insert)
# print(insert_result)