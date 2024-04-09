import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    followers_count = followers.groupby('user_id').size().reset_index(name='followers_count')

    # 按照 user_id 排序
    followers_count = followers_count.sort_values(by='user_id')

    return followers_count