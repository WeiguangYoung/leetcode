import pandas as pd


def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    signups = signups.merge(confirmations, how="left", on="user_id")
    confirmation_rate = signups.groupby(
        "user_id")["action"].apply(lambda x: round((x == "confirmed").mean(), 2)).reset_index()
    confirmation_rate = confirmation_rate.rename(columns={
        "action": "confirmation_rate"
    })
    return confirmation_rate
