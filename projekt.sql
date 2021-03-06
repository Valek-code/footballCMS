drop database projekt;
CREATE DATABASE projekt;
USE projekt;

CREATE TABLE drzava(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL
);

CREATE TABLE grad(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL,
    id_drzava INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id)
);

CREATE TABLE tim(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL,
	kratica VARCHAR(5) NOT NULL,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id)
);

CREATE TABLE igrac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

CREATE TABLE trener(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

CREATE TABLE sudac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id)
);

CREATE TABLE postava(
	id_igrac INT NOT NULL,
	id_tim INT NOT NULL,
    pozicija VARCHAR(25) NOT NULL
);

CREATE TABLE stadion(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	naziv VARCHAR(255) NOT NULL,
    kapacitet_gledatelja INT NOT NULL,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id)
);

CREATE TABLE sesija(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_tim1 INT NOT NULL,
    id_tim2 INT NOT NULL,
    id_sudac INT NOT NULL,
    id_stadion INT NOT NULL,
    datum_sesija DATETIME,
    CONSTRAINT CHK_tim2 CHECK ( id_tim1 != id_tim2 ),
    FOREIGN KEY (id_tim1) REFERENCES tim(id),
    FOREIGN KEY (id_tim2) REFERENCES tim(id),
    FOREIGN KEY (id_sudac) REFERENCES sudac(id),
    FOREIGN KEY (id_stadion) REFERENCES stadion(id)
);

