import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(prices, units_sold, how="left", on="product_id")
    df = df[(df["purchase_date"] >= df["start_date"])
            & (df["purchase_date"] <= df["end_date"])]
    df["sales"] = df["price"] * df["units"]

    result = df.groupby("product_id").agg(
        {"sales": "sum", "units": "sum"}).fillna(0).reset_index()
    result["average_price"] = round(result["sales"]/result["units"], 2)

    no_sales_product = prices[~prices["product_id"].isin(
        result["product_id"])].copy()
    no_sales_product["average_price"] = 0

    result = pd.concat([result, no_sales_product])

    return result[["product_id", "average_price"]].sort_values("product_id").reset_index(drop=True)