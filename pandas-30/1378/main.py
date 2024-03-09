import pandas as pd


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    employees = employees.merge(
        employee_uni,
        left_on="id",
        right_on="id",
        how="left",
    )
    employees.drop("id", axis=1, inplace=True)

    return employees
