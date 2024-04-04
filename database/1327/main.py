import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders["month"] = orders["order_date"].dt.strftime('%Y-%m')
    results = orders[orders["month"] == "2020-02"]
    results = results.groupby(["product_id", "month"]).agg({
        "unit": "sum"
    }).reset_index()
    results = results[results["unit"] >= 100]

    results = results.merge(products)
    return results[["product_name", "unit"]]
