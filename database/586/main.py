import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby("customer_number")[
        "order_number"].size().reset_index(name="count")
    orders = orders.sort_values("count", ascending=False, inplace=True)
    return orders[["customer_number"]][:1]
