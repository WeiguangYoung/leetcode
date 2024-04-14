import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # 然后筛选出只出现一次的 employee_id 对应的行
    single_employee_ids = employee['employee_id'].value_counts()[employee['employee_id'].value_counts() == 1].index
    
    result_df = employee[employee['primary_flag'] == 'Y' | employee['employee_id'].isin(single_employee_ids)]
    return result_df