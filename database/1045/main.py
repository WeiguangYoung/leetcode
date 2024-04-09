
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame: 
    # 找出所有客户购买过的产品
    customer_products = customer[customer['product_key'].isin(product['product_key'])]

    # 计算每个客户购买的不同产品数量
    customer_product_counts = customer_products.groupby('customer_id')['product_key'].nunique()

    # 计算产品表中产品的总数
    total_product_count = len(product)

    # 筛选出购买了所有产品的客户
    filtered_customers = customer_product_counts[customer_product_counts == total_product_count].index

    return pd.DataFrame({"customer_id":filtered_customers})