select a.employee_id as 'employee_id', a.name as 'name', count(b.employee_id) as 'reports_count', round(avg(b.age), 0) as 'average_age'
from Employees a
    left join Employees b on a.employee_id = b.reports_to
where
    b.employee_id is not null
group by
    a.employee_id
order by a.employee_id;