SELECT 
  country,
  COUNT(DISTINCT user_id) AS active_users
FROM online_course_engagement
GROUP BY country
ORDER BY active_users DESC
LIMIT 10;
