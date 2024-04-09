import pandas as pd

def biggest_single_number(number: pd.DataFrame) -> pd.DataFrame:
    counts = number.groupby('num').size()

    # 筛选出只出现一次的数字
    unique_nums = counts[counts == 1].index

    # 找出这些数字中的最大值
    max_unique_num = unique_nums.max()
    return pd.DataFrame({"num":[max_unique_num]})