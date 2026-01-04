import re

FORBIDDEN_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP", "ALTER",
    "TRUNCATE", "CREATE", "REPLACE", "ATTACH", "DETACH"
]

def is_safe_sql(query: str) -> bool:
    """
    Allows only SELECT queries.
    Blocks any write / schema modification operations.
    """
    if not query:
        return False

    query_upper = query.strip().upper()

    # Must start with SELECT
    if not query_upper.startswith("SELECT"):
        return False

    # Block forbidden keywords
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", query_upper):
            return False

    return True


def validate_sql_or_raise(query: str):
    """
    Raises exception if SQL is unsafe.
    """
    if not is_safe_sql(query):
        raise ValueError("Unsafe SQL query detected. Only SELECT queries are allowed.")
