import pandas as pd
from decimal import Decimal, ROUND_HALF_UP


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # 使用 left join 将员工表连接自身，以获取每个员工的下属数量和下属平均年龄
    merged_df = employees.merge(employees, how='left', left_on='employee_id',
                                right_on='reports_to', suffixes=('', '_report'))

    # 筛选出下属不为空的行
    merged_df = merged_df[merged_df['employee_id_report'].notnull()]

    # 计算每个员工的下属数量和下属平均年龄
    result_df = merged_df.groupby(['employee_id', 'name'])[['employee_id_report', 'age_report']].agg(
        {
            'employee_id_report': 'count',
            'age_report': lambda x: Decimal(x.mean()).quantize(0, rounding=ROUND_HALF_UP),
        }).reset_index()

    # 重命名列名
    result_df.columns = ['employee_id', 'name', 'reports_count', 'average_age']

    # 对结果按照员工ID进行排序
    result_df = result_df.sort_values(by='employee_id')
    return result_df
