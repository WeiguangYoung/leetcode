import pandas as pd


def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    user_cnt = len(users)
    result = register.groupby("contest_id")["user_id"].apply(lambda x: round(
        x.count()*100/user_cnt, 2)).reset_index(name="percentage")
    result = result.sort_values(
        ["percentage", "contest_id"], ascending=[False, True])
    return result
