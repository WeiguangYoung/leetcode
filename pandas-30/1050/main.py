import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(
        ["actor_id", "director_id"]).size().reset_index(name="count")
    actor_director = actor_director[actor_director["count"] >= 3]
    actor_director.drop("count", axis=1, inplace=True)
    return actor_director
