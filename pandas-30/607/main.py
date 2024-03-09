import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_com = orders.merge(company, on="com_id")
    red_orders = order_com[order_com["name"] == "RED"]
    red_ids = red_orders.sales_id.unique()

    sales_person = sales_person[~sales_person["sales_id"].isin(red_ids)]

    return sales_person[["name"]]