CREATE TABLE out_s( /* jer nemoze pisati OUT pa je out_s :D */
	id_sesija INT NOT NULL,
    id_tim INT NOT NULL,
    broj_outova INT DEFAULT 0,
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

CREATE TABLE gol(
	id_sesija INT NOT NULL,
    id_tim INT NOT NULL,
    id_igrac INT NOT NULL,
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
    FOREIGN KEY (id_igrac) REFERENCES igrac(id)
);

CREATE TABLE kazne(
	id_sesija INT NOT NULL,
    id_tim INT NOT NULL,
    id_igrac INT NOT NULL,
    tip_kazne VARCHAR(20),
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
    FOREIGN KEY (id_igrac) REFERENCES igrac(id)
);

CREATE TABLE udarci(
	id_sesija INT NOT NULL,
    id_tim INT NOT NULL,
    ukupno INT DEFAULT 0,
    u_okvir INT DEFAULT 0,
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);



INSERT INTO drzava(ime) 
VALUES
("Hrvatska"),
("Srbija"),
("Brazil"),
("Njemačka"),
("Francuska");

INSERT INTO grad(ime, id_drzava) 
VALUES
("Zagreb", 1),
("Beograd", 2),
("Brasilia", 3),
("Berlin", 4),
("Paris", 5);

SELECT * FROM grad;
SELECT * FROM drzava;
SELECT * FROM tim;
INSERT INTO tim(id, ime, kratica, id_grad) 
VALUES
(1,"Dinamo", "DZG", 1),
(2, "Crvena Zvezda", "CZV", 2),
(3, "Sport Club Mangueira", "SCM",3),
(4, "Bayern", "FCB",4),
(5, "Paris Saint-Germain","PSG", 5);

INSERT INTO igrac(id, ime, prezime, datum_rodenja, id_grad, id_tim) VALUES
(1, "Alen", "Valek", STR_TO_DATE('10.10.2000.', '%d.%m.%Y.'), 1, 1),
(2, "Maja", "Vrh", STR_TO_DATE('11.10.2000.', '%d.%m.%Y.'),  1, 1),
(3, "Matej", "Kurevija", STR_TO_DATE('12.10.2000.', '%d.%m.%Y.'), 2, 2),
(4, "Deni", "Vidan", STR_TO_DATE('14.10.2000.', '%d.%m.%Y.'), 2, 2),
(5, "Andrej", "Korica", STR_TO_DATE('15.10.2000.', '%d.%m.%Y.'), 3, 3),
(6, "Elena", "Ilic", STR_TO_DATE('18.10.2000.', '%d.%m.%Y.'), 4, 4),
(7, "David", "Sajina", STR_TO_DATE('19.10.2000.', '%d.%m.%Y.'), 4, 4);
INSERT INTO trener(id, ime, prezime, datum_rodenja, id_grad, id_tim) VALUES
(8, "Trener", "Valek", STR_TO_DATE('10.10.2000.', '%d.%m.%Y.'), 1, 1);

Select ime from igrac;

drop procedure pr_4;
DELIMITER //
CREATE PROCEDURE pr_4 (IN i_id INT, OUT r VARCHAR(700), OUT r2 VARCHAR(60))
BEGIN
DECLARE pomocni VARCHAR(50) DEFAULT '';
DECLARE pomocni2 VARCHAR(50) DEFAULT '';
DECLARE pomocni3 INT DEFAULT 0;
DECLARE pomocni4 VARCHAR(50) DEFAULT '';
DECLARE pomocni5 VARCHAR(50) DEFAULT '';
DECLARE pomocni6 INT DEFAULT 0;
DECLARE br INTEGER DEFAULT 0;
DECLARE f INTEGER DEFAULT 0;

DECLARE kursor CURSOR FOR
SELECT ime FROM igrac;
DECLARE kursor2 CURSOR FOR
SELECT prezime from igrac;
DECLARE kursor3 CURSOR FOR
SELECT id_tim from igrac;

DECLARE kursor4 CURSOR FOR
SELECT ime FROM trener;
DECLARE kursor5 CURSOR FOR
SELECT prezime from trener;
DECLARE kursor6 CURSOR FOR
SELECT id_tim from trener;
DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET  f=1;
SET r='Igraci';
SET r2=' ';

OPEN kursor4; OPEN kursor5; OPEN kursor6;
petlja: LOOP 
FETCH kursor4 INTO pomocni4;
FETCH kursor5 INTO pomocni5;
FETCH kursor6 INTO pomocni6;
IF br=1 THEN LEAVE petlja;
END IF;
IF i_id=pomocni6 THEN
SET r2 = CONCAT("Trener: ",pomocni4, " ", pomocni5), br=1;
END IF;
END LOOP petlja;
CLOSE kursor4; CLOSE kursor5; CLOSE kursor6;

OPEN kursor; OPEN kursor2; OPEN kursor3;
SET f=0;
petlja: LOOP 
FETCH kursor INTO pomocni;
FETCH kursor2 INTO pomocni2;
FETCH kursor3 INTO pomocni3;
IF f=1 THEN LEAVE petlja;
END IF;
IF (i_id=pomocni3) THEN
SET r = CONCAT(r, "; ", pomocni, " ", pomocni2);
END IF;
END LOOP petlja;
CLOSE kursor; CLOSE kursor2; CLOSE kursor3;
END//
DELIMITER ;

CALL pr_4(1,@rez,@r);
SELECT @r,@rez;
SELECT * FROM trener;
-- -- -- -- -- -- -- Ispisuje sve o igracima odabirom id tim -- -- -- -- -- -- --
SELECT i.id, i.ime, i.prezime, t.ime as tim, d.ime as drzava, g.ime as grad, tr.Ime as Ime_Trener, tr.prezime as Prez_Trener
 FROM igrac AS i LEFT JOIN tim AS t
 ON i.id_tim=t.id
 LEFT JOIN drzava as d ON i.id_drzava=d.id
 LEFT JOIN grad as g ON i.id_grad=g.id
 LEFT JOIN trener as tr ON tr.id_tim=t.id
 WHERE i.id_tim=1 /* umjesto 1 vanjska varijabla X */
 GROUP BY i.id;
 
 INSERT INTO sudac(ime, prezime, datum_rodenja, id_grad) VALUES('Alen','Valek',STR_TO_DATE('21/12/1999', '%d/%m/%Y'), 1);
 
 drop function br_s;
 DELIMITER //
 CREATE FUNCTION br_s (  p_id_sudac INT) RETURNS INT
DETERMINISTIC 
	BEGIN 
	DECLARE rez INT;
    
    SELECT COUNT(*) as broj_sudjenja INTO rez
 FROM sudac AS s LEFT JOIN sesija AS se
 ON s.id=se.id_sudac WHERE s.id=p_id_sudac;
    RETURN rez;
END //
DELIMITER ;
SELECT br_s(4);

SELECT * FROM tim;