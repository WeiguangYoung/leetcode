import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    # 将日期转换为月份格式
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['country'] = transactions['country'].fillna('Unknown')

    # 分组并计算统计量
    result = transactions.groupby(['month', 'country']).agg(
        trans_count=('trans_date', 'count'),
        approved_count=('state', lambda x: (x == 'approved').sum()),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('amount', lambda x: x[transactions['state'] == 'approved'].sum())
    ).reset_index()
    
    # 将 "Unknown" 替换为 null
    result['country'] = result['country'].replace('Unknown', None)
    return result