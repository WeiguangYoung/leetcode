import pandas as pd


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["quality"] = queries["rating"] / queries["position"]
    queries["poor_query_percentage"] = queries["rating"].apply(
        lambda x: 1 if x < 3 else 0)
    grouped_queries = queries.groupby("query_name")
    grouped_queries = grouped_queries.agg({
        "quality": lambda x: round(x.mean(), 2),
        "poor_query_percentage": lambda x: round(x.sum()*100/x.count(), 2),
    }).reset_index()
    grouped_queries = grouped_queries[grouped_queries["query_name"].notnull()]
    return grouped_queries
