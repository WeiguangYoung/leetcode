import pandas as pd

# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     rs = pd.merge(customers, orders,left_on="id",right_on="customerId", how='left')
#     rs = rs[rs["customerId"].isna()]
#     rs = rs[["name"]].rename(columns={"name": "customers"})
#     return rs

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers["id"].isin(orders["customerId"])]
    df = df[["name"]].rename(columns={"name": "customers"})
    return df