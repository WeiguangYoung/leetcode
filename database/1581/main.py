import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    trans_visit_id = transactions["visit_id"].unique()
    no_trans_visits = visits[~visits["visit_id"].isin(trans_visit_id)]
    no_trans_visits = no_trans_visits.groupby(
        "customer_id").size().reset_index(name="count_no_trans")
    return no_trans_visits
