import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    exam_grouped = examinations.groupby(
        ["student_id", "subject_name"]).size().reset_index(name="attended_exams")

    students_with_subs = students.merge(subjects, how="cross")
    results = students_with_subs.merge(exam_grouped, how="left")

    results['attended_exams'] = results['attended_exams'].fillna(0)

    results.sort_values(["student_id", "subject_name"], inplace=True)
    return results[["student_id", "student_name", "subject_name", "attended_exams"]]
