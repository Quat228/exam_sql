SELECT 
(SELECT name FROM user_language WHERE id = (SELECT language_id FROM user_course WHERE id = course_id)) as language,
SUM(amount) AS sum_amount
FROM payments
GROUP BY language;