import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather2 = weather.copy(deep=True)
    weather2["recordDate"] = weather2["recordDate"]+pd.Timedelta(days=1)
    df = weather.merge(weather2, on="recordDate")
    df = df[df["temperature_x"] > df["temperature_y"]][["id_x"]]
    df = df.rename(columns={"id_x": "Id"})
    return df
