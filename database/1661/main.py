import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity['processing_time'] = activity.groupby(["machine_id", "process_id"])[
        'timestamp'].transform(lambda x: x.max() - x.min())
    machine_activity = activity.groupby(
        "machine_id")['processing_time'].mean().reset_index()
    machine_activity["processing_time"] = machine_activity["processing_time"].round(
        3)
    return machine_activity
