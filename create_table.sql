CREATE TABLE payments (
id SERIAL PRIMARY KEY,
 course_id INTEGER REFERENCES user_course(id) ON DELETE CASCADE,
 amount INTEGER,
 pay_date DATE
);

INSERT INTO payments (course_id, amount, pay_date)
VALUES 
((SELECT get_course_id_by_email('aman@mail.ru')), 15000, '15.08.2022'),
((SELECT get_course_id_by_email('aapina@bk.ru')), 55000, '05.08.2022'),
((SELECT get_course_id_by_email('spencer@microsoft.com')), 5000, '25.08.2022');
