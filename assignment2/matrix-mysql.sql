CREATE TABLE a (
row_num int,
col_num int,
value int,
primary key (row_num, col_num));
INSERT INTO a VALUES(0,3,55);
INSERT INTO a VALUES(0,4,78);
INSERT INTO a VALUES(1,0,19);
INSERT INTO a VALUES(1,2,21);
INSERT INTO a VALUES(1,3,3);
INSERT INTO a VALUES(1,4,81);
INSERT INTO a VALUES(2,1,48);
INSERT INTO a VALUES(2,2,50);
INSERT INTO a VALUES(2,3,1);
INSERT INTO a VALUES(3,2,33);
INSERT INTO a VALUES(3,4,67);
INSERT INTO a VALUES(4,0,95);
INSERT INTO a VALUES(4,4,31);
CREATE TABLE b (
row_num int,
col_num int,
value int,
primary key (row_num, col_num));
INSERT INTO b VALUES(0,1,73);
INSERT INTO b VALUES(0,4,42);
INSERT INTO b VALUES(1,2,82);
INSERT INTO b VALUES(2,0,83);
INSERT INTO b VALUES(2,1,13);
INSERT INTO b VALUES(2,3,57);
INSERT INTO b VALUES(3,0,48);
INSERT INTO b VALUES(3,1,85);
INSERT INTO b VALUES(3,2,18);
INSERT INTO b VALUES(3,3,24);
INSERT INTO b VALUES(4,0,98);
INSERT INTO b VALUES(4,1,7);
INSERT INTO b VALUES(4,4,3);
COMMIT;