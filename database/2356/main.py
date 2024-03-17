import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby("teacher_id")["subject_id"].nunique().reset_index()
    return teacher.rename(columns={"subject_id": "cnt"})