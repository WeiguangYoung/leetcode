SELECT
    Students.student_id, 
    Students.student_name,
    Subjects.subject_name, 
    IFNULL(exam_grouped.attended_exams, 0) AS attended_exams
FROM
    Students
CROSS JOIN
    Subjects
LEFT JOIN
    (
    SELECT 
        student_id, subject_name, COUNT(*) AS attended_exams
    FROM 
        Examinations
    GROUP BY 
        student_id, subject_name
    ) exam_grouped
ON 
    Subjects.subject_name = exam_grouped.subject_name
    AND
    Students.student_id = exam_grouped.student_id
ORDER BY
    Students.student_id, 
    Subjects.subject_name
;