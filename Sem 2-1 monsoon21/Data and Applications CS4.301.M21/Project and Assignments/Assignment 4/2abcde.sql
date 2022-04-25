-- create database test; use test; source "C:\SSDFiles\GitStuff\iiith\Sem 2-1 monsoon21\Data and Applications CS4.301.M21\Project and Assignments\Assignment 4\2abcde.sql"; drop database test;

-- SCHEMA -----------------------------------------------------------

CREATE TABLE INVINDEX
(
  WORD VARCHAR(200) NOT NULL,
  DOC_ID INT unsigned NOT NULL,
  FREQ INT NOT NULL
);

INSERT INTO INVINDEX (WORD, DOC_ID, FREQ) VALUES
  ('Hello', 4, 20),
  ('Hello', 41, 3),
  ('Marvel', 2, 4),
  ('World', 12, 9),
  ('Blackpi', 41, 5),
  ('Bonda', 12, 20),
  ('Hammer', 6, 9),
  ('Lotus', 2, 19);


CREATE TABLE ENTITY
(
  WORD1 VARCHAR(200) NOT NULL,
  WORD2 VARCHAR(200) NOT NULL,
  DOC_ID INT unsigned NOT NULL
);

INSERT INTO ENTITY (WORD1, WORD2, DOC_ID) VALUES
  ('Pizza', 'Italy', 5),
  ('Margher', 'Pizza', 21),
  ('Italy', 'Grammy', 8),
  ('Italy', 'Pasta', 5),
  ('Taylor', 'Singer', 8),
  ('Modi', 'Dancer', 13),
  ('Pasta', 'Orange', 4),
  ('Pasta', 'Pineapp', 5);


-- Problem A -----------------------------------------------------------

-- return the score of WORD w in DOC_ID d
DELIMITER $$
CREATE FUNCTION GetWordScore(w VARCHAR(200), d INT) RETURNS FLOAT(4) DETERMINISTIC
BEGIN
  DECLARE score FLOAT(4) DEFAULT 0.0;
  SELECT FREQ INTO score FROM INVINDEX WHERE WORD = w and DOC_ID = d;
  SELECT score/SUM(FREQ) INTO score FROM INVINDEX WHERE DOC_ID = d;
  RETURN score;
END $$
DELIMITER ;

SELECT DISTINCT DOC_ID, GetWordScore('Hello',DOC_ID)+GetWordScore('World', DOC_ID) as SCORE FROM INVINDEX WHERE GetWordScore('Hello',DOC_ID)+GetWordScore('World', DOC_ID) != 0;

-- Problem B -----------------------------------------------------------

CREATE VIEW ONE as
SELECT WORD1 as WORD11, WORD2 as WORD12, DOC_ID as DOCID1 FROM ENTITY WHERE WORD1 = 'Pizza';

CREATE VIEW TWO as
SELECT WORD12 as WORD21, WORD2 as WORD22, DOC_ID as DOCID2 
FROM ENTITY, ONE 
WHERE WORD1 = WORD12 and DOC_ID = DOCID1;

CREATE VIEW THREE as
SELECT WORD22 as WORD31, WORD2 as WORD32, DOC_ID as DOCID3 
FROM ENTITY, TWO 
WHERE WORD1 = WORD22 and DOC_ID = DOCID2;

SELECT WORD32 as 3HOP, DOCID3 as DOC_ID 
FROM THREE;

DROP VIEW ONE; DROP VIEW TWO; DROP VIEW THREE;

-- Problem C -----------------------------------------------------------

SELECT FREQ as 'FREQ of Lotus' 
FROM INVINDEX 
WHERE WORD = 'Lotus';

-- Problem D -----------------------------------------------------------

-- return the score of WORD w in DOC_ID d
DELIMITER $$
CREATE FUNCTION GetWordScore(w VARCHAR(200), d INT) RETURNS FLOAT(4) DETERMINISTIC
BEGIN
  DECLARE score FLOAT(4) DEFAULT 0.0;
  SELECT FREQ INTO score FROM INVINDEX WHERE WORD = w and DOC_ID = d;
  SELECT score/SUM(FREQ) INTO score FROM INVINDEX WHERE DOC_ID = d;
  RETURN score;
END $$
DELIMITER ;

SELECT WORD, AVG(GetWordScore(WORD, DOC_ID)) as AvgScore 
FROM INVINDEX 
GROUP BY WORD 
ORDER BY AvgScore DESC;

-- Problem E -----------------------------------------------------------

SELECT 'Cant believe the assignments are all done!' as '';