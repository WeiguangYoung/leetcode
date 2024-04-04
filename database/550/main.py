import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_activity = activity.groupby(
        "player_id")["event_date"].min().reset_index()
    first_activity["event_date"] = first_activity["event_date"] + \
        pd.Timedelta(days=1)

    merge_activity = first_activity.merge(
        activity, how="inner", on=["player_id", "event_date"])
    fraction = round(len(merge_activity)/len(first_activity), 2)

    return pd.DataFrame({"fraction": [fraction]})
