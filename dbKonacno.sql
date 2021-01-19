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
    FOREIGN KEY (id_grad) REFERENCES grad(id),
	CONSTRAINT CHK_imeLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_kraticaLen CHECK ( length(kratica) >= 1 )
);

CREATE TABLE igrac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
	CONSTRAINT CHK_imeLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_prezimeLen CHECK ( length(prezime) >= 2 )
);

ALTER TABLE igrac ADD CONSTRAINT CHK_imeLen CHECK ( length(ime) >= 5 );
ALTER TABLE igrac ADD CONSTRAINT CHK_prezimeLen CHECK ( length(prezime) >= 3 );

CREATE TABLE trener(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
	CONSTRAINT CHK_imeLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_prezimeLen CHECK ( length(prezime) >= 2 )
);

CREATE TABLE sudac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
	CONSTRAINT CHK_imeLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_prezimeLen CHECK ( length(prezime) >= 2 )
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
    FOREIGN KEY (id_grad) REFERENCES grad(id),
	CONSTRAINT CHK_imeLen CHECK ( length(naziv) >= 2 )
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
    FOREIGN KEY (id_tim) REFERENCES tim(id),
    FOREIGN KEY (id_sesija) REFERENCES sesija(id)
);

CREATE TABLE gol(
	id_sesija INT NOT NULL,
    id_tim INT NOT NULL,
    id_igrac INT NOT NULL,
    vrijeme DATETIME NOT NULL,
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
    id_igrac INT NOT NULL, 
    ukupno INT DEFAULT 0,
    u_okvir INT DEFAULT 0,
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
    FOREIGN KEY (id_igrac) REFERENCES igrac(id)
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

INSERT INTO trener(id, ime, prezime, datum_rodenja, id_grad, id_tim) VALUES(7, "Trener", "Šajina", STR_TO_DATE('10.10.2000.', '%d.%m.%Y.'), 1, 2);
INSERT INTO trener(id, ime, prezime, datum_rodenja, id_grad, id_tim) VALUES(8, "Trener", "Valek", STR_TO_DATE('10.10.2000.', '%d.%m.%Y.'), 1, 1);

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

SELECT * FROM igrac;
DELETE FROM igrac WHERE id='8';





## TRIGGERI / PROCEDURE

DROP TRIGGER IF EXISTS  pazi_spec_znak_drzava;
DELIMITER //
CREATE TRIGGER pazi_spec_znak_drzava
	BEFORE INSERT ON drzava
	FOR EACH ROW
BEGIN

	IF new.ime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ime ne smije sadrzavati specijalne znakove';
	END IF;
    
END//
DELIMITER ;


SELECT * FROM drzava;

DROP TRIGGER IF EXISTS  pazi_spec_znak_grad;
DELIMITER //
CREATE TRIGGER pazi_spec_znak_grad
	BEFORE INSERT ON grad
	FOR EACH ROW
BEGIN

	IF new.ime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ime ne smije sadrzavati specijalne znakove';
	END IF;
    
END//
DELIMITER ;



DROP TRIGGER IF EXISTS  pazi_spec_znak_igrac;
DELIMITER //
CREATE TRIGGER pazi_spec_znak_igrac
	BEFORE INSERT ON igrac
	FOR EACH ROW
BEGIN

	IF new.ime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ime ne smije sadrzavati specijalne znakove';
	END IF;
    
    IF new.prezime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Prezime ne smije sadrzavati specijalne znakove';
	END IF;
    
END//
DELIMITER ;





DROP TRIGGER IF EXISTS  pazi_spec_znak_trener;
DELIMITER //
CREATE TRIGGER pazi_spec_znak_trener
	BEFORE INSERT ON trener
	FOR EACH ROW
BEGIN

	IF new.ime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ime ne smije sadrzavati specijalne znakove';
	END IF;
    
    IF new.prezime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Prezime ne smije sadrzavati specijalne znakove';
	END IF;
    
END//
DELIMITER ;





DROP TRIGGER IF EXISTS  pazi_spec_znak_sudac;
DELIMITER //
CREATE TRIGGER pazi_spec_znak_sudac
	BEFORE INSERT ON tim
	FOR EACH ROW
BEGIN

	IF new.ime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ime ne smije sadrzavati specijalne znakove';
	END IF;
    
	IF new.prezime REGEXP '^[!#$%&()*+,\-./:;<=>?@[\\\]^`{|}~]+$]' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Prezime ne smije sadrzavati specijalne znakove';
	END IF;
    
END//
DELIMITER ;





DROP TRIGGER IF EXISTS  datum_veci_igrac;
DELIMITER //
CREATE TRIGGER datum_veci_igrac
	BEFORE INSERT ON igrac
	FOR EACH ROW
BEGIN

	IF new.datum_rodenja >= CURDATE() THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Datum je veći od današnjeg';
	END IF;
    
END//
DELIMITER ;


DROP TRIGGER IF EXISTS  datum_veci_trener;
DELIMITER //
CREATE TRIGGER datum_veci_trener
	BEFORE INSERT ON trener
	FOR EACH ROW
BEGIN

	IF new.datum_rodenja >= CURDATE() THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Datum je veći od današnjeg';
	END IF;
    
END//
DELIMITER ;



DROP TRIGGER IF EXISTS  datum_veci_sudac;
DELIMITER //
CREATE TRIGGER datum_veci_sudac
	BEFORE INSERT ON sudac
	FOR EACH ROW
BEGIN

	IF new.datum_rodenja >= CURDATE() THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Datum je veći od današnjeg';
	END IF;
    
END//
DELIMITER ;


DROP TRIGGER IF EXISTS  out_nije_broj;
DELIMITER //
CREATE TRIGGER out_nije_broj
	BEFORE INSERT ON out_s
	FOR EACH ROW
BEGIN

	IF new.broj_outova LIKE '%[a-zA-Z][a-zA-Z]%' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Broj outova nije broj';
	END IF;
    
END//
DELIMITER ;




DROP TRIGGER IF EXISTS  stadion_kapacitet_gledatelja_nije_broj;
DELIMITER //
CREATE TRIGGER stadion_kapacitet_gledatelja_nije_broj
	BEFORE INSERT ON stadion
	FOR EACH ROW
BEGIN

	IF new.kapacitet_gledatelja LIKE '%[a-zA-Z][a-zA-Z]%' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Kapacitet nije broj';
	END IF;
    
END//
DELIMITER ;



DROP TRIGGER IF EXISTS  udarci_nije_broj;
DELIMITER //
CREATE TRIGGER udarci_nije_broj
	BEFORE INSERT ON udarci
	FOR EACH ROW
BEGIN

	IF new.ukupno LIKE '%[a-zA-Z][a-zA-Z]%' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Udarci nisu broj';
	END IF;
    
    IF new.u_okvir LIKE '%[a-zA-Z][a-zA-Z]%' THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Udarci nisu broj';
	END IF;
    
END//
DELIMITER ;

select * from udarci;


DROP TRIGGER IF EXISTS  golovi_vise_od_udaraca;
DELIMITER //
CREATE TRIGGER golovi_vise_od_udaraca
	BEFORE INSERT ON gol
	FOR EACH ROW
BEGIN

	DECLARE br_udaraca INT;
    DECLARE br_golova INT;
    
	SELECT broj_udaraca INTO br_udaraca
		FROM udarci;
        
	SELECT COUNT(*) INTO br_golova
    FROM gol
    WHERE id_sesija = new.id_sesija;

    
    IF br_udaraca = br_golova THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ne moze biti vise golova od udaraca';
	END IF;
    
END//
DELIMITER ;




DROP TRIGGER IF EXISTS  kraticeUpperPls;
DELIMITER //
CREATE TRIGGER kraticeUpperPls
	BEFORE INSERT ON tim
	FOR EACH ROW
BEGIN

	SET new.kratica = UPPER(kratica);
    
END//
DELIMITER ;



DROP TRIGGER IF EXISTS  crveniZuti;
DELIMITER //
CREATE TRIGGER crveniZuti
	BEFORE INSERT ON kazne
	FOR EACH ROW
BEGIN

	DECLARE br_zutih INT;
    
    SELECT COUNT(*) INTO br_zutih
		FROM kazne
        WHERE id_igrac = new.id_igrac AND id_sesija = new.id_sesija AND tip_kazne='žuti';
    
    if br_zutih >= 1 THEN
		SET new.tip_kazne = 'crveni';
    END IF;
    
    
END//
DELIMITER ;


-- Pripisuje odreden broj golova igracu u odredenoj sesiji --

DROP PROCEDURE IF EXISTS zabij_golove;
DELIMITER //
CREATE PROCEDURE zabij_golove(igra_id INTEGER,ses_id INTEGER,br_golova INTEGER)
BEGIN
    
   DECLARE id_tima INTEGER;
   DECLARE count INTEGER DEFAULT 0;
   
   SELECT id_tim INTO id_tima
	FROM igrac
    WHERE id = igra_id;
    
    WHILE count < br_golova DO
		
        INSERT INTO gol(id_sesija,id_tim,id_grac, vrijeme) VALUES(ses_id,id_tima, igra_id, NOW());
		
        SET count = count + 1;
    END WHILE;
   
END //
DELIMITER ;


SELECT * FROM sesija;

SELECT * FROM igrac;
SELECT * FROM grad;

INSERT INTO sudac VALUES(1, 'Alen', 'Sudac', '1999-12-1 12:00:00', 2);
INSERT INTO stadion VALUES(1,'Ze stadion',2000,1);
INSERT INTO sesija VALUES(1,1,2,1,1,'2020-12-1 12:00:00');

INSERT INTO gol VALUES(1,1,1,'2011-12-18 13:17:17');
INSERT INTO gol VALUES(1,2,4,'2011-12-18 13:17:30');



-- Izbacuje najboljeg igraca u utakmici u neku out varijablu --

DROP PROCEDURE IF EXISTS game_mvp;
DELIMITER //
CREATE PROCEDURE game_mvp(ses_id INTEGER, OUT rezultat INTEGER)
BEGIN
    
    DECLARE id_mvpa INTEGER;
    
    SELECT id_igrac INTO id_mvpa
		FROM gol
        WHERE id_sesija = 1
        GROUP BY id_igrac
        ORDER BY COUNT(id_igrac) DESC
        LIMIT 1;
        
    SET rezultat = id_mvpa;
    
END //
DELIMITER ;

CALL game_mvp(1, @rezultat);

SELECT @rezultat;


-- Izbacuje sve igrace koji su u nekoj sesiji zabili gol --

DROP PROCEDURE IF EXISTS dobi_zabijace 
DELIMITER //
CREATE PROCEDURE dobi_zabijace(IN id_sesije INT)
BEGIN

	DROP TEMPORARY TABLE IF EXISTS zabijaci;
    CREATE TEMPORARY TABLE zabijaci
	SELECT ime,prezime,vrijeme FROM gol g
	JOIN igrac i ON g.id_igrac = i.id
	WHERE g.id_sesija = id_sesije
    ORDER BY vrijeme DESC;
	
    SELECT * FROM zabijaci;
END //

DELIMITER ;
CALL dobi_zabijace(1);


SELECT * FROM trener;


-- Izbacuje trenere za svaki tim --

DROP PROCEDURE IF EXISTS dobi_trenere 
DELIMITER //
CREATE PROCEDURE dobi_trenere(IN id_sesije INT)
BEGIN

	DROP TEMPORARY TABLE IF EXISTS treneri;
    CREATE TEMPORARY TABLE treneri
	SELECT t.ime ime_tima,tr.ime ime_trenera,tr.prezime prezime_trenera FROM sesija s
		JOIN tim t ON t.id = s.id_tim1 OR t.id=s.id_tim2
		JOIN trener tr ON tr.id_tim = t.id
		WHERE s.id=id_sesije;
	
    SELECT * FROM treneri;
END //

DELIMITER ;
CALL dobi_trenere(1);


-- Izbacuje igrace za tim 1 i tim 2 --
DROP PROCEDURE IF EXISTS dobi_igrace;
DELIMITER //
CREATE PROCEDURE dobi_igrace(IN id_sesije INT)
BEGIN
	DROP TEMPORARY TABLE IF EXISTS tempIgraci;
    CREATE TEMPORARY TABLE tempIgraci
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac' FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = id_sesije
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac' FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = id_sesije;
	
    SELECT * FROM tempIgraci;
END //
DELIMITER ;

call dobi_igrace(1);


-- Izbacuje golove za sesiju --
DROP PROCEDURE IF EXISTS dobi_golove_u_sesiji;
DELIMITER //
CREATE PROCEDURE dobi_golove_u_sesiji(IN id_sesije INT)
BEGIN

	DROP TEMPORARY TABLE IF EXISTS tempGolovi;
    CREATE TEMPORARY TABLE tempGolovi
    
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', g.vrijeme FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
        JOIN gol g ON i.id = g.id_igrac
		WHERE s.id = id_sesije
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', g.vrijeme FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
        JOIN gol g ON i.id = g.id_igrac
		WHERE s.id = id_sesije;
        
    SELECT * FROM tempGolovi;
END //
DELIMITER ;

SELECT * FROM sudac;
SELECT * FROM drzava;
COMMIT;
DELETE FROM drzava WHERE id = 6;
call dobi_golove_u_sesiji(1);
DELETE FROM gol WHERE YEAR(vrijeme) = 2011;
SELECT * FROM gol;


-- Izbacuje prosjek godina svih igraca u sesiji --

DROP PROCEDURE IF EXISTS dobi_prosjecno_godina;
DELIMITER //
CREATE PROCEDURE dobi_prosjecno_godina(IN id_sesije INT)
BEGIN
	
	DECLARE sada INT DEFAULT YEAR(NOW());
    DECLARE prosjecna_godina INT;
    DECLARE prosjek INT;
    
    DROP TEMPORARY TABLE IF EXISTS tempIgraciGodine;
    CREATE TEMPORARY TABLE tempIgraciGodine
    
    SELECT i.datum_rodenja FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = 1
	UNION
	SELECT i.datum_rodenja FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = 1;
        
	SELECT AVG(YEAR(datum_rodenja)) FROM tempIgraciGodine INTO prosjecna_godina;
    
    SET prosjek = sada - prosjecna_godina;
    SELECT prosjek AS prosjek_godina_svih_igraca;
	
END //
DELIMITER ;

CALL dobi_prosjecno_godina(1);


-- Izbacuje prosjek godina svih igraca u sesiji zasebno za svaki tim --

DROP PROCEDURE IF EXISTS dobi_prosjecno_godina_Timovi;
DELIMITER //
CREATE PROCEDURE dobi_prosjecno_godina_Timovi(IN id_sesije INT)
BEGIN
	
	DECLARE sada INT DEFAULT YEAR(NOW());
    
    DECLARE prosjecna_godina_tim1 INT;
    DECLARE prosjecna_godina_tim2 INT;
    
    DECLARE prosjek_tim1 INT;
    DECLARE prosjek_tim2 INT;
    
    DROP TEMPORARY TABLE IF EXISTS tempIgraciGodineTim1;
    CREATE TEMPORARY TABLE tempIgraciGodineTim1
    
    SELECT i.datum_rodenja FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = 1;
        
	DROP TEMPORARY TABLE IF EXISTS tempIgraciGodineTim2;
    CREATE TEMPORARY TABLE tempIgraciGodineTim2
	SELECT i.datum_rodenja FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = 1;
        
	SELECT AVG(YEAR(datum_rodenja)) FROM tempIgraciGodineTim1 INTO prosjecna_godina_tim1;
	SELECT AVG(YEAR(datum_rodenja)) FROM tempIgraciGodineTim2 INTO prosjecna_godina_tim2;
    
    SET prosjek_tim1 = sada - prosjecna_godina_tim1;
    SET prosjek_tim2 = sada - prosjecna_godina_tim2;
	
    SELECT t.ime, prosjek_tim1 AS Tim_prosjek_godina
		FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
	UNION
    SELECT t.ime, prosjek_tim2 AS Tim_prosjek_godina
		FROM sesija s
		JOIN tim t ON t.id = s.id_tim2;
END //
DELIMITER ;

ALTER TABLE out_s ADD COLUMN id_igrac INT NOT NULL REFERENCES igrac(id);

SELECT broj_outova FROM out_s JOIN sesija s ON 2 = s.id AND id_tim = s.id_tim1;
SELECT broj_outova FROM out_s JOIN sesija s ON 1 = s.id AND id_tim = s.id_tim2;

CALL dobi_prosjecno_godina_Timovi(1);

SELECT * FROM udarci JOIN igrac i ON i.id = id_igrac WHERE id_sesija = 1;

SELECT * FROM out_s;

 SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', u.ukupno, u.u_okvir FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
        JOIN udarci u ON i.id = u.id_igrac
		WHERE s.id = 1
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', u.ukupno, u.u_okvir FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
        JOIN udarci u ON i.id = u.id_igrac
		WHERE s.id = 1;


## POGLEDI ## 

-- 1. view
DROP VIEW IF EXISTS teren_s_najvise_odigranih_utakmica;
CREATE VIEW teren_s_najvise_odigranih_utakmica AS
SELECT g.ime, stad.naziv, stad.kapacitet_gledatelja, COUNT(id_stadion) AS najvise_odigranih_utakmica
	FROM sesija AS ses
    INNER JOIN stadion AS stad ON stad.id = ses.id_stadion
    INNER JOIN grad AS g ON g.id = stad.id_grad
    GROUP BY id_stadion
    LIMIT 1;

SELECT * FROM teren_s_najvise_odigranih_utakmica;



-- 2. view
DROP VIEW s_koje_pozicije_ima_najvise_igraca_u_lizi;
CREATE VIEW s_koje_pozicije_ima_najvise_igraca_u_lizi AS
SELECT pozicija, COUNT(pozicija) AS broj_igraca_na_toj_poziciji
	FROM postava
    GROUP BY pozicija
    ORDER BY id_tim
    LIMIT 1;

SELECT * FROM s_koje_pozicije_ima_najvise_igraca_u_lizi;


-- 3. view
DROP VIEW IF EXISTS postignuti_pogodci_na_sesiji;
CREATE VIEW postignuti_pogodci_na_sesiji AS
SELECT i.ime, i.prezime, t.ime AS team, COUNT(id_igrac) AS broj_golova_na_utakmici
	FROM gol AS g
    INNER JOIN igrac AS i ON i.id = g.id_igrac
    INNER JOIN tim AS t ON t.id = i.id_tim
    WHERE id_sesija = 1
    GROUP BY id_igrac
    ORDER BY g.id_tim;
    
SELECT * FROM postignuti_pogodci_na_sesiji;



-- 4. view
DROP VIEW IF EXISTS rezultat_na_sesiji;
CREATE VIEW rezultat_na_sesiji AS
SELECT t.ime AS team, COUNT(id_igrac) AS broj_golova_na_utakmici
	FROM gol AS g
    INNER JOIN igrac AS i ON i.id = g.id_igrac
    INNER JOIN tim AS t ON t.id = i.id_tim
    WHERE id_sesija = 1
    GROUP BY t.ime
    ORDER BY g.id_tim;
    
SELECT * FROM rezultat_na_sesiji;

-- 5. view  
DROP VIEW IF EXISTS udarci_izvan_okvira_ekipe_koja_ima_vise_udaraca_u_jednoj_sesiji;
CREATE VIEW udarci_izvan_okvira_ekipe_koja_ima_vise_udaraca_u_jednoj_sesiji AS
SELECT ime, ukupno AS ukupan_broj_udaraca, u_okvir, 
		((SELECT ukupno FROM udarci AS u ORDER BY udar.id_tim ASC LIMIT 1) - 
		(SELECT u_okvir FROM udarci AS o ORDER BY udar.id_tim ASC LIMIT 1)) AS udarci_izvan_okvira
	FROM udarci AS udar
    INNER JOIN tim AS t ON t.id = udar.id_tim
    LIMIT 1;

SELECT * FROM udarci_izvan_okvira_ekipe_koja_ima_vise_udaraca_u_jednoj_sesiji;


-- 6. view
DROP VIEW IF EXISTS broj_outovi_manji_od_10;
CREATE VIEW broj_outovi_manji_od_10 AS
SELECT * 
FROM out_s AS os
LEFT JOIN tim AS t ON os.id_tim = t.id
WHERE id_sesija IN (SELECT id_sesija
FROM out_s AS os WHERE broj_outova < 10);

SELECT * FROM broj_outovi_manji_od_10;


-- 7, view
DROP VIEW IF EXISTS igrac_s_zutim_kartonom;
CREATE VIEW igrac_s_zutim_kartonom AS
SELECT i.ime, i.prezime, s.tip_kazne
FROM igrac AS i, kazne AS k
WHERE i.id = k.id_igrac
GROUP BY i.prezime
HAVING k.tip_kazne = 'zuti karton'
ORDER BY i.ime ASC;

SELECT * FROM igrac_s_zutim_kartonom;


## Naknadne funkcije
DROP FUNCTION IF EXISTS informacije_o_igracu;
DELIMITER //
CREATE FUNCTION informacije_o_igracu(id_trazenog_igraca INTEGER) RETURNS VARCHAR(200) 
DETERMINISTIC 
BEGIN 
DECLARE IME, PREZIME, GODISTE, TIM, BROJ_GOLOVA, BROJ_UTAKMICA, BROJ_KAZNI VARCHAR(20);
DECLARE INFO_IGRAC VARCHAR(200);

SELECT i.ime , i.prezime , EXTRACT( YEAR FROM i.datum_rodenja), t.ime FROM igrac AS i JOIN tim AS t 
ON i.id_tim=t.id
WHERE id_trazenog_igraca=i.id
INTO IME, PREZIME, GODISTE, TIM;

SELECT COUNT(*) FROM igrac AS i JOIN gol AS g
ON i.id=g.id_igrac
WHERE i.id=id_trazenog_igraca
INTO BROJ_GOLOVA
;

SELECT COUNT(*) FROM igrac AS i JOIN sesija AS s
ON i.id_tim=s.id_tim1 OR i.id_tim=s.id_tim2
WHERE i.id=id_trazenog_igraca
INTO BROJ_UTAKMICA ;

SELECT COUNT(*)  FROM kazne AS k JOIN igrac AS i 
ON i.id=k.id_igrac
WHERE i.id=id_trazenog_igraca
INTO BROJ_KAZNI;

SET INFO_IGRAC=CONCAT( 'IME: ',IME,'  -----  ',' PREZIME: ', PREZIME,'  -----  ',' GODISTE: ', GODISTE,'  -----  ',' TIM: ', TIM,'  -----  ',' BROJ_GOLOVA: ', BROJ_GOLOVA, '  -----  ',
 ' BROJ_ODIGRANIH_UTAKMICA: ',BROJ_UTAKMICA ,'  -----  ', ' BROJ_DOBIVENIH_KAZNI: ',BROJ_KAZNI);
RETURN INFO_IGRAC;
END//
DELIMITER ;

SELECT informacije_o_igracu(100) FROM DUAL;

SELECT * FROM igrac;
SELECT * FROM grad;
DELETE FROM igrac where id = 10;