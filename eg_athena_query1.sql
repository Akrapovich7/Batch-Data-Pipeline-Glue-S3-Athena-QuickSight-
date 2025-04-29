--1
SELECT 
  course_name,
  ROUND(AVG(duration_minutes), 2) AS avg_duration_minutes,
  COUNT(*) AS total_events
FROM online_course_engagement
GROUP BY course_name
ORDER BY avg_duration_minutes DESC
LIMIT 5;

