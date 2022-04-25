-- create database test; use test; source "C:\SSDFiles\GitStuff\iiith\Sem 2-1 monsoon21\Data and Applications CS4.301.M21\Project and Assignments\Assignment 4\1abcdef.sql"; drop database test;

-- SCHEMA -------------------------------------
CREATE TABLE POINT
(
  X INT NOT NULL,
  Y INT NOT NULL,
  Z INT NOT NULL
);

INSERT INTO POINT 
VALUES
  (1, 1, 0),
  (-3, 0, 0),
  (1, -2, 3);

-- PROBLEM A -------------------------------------

-- default sorting is in ascending order
SELECT * 
FROM POINT
ORDER BY X, Y, Z; 

-- PROBLEM B -------------------------------------
-- maximum elevation
SELECT * 
FROM POINT
WHERE Z=(SELECT max(Z) FROM POINT);

-- minimum elevation
SELECT * 
FROM POINT
WHERE Z=(SELECT min(Z) FROM POINT);

-- PROBLEM C -------------------------------------
SELECT X,Y,Z
FROM 
(
  SELECT X,Y,Z,
  X*X+Y*Y+Z*Z as EUDIST
  FROM POINT
  ORDER BY EUDIST
) AS dist
LIMIT k;

-- PROBLEM D -------------------------------------

SELECT AVG(X) AS CentroidX, AVG(Y) AS CentroidY, AVG(Z) AS CentroidZ
FROM POINT;

-- PROBLEM E -------------------------------------
-- SET @a := alpha;
SET @a := 1.57;

CREATE TABLE ROTATE (col1 FLOAT, col2 FLOAT, col3 FLOAT);

INSERT INTO ROTATE VALUES
  (cos(@a), -sin(@a), 0),
  (sin(@a), cos(@a), 0),
  (0, 0, 1);

SELECT * FROM ROTATE;

-- PROBLEM F -------------------------------------

CREATE TABLE ROTATED (X FLOAT, Y FLOAT, Z FLOAT);

CREATE VIEW ROT AS
SELECT col1, col2, col3, ROW_NUMBER() OVER() as r FROM ROTATE;

DELIMITER $$
CREATE FUNCTION GetRotatedPoint(px FLOAT, py FLOAT ,pz FLOAT, ro INT) RETURNS FLOAT(4) DETERMINISTIC
BEGIN
  DECLARE rot FLOAT(4) DEFAULT 0.0;
  SELECT px * R.col1 + py * R.col2 + pz * R.col3 INTO rot FROM ROT AS R WHERE R.r = ro;
  RETURN rot;
END $$
DELIMITER ;

INSERT INTO ROTATED
SELECT GetRotatedPoint(p.X, p.Y, p.Z, 1), GetRotatedPoint(p.X, p.Y, p.Z, 2), GetRotatedPoint(p.X, p.Y, p.Z, 3) FROM POINT as p;

DROP VIEW ROT;

SELECT * FROM ROTATED;