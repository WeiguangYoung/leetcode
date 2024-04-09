import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # 计算指定日期范围内的活动
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.Timedelta(days=29)

    filtered_df = activity[(activity['activity_date'] >= start_date) & (activity['activity_date'] <= end_date)]

    # 计算活跃用户数
    result = filtered_df.groupby('activity_date')['user_id'].nunique().reset_index()
    result.columns = ['day', 'active_users']
    return result
