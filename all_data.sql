SELECT 
name, 
date_started, 
(SELECT name FROM user_student WHERE id = student_id) AS student_name,
(SELECT name FROM user_mentor WHERE id = mentor_id) AS mentor_name,
(SELECT name FROM user_language WHERE id = language_id) AS language_name
FROM user_course;