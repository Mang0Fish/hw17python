--a
SELECT first_name, last_name, course_name from lecturers l LEFT JOIN courses c on l.lecturer_id = c.lecturer_id where c.course_name NOTNULL --b
--b
SELECT course_name from courses c WHERE c.lecturer_id ISNULL
--c
SELECT c.course_name, l.first_name, l.last_name from courses c left join lecturers l on c.lecturer_id = l.lecturer_id
--d
SELECT l.first_name, l.last_name, c.course_name from lecturers l inner join courses c USING (lecturer_id)
--e
SELECT l.first_name, l.last_name from lecturers l join courses c on l.lecturer_id = c.course_id where c.lecturer_id ISNULL
--f
SELECT l.first_name, l.last_name, c.course_name from lecturers l left join courses c on c.lecturer_id = l.lecturer_id
--g
SELECT c.course_name, l.first_name, l.last_name from courses c left join lecturers l using (lecturer_id) UNION ALL
SELECT l.first_name, l.last_name, c.course_name from lecturers l left join courses c using (lecturer_id)
--h
SELECT l.first_name, l.last_name, c.course_name from lecturers l join courses c

