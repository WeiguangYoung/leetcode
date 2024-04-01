import pandas as pd


def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    project_with_employee = project.merge(
        employee, how="left", on="employee_id")
    grouped_project = project_with_employee.groupby(
        "project_id")["experience_years"].apply(lambda x: round(x.mean(), 2)).reset_index(name="average_years")
    return grouped_project
