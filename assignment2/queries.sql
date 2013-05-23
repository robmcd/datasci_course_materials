SELECT
count(*)
FROM
Frequency f
WHERE
f.docid = '10398_txt_earn'
;

SELECT
count(*)
FROM
Frequency f
WHERE
-- πterm( σdocid=10398_txt_earn&count=1(frequency)) 
docid = '10398_txt_earn'
and count = 1
;

-- πterm( σdocid=10398_txt_earn&count=1(frequency)) U πterm( σdocid=925_txt_trade&count=1(frequency))
select count(*) from (
(SELECT
term
FROM
Frequency f
WHERE
docid = '10398_txt_earn'
and count = 1)
UNION
(SELECT
term
FROM
Frequency f
WHERE
docid = '925_txt_trade'
and count = 1)) a
;


SELECT
distinct docid
FROM
Frequency f
WHERE
f.term = 'parliament'
;


SELECT
docid, sum(count) num_terms
FROM
Frequency f
GROUP BY 
docid
HAVING
num_terms > 300
;

-- Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
SELECT
f1.docid, f1.term, f1.count, f2.docid, f2.term, f2.count
FROM
Frequency f1, Frequency f2
WHERE
f1.docid = f2.docid
and f1.term = 'transactions'
and f2.term = 'world'
;


-- matrix multiplication
SELECT A.row_number, B.column_number, SUM(A.value * B.value)
FROM A, B
WHERE A.column_number = B.row_number
GROUP BY A.row_number, B.column_number
;


SELECT 
A.docid, B.docid, SUM(A.count * B.count)
FROM 
Frequency A, Frequency B
WHERE 
A.term = B.term
and A.docid = '10080_txt_crude' and B.docid = '17035_txt_earn'
and A.docid < B.docid
GROUP BY 
A.docid, B.docid
;


CREATE VIEW frequency_query AS
SELECT * FROM Frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
;


SELECT 
A.docid, B.docid, SUM(A.count * B.count) similarity
FROM 
frequency_query A, frequency_query B
WHERE 
A.term = B.term
and A.docid = 'q'
and A.docid != B.docid
GROUP BY 
A.docid, B.docid
ORDER BY
similarity desc
LIMIT 0, 100
;

