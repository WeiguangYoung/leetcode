import pandas as pd


def sales_analysis(product_df: pd.DataFrame, sales_df: pd.DataFrame) -> pd.DataFrame:
    # 通过左连接获取产品名称
    result_df = pd.merge(sales_df, product_df, on='product_id', how='left')

    # 按产品分组并应用筛选条件
    result_df = result_df.groupby('product_id').filter(
        lambda x: len(x[(x['sale_date'] >= '2019-01-01') & (x['sale_date'] <= '2019-03-31')]) == len(x))

    # 删除重复的产品行
    result_df = result_df.drop_duplicates(subset='product_id')

    return result_df[["product_id","product_name"]]
