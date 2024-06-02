--SQL query that will list the book titel with the author 

SELECT b.title, a.first, a.last
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id;
