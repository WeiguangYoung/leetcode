import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    mng_cnt = employee.groupby("managerId").size().reset_index(name="count")
    mng_cnt = mng_cnt[mng_cnt["count"] >= 5]

    results = employee[employee["id"].isin(mng_cnt["managerId"])]
    return results[["name"]]