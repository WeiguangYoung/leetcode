import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 合并表以及重命名
    df = employee.merge(department, left_on='departmentId',
                        right_on='id', how='left')
    df.rename(columns={'name_x': 'Employee',
              'name_y': 'Department', 'salary': 'Salary'}, inplace=True)

    # 选择工资等于部门最高工资的员工
    max_salary = df.groupby("Department")["Salary"].transform("max")
    df = df[df["Salary"] == max_salary]

    return df[["Department", "Salary", "Employee"]]
