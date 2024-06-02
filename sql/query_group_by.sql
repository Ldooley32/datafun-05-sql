--SQL query to count the books each author has in table

SELECT author_id, COUNT(*) AS books_count FROM books GROUP BY author_id;
