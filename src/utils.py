import pandas as pd
from conf import DATABASE_FILE


def load_database() -> pd.DataFrame:
    """
    reads database data
    """
    return pd.read_csv(DATABASE_FILE, index_col="Company Name")


def compare_data(source: dict, database: dict) -> dict:
    """
    compares values of 2 dicts
    """
    comparison = []
    all_fields = set(source.keys()).union(set(database.keys()))
    matches = 0
    for field in all_fields:
        file_value = source.get(field, None)
        db_value = database.get(field, None)
        match = file_value == db_value
        comparison.append({
            "field": field,
            "source": file_value,
            "database": db_value,
            "match": match
        })
        if match:
            matches += 1

    return {
        "matches": matches,
        "total": len(all_fields),
        "results": comparison
    }
