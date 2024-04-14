import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle.apply(
        lambda x: "Yes" if x["x"]+x["y"] > x["z"] and x["x"] +
        x["z"] > x["y"] and x["z"]+x["y"] > x["x"] else "No",
        axis=1,
    )
    return triangle
