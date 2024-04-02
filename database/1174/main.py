import pandas as pd


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    first_orders = delivery.groupby(
        "customer_id")['order_date'].min().reset_index()
    first_orders.rename(
        columns={'order_date': 'first_order_date'}, inplace=True)

    merged_df = pd.merge(delivery, first_orders, on="customer_id")
    # 根据条件过滤出即时订单
    immediate_orders = merged_df[(merged_df['order_date'] == merged_df['customer_pref_delivery_date']) &
                                 (merged_df['order_date'] == merged_df['first_order_date'])]

    # why not
    # immediate_orders = delivery[delivery.apply(lambda x: (x['customer_id'], x['order_date']) in first_orders.values, axis=1) & (
    #     delivery["order_date"] == delivery["customer_pref_delivery_date"])]

    # 计算即时订单在所有用户的首次订单中的比例
    immediate_percentage = round(
        len(immediate_orders) / len(first_orders) * 100, 2)

    return pd.DataFrame({"immediate_percentage": [immediate_percentage]})
