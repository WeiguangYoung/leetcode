import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby("player_id")["event_date"].min().reset_index()
    activity = activity.rename({"event_date": "first_login"}, axis=1)
    return activity
