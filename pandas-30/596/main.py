import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby("class")["student"].count().reset_index()
    courses = courses[courses["student"] >= 5]
    courses.drop('student', axis=1, inplace=True)
    return courses
