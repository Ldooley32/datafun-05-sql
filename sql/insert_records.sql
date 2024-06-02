--SQL query to insert an entry for author and book tables 

INSERT INTO authors (author_id, first, last) VALUES ('4dca0632-2c53-490c-99d5-4f6d41e56c0e', 'Jane', 'Austen'), ('0cc3c8e4-e0c0-482f-b2f7-af87330de214', 'Ray', 'Bradbury');
INSERT INTO books (Book_id, title, author_id) VALUES ('c6e67918-e509-4a6b-bc3a-979f6ad802f1', 'Emma', '4dca0632-2c53-490c-99d5-4f6d41e56c0e'), ('3a1d835c-1e15-4a48-8e8c-b12239604e99', 'All Summer in a Day', '0cc3c8e4-e0c0-482f-b2f7-af87330de214');
