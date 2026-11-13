-- Accuracy by annotator
SELECT annotator, AVG(correct) AS accuracy, COUNT(*) AS tasks
FROM annotation_qa
GROUP BY annotator
ORDER BY accuracy DESC;

-- Error rate by category
SELECT category, 1 - AVG(correct) AS error_rate, COUNT(*) AS tasks
FROM annotation_qa
GROUP BY category;

-- Duplicate check
SELECT task_id, COUNT(*) AS n
FROM annotation_qa
GROUP BY task_id
HAVING COUNT(*) > 1;
