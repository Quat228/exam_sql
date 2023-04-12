CREATE FUNCTION get_course_id_by_email(student_email VARCHAR(30)) RETURNS INTEGER 
AS
$BODY$
	SELECT id
	FROM user_course
	WHERE student_id = (SELECT id FROM user_student WHERE email = student_email);
$BODY$
LANGUAGE SQL;

SELECT get_course_id_by_email('aman@mail.ru');
