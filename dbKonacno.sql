drop database projekt;
CREATE DATABASE projekt;
USE projekt;

CREATE TABLE drzava(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE grad(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL UNIQUE,
    id_drzava INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id)
);

CREATE TABLE tim(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL UNIQUE,
	kratica VARCHAR(5) NOT NULL,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
	CONSTRAINT CHK_imeTimLen CHECK ( length(ime) >= 2 ),
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
	CONSTRAINT CHK_imeIgracLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_prezimeIgracLen CHECK ( length(prezime) >= 2 )
);


CREATE TABLE trener(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
	CONSTRAINT CHK_imeTrenerLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_prezimeTrenerLen CHECK ( length(prezime) >= 2 )
);

CREATE TABLE sudac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_grad) REFERENCES grad(id),
	CONSTRAINT CHK_imeSudacLen CHECK ( length(ime) >= 2 ),
	CONSTRAINT CHK_prezimeSudacLen CHECK ( length(prezime) >= 2 )
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
	CONSTRAINT CHK_imeStadionLen CHECK ( length(naziv) >= 2 )
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
    id_igrac INT NOT NULL,
    id_tim INT NOT NULL,
    broj_outova INT DEFAULT 0,
    FOREIGN KEY (id_igrac) REFERENCES igrac(id),
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
("Italija"),
("Austrija"),
("Švicarska"),
("Crna Gora"),
("Kosovo"),
("Bosna i Hercegovina"),
("Portugal"),
("Rusija"),
("Mađarska"),
("Poljska"),
("Norveška"),
("Belgija"),
("Kanada"),
("Španjolska"),
("Grčka"),
("Turska"),
("Turkmenistan"),
("Afganistan"),
("Egipat"),
("Nigerija"),
("Engleska"),
("Izrael"),
("Monaco"),
("Finska"),
("Slovenija"),
("Japan"),
("Francuska");


INSERT INTO grad(ime, id_drzava) 
VALUES
("Zagreb", 1),
("Beograd", 2),
("Brasilia", 3),
("Berlin", 4),
("Rim", 5),
("Beč", 6),
("Bern", 7),
("Podgorica", 8),
("Priština", 9),
("Sarajevo", 10),
("Lisabon", 11),
("Moskva", 12),
("Budimpešta", 13),
("Varšava", 14),
("Oslo", 15),
("Bruixeulles", 16),
("Ottowa", 17),
("Madrid", 18),
("Atena", 19),
("Ankara", 20),
("Asgabat", 21),
("Kabul", 22),
("Cairo", 23),
("Abuja", 24),
("London", 25),
("Jeruzalem", 26),
("Monako", 27),
("Helsinki", 28),
("Ljubljana", 29),
("Tokyo", 30),
("Paris", 31);


INSERT INTO tim (ime, kratica, id_grad)VALUES
("Hajduk", "HAJ", 1),
("Crvena zvezda", "CRZ", 2),
("Brazil national footbal team", "BFT",3),
("Hertha BSC", "BSC", 4),
("A.S. Roma", "ASR", 5),
("FK Austria", "FKA", 6),
("BSC Bern", "BSC", 7),
("Bratstvo Cijevina", "BRC", 8),
("FC Priština", "FCP", 9),
("FK Sarajevo", "FKS", 10),
("Sporting CP", "SCP", 11),
("FC Moscow", "FCM", 12),
("FK Budapešt", "FKB", 13),
("Legia" , "LEG", 14),
("Lyn fotball", "LYF", 15),
("Anderlecht", "ANL", 16),
("Ottawa Fury", "OTF", 17),
("Real Madrid", "RMA", 18),
("AEK FC", "AEK", 19),
("Ankaraspor", "AKS", 20),
("FC Asgabat", "ASG", 21),
("Afganistan NFT", "AFG", 22),
("Wadi Degla", "WAD", 23),
("Abuja FC", "ABJ", 24),
("Arsenal FC", "ARS", 25),
("Beitar", "BEI", 26),
("AS Monaco", "MON", 27),
("HIFK", "HIF", 28),
("NK Olimpija", "OLI", 29),
("FC TOKYO", "TOK", 30),
("PSG FR", "PSG", 31);


INSERT INTO trener(ime, prezime, datum_rodenja, id_grad, id_tim) VALUES
("Jorge", "Jesus", STR_TO_DATE('09.10.1960.', '%d.%m.%Y.'), 1, 1),
("Ernesto", "Valverede", STR_TO_DATE('05.05.1965.', '%d.%m.%Y.'), 2, 2),
("Renato", "Gaucho", STR_TO_DATE('15.02.1971.', '%d.%m.%Y.'), 3, 3),
("Richard", "Ferretti", STR_TO_DATE('01.03.1965.', '%d.%m.%Y.'), 4, 4),
("Jose", "Bordalas", STR_TO_DATE('02.04.1964.', '%d.%m.%Y.'), 5, 5),
("Tiago", "Nunes", STR_TO_DATE('06.04.1963.', '%d.%m.%Y.'), 6, 6),
("Rui", "Vitoria", STR_TO_DATE('08.08.1967.', '%d.%m.%Y.'), 7, 7),
("Imanol", "Alguacil", STR_TO_DATE('14.10.1962.', '%d.%m.%Y.'), 8, 8),
("Jose", "Morais", STR_TO_DATE('16.05.1960.', '%d.%m.%Y.'), 9, 9),
("Paul", "Fonseca", STR_TO_DATE('13.11.1969.', '%d.%m.%Y.'), 10, 10),
("Bruno", "Lage", STR_TO_DATE('12.12.1968.', '%d.%m.%Y.'), 11, 11),
("Odair", "Hellmann", STR_TO_DATE('08.10.1964.', '%d.%m.%Y.'), 12, 12),
("Luiz", "Scolari", STR_TO_DATE('04.11.1972.', '%d.%m.%Y.'), 13, 13),
("Unai", "Emery", STR_TO_DATE('02.05.1964.', '%d.%m.%Y.'), 14, 14),
("Javi", "Calleja", STR_TO_DATE('19.10.1969.', '%d.%m.%Y.'), 15, 15);


INSERT INTO sudac(ime, prezime, datum_rodenja, id_grad) VALUES
("Frank", "Bleeckere", STR_TO_DATE('19.11.1975.', '%d.%m.%Y.'), 1),
("Oscar", "Ruiz", STR_TO_DATE('25.05.1975.', '%d.%m.%Y.'), 2),
("Pedro", "Proenca", STR_TO_DATE('15.02.1978.', '%d.%m.%Y.'), 3),
("Michel", "Vautrot", STR_TO_DATE('16.03.1969.', '%d.%m.%Y.'), 4),
("Peter", "Mikkelsen", STR_TO_DATE('12.05.1970.', '%d.%m.%Y.'), 5),
("Sandro", "Puhl", STR_TO_DATE('13.06.1975.', '%d.%m.%Y.'), 6),
("Kim", "Milton", STR_TO_DATE('18.08.1971.', '%d.%m.%Y.'), 7),
("Howard", "Webb", STR_TO_DATE('14.10.1970.', '%d.%m.%Y.'), 8),
("Markus", "Merk", STR_TO_DATE('20.06.1974.', '%d.%m.%Y.'), 9),
("Pier", "Collina", STR_TO_DATE('13.11.1969.', '%d.%m.%Y.'), 10),
("Yasmin", "Haidari", STR_TO_DATE('12.03.1971.', '%d.%m.%Y.'), 11),
("Jorgji", "Enea", STR_TO_DATE('18.10.1969.', '%d.%m.%Y.'), 12),
("Atman", "Lamia", STR_TO_DATE('02.11.1970.', '%d.%m.%Y.'), 13),
("Joao", "Goma", STR_TO_DATE('04.02.1968.', '%d.%m.%Y.'), 14),
("Helder", "Rodrigues", STR_TO_DATE('19.10.1969.', '%d.%m.%Y.'), 15),
("Tania", "Duarte", STR_TO_DATE('09.07.1970.', '%d.%m.%Y.'), 16),
("Iola", "Simmons", STR_TO_DATE('15.06.1971.', '%d.%m.%Y.'), 17),
("Mauro", "Vigliano", STR_TO_DATE('13.09.1973.', '%d.%m.%Y.'), 18),
("Fernando", "Rapallini", STR_TO_DATE('14.10.1970.', '%d.%m.%Y.'), 18),
("Nestor", "Pitana", STR_TO_DATE('24.12.1969.', '%d.%m.%Y.'), 19),
("Patricio", "Lousstau", STR_TO_DATE('26.01.1972.', '%d.%m.%Y.'), 20);


INSERT INTO igrac(ime, prezime, datum_rodenja, id_grad, id_tim) VALUES
("Cristiano ", "Ronaldo", STR_TO_DATE('09.10.1975.', '%d.%m.%Y.'), 1, 1),
("Lionel", "Messi", STR_TO_DATE('05.06.1978.', '%d.%m.%Y.'), 2, 2),
("Luis", "Suarez", STR_TO_DATE('15.04.1980.', '%d.%m.%Y.'), 3, 3),
("Manuel ", "Neuer", STR_TO_DATE('05.03.1985.', '%d.%m.%Y.'), 4, 4), 
("Robert", "Lewandowski", STR_TO_DATE('01.04.1974.', '%d.%m.%Y.'), 5, 5),
("Sergio ", "Ramos", STR_TO_DATE('06.12.1970.', '%d.%m.%Y.'), 6, 6),
("Eden ", "Hazard", STR_TO_DATE('05.11.1973.', '%d.%m.%Y.'), 7, 7),
("Toni ", "Kroos", STR_TO_DATE('14.01.1969.', '%d.%m.%Y.'), 8, 8),
("Gonzalo ", "Higuain", STR_TO_DATE('16.05.1990.', '%d.%m.%Y.'), 9, 9),
("Luka ", "Modric", STR_TO_DATE('13.03.1969.', '%d.%m.%Y.'), 10, 10),
("Gianluigi ", "Buffon ", STR_TO_DATE('14.06.1985.', '%d.%m.%Y.'), 11, 11), 
("Antoine  ", "Griezmann", STR_TO_DATE('08.06.1984.', '%d.%m.%Y.'), 12, 12),
("Jan  ", "Oblak", STR_TO_DATE('04.10.1982.', '%d.%m.%Y.'), 13, 13), 
("Zlatan ", "Ibrahimovic", STR_TO_DATE('02.08.1964.', '%d.%m.%Y.'), 14, 14),
("Edinson ", "Cavani", STR_TO_DATE('02.01.1965.', '%d.%m.%Y.'), 4, 15),
("Paul  ", "Pogba", STR_TO_DATE('07.01.1973.', '%d.%m.%Y.'), 11, 16),
("Romelu  ", "Lukaku", STR_TO_DATE('08.09.1976.', '%d.%m.%Y.'), 11, 17),
("Ivan  ", "Rakitic", STR_TO_DATE('14.11.1978.', '%d.%m.%Y.'), 10, 18),
("Franck  ", "Ribery", STR_TO_DATE('14.05.1985.', '%d.%m.%Y.'), 9, 19),
("Diego  ", "Costa", STR_TO_DATE('13.12.1991.', '%d.%m.%Y.'), 8, 20),
("Ivan ", "Perišić", STR_TO_DATE('02.12.1992.', '%d.%m.%Y.'), 8, 1),
("Domagoj ", "Vida", STR_TO_DATE('06.04.1993.', '%d.%m.%Y.'), 7, 1),
("Fernando   ", "Torres", STR_TO_DATE('08.08.1999.', '%d.%m.%Y.'), 7, 2),
("Xabi ", "Alonso", STR_TO_DATE('14.10.1985.', '%d.%m.%Y.'), 8, 1),
("Šime ", "Vresaljko", STR_TO_DATE('16.05.1967.', '%d.%m.%Y.'), 9, 2),
("Didier ", "Drogba", STR_TO_DATE('08.05.1971.', '%d.%m.%Y.'), 7, 1),
("Sergio ", "Busquets", STR_TO_DATE('14.11.1962.', '%d.%m.%Y.'), 8, 1),
("Dejan ", "Lovren", STR_TO_DATE('18.05.1987.', '%d.%m.%Y.'), 9, 1),
("Kylan", "Mbappe", STR_TO_DATE('17.06.1971.', '%d.%m.%Y.'), 15, 2),
("Ivan ", "Šaponjić", STR_TO_DATE('14.11.1991.', '%d.%m.%Y.'), 8, 2),
("Yannick ", "Carrasco", STR_TO_DATE('15.05.1977.', '%d.%m.%Y.'), 9, 3),
("Thomas ", "Lemar", STR_TO_DATE('08.06.1978.', '%d.%m.%Y.'), 7, 3),
("Kieran ", "Trippier", STR_TO_DATE('15.07.1962.', '%d.%m.%Y.'), 8, 3),
("Renan ", "Lodi", STR_TO_DATE('18.08.1999.', '%d.%m.%Y.'), 9, 3),
("Stefan", "Savić", STR_TO_DATE('17.12.1991.', '%d.%m.%Y.'), 15, 1),
("Federico", "Velverde", STR_TO_DATE('08.01.1998.', '%d.%m.%Y.'), 7, 1),
("Aleix ", "Vidal", STR_TO_DATE('14.04.1997.', '%d.%m.%Y.'), 8, 1),
("Nemanja ", "Gudelj", STR_TO_DATE('16.04.1997.', '%d.%m.%Y.'), 9, 1),
("Diego ", "Carlos", STR_TO_DATE('08.03.1996.', '%d.%m.%Y.'), 7, 1),
("Samuel ", "Umtiti", STR_TO_DATE('14.10.1995.', '%d.%m.%Y.'), 8, 2),
("Wilfred ", "Ndidi", STR_TO_DATE('18.04.1994.', '%d.%m.%Y.'), 9, 3),
("Demaray", "Gray", STR_TO_DATE('17.10.1993.', '%d.%m.%Y.'), 15, 3);

INSERT INTO stadion(naziv, kapacitet_gledatelja, id_grad) VALUES
("Maksimir", 50000, 1),
("Marakana", "70000", 2),
("Estadio Nacional Mane Garrincha", "70000", 3),
("Stadion An der Alten Forsterei", "22000", 4),
("Stadio Olimpico", "70000", 5),
("Generali Arena", "13000", 6),
("Stadion Neufeld", "14000", 7),
("Stadion Pod Goricom", "15000", 8),
("Fadil Vokrri Stadium", "13000", 9),
("Stadion Asim Ferhatović Hase", "37000", 10),
("Estadio Jose Alvalade", "50000", 11),
("Arena CSKA", "30000", 12),
("Stadion Hidegkuti Nandor", "5000", 13),
("Stadion Wojska Polskiego", "30000", 14),
("Stubberudmyra", "4000", 15),
("Stadion Edmond Machtens", "11000", 16),
("TD Place", "24000", 17),
("Stadion Santiago Bernabeu", "85000", 18),
("Olimpijski stadion u Ateni", "70000", 19),
("TCDD Ankara Demirspor Stadium", "3000", 20),
("Ashgabat Olympic Stadium", "1500", 21),
("Melat Stadium", "9000", 22),
("Stadion Petro Sport", "16000", 23),
("Old Parade Ground", "5000", 24),
("Emirates Stadium", "60000", 25),
("Jabna", "2500", 26),
("Stadion Louis II", "18000", 27),
("Stadion Sonera", "10000", 28),
("Stadion Stožice", "16000", 29),
("Stadion Ajinomoto", "50000", 30),
("Park Prinčeva", "48000", 31);



DROP PROCEDURE IF EXISTS pr_4;
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
DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET  f=1, br=1;
SET r='Igraci ';
SET r2='';

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

CALL pr_4(2,@rez,@r);
SELECT @r,@rez;
SELECT * FROM trener;

 
drop function IF EXISTS br_s;
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
	BEFORE INSERT ON sudac
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



DROP TRIGGER IF EXISTS  br_igraca_u_sesiji;
DELIMITER //
CREATE TRIGGER br_igraca_u_sesiji
	BEFORE INSERT ON sesija
	FOR EACH ROW
BEGIN

	DECLARE broj_igraca_u_timu1 INT;
    DECLARE broj_igraca_u_timu2 INT;
    
    SELECT COUNT(*) INTO broj_igraca_u_timu1
		FROM igrac i
		WHERE i.id_tim = new.id_tim1;
	
    SELECT COUNT(*) INTO broj_igraca_u_timu2
		FROM igrac i
		WHERE i.id_tim = new.id_tim2;

	IF NOT broj_igraca_u_timu1 >= 11 AND NOT broj_igraca_u_timu2 >=11  THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Broj igraca u timovima nije dovoljan za unijeti sesiju';
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
    
	SELECT ukupno INTO br_udaraca
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

-- Izbacuje najboljeg igraca u utakmici u neku out varijablu --

DROP PROCEDURE IF EXISTS game_mvp;
DELIMITER //
CREATE PROCEDURE game_mvp(ses_id INTEGER, OUT rezultat INTEGER)
BEGIN
    
    DECLARE id_mvpa INTEGER;
    
    SELECT id_igrac INTO id_mvpa
		FROM gol
        WHERE id_sesija = ses_id
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
		WHERE s.id = id_sesije
	UNION
	SELECT i.datum_rodenja FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = id_sesije;
        
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
		WHERE s.id = id_sesije;
        
	DROP TEMPORARY TABLE IF EXISTS tempIgraciGodineTim2;
    CREATE TEMPORARY TABLE tempIgraciGodineTim2
	SELECT i.datum_rodenja FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = id_sesije;
        
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

CALL dobi_prosjecno_godina_Timovi(1);



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
    ORDER BY najvise_odigranih_utakmica DESC
    LIMIT 1;

SELECT * FROM teren_s_najvise_odigranih_utakmica;



-- 2. view
DROP VIEW IF EXISTS s_koje_pozicije_ima_najvise_igraca_u_lizi;
CREATE VIEW s_koje_pozicije_ima_najvise_igraca_u_lizi AS
SELECT pozicija, COUNT(pozicija) AS broj_igraca_na_toj_poziciji
	FROM postava
    GROUP BY pozicija
    ORDER BY broj_igraca_na_toj_poziciji DESC
    LIMIT 1;
SELECT * FROM s_koje_pozicije_ima_najvise_igraca_u_lizi;


-- 3. view
DROP VIEW IF EXISTS postignuti_pogodci_na_sesiji;
CREATE VIEW postignuti_pogodci_na_sesiji AS
SELECT i.ime, i.prezime, COUNT(id_igrac) AS broj_golova_na_utakmici
	FROM gol AS g
    INNER JOIN igrac AS i ON i.id = g.id_igrac
    INNER JOIN tim AS t ON t.id = i.id_tim
    WHERE id_sesija = 1
    GROUP BY id_igrac
    ORDER BY broj_golova_na_utakmici DESC;
    
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
SELECT i.ime, i.prezime, k.tip_kazne
FROM igrac AS i, kazne AS k
WHERE i.id = k.id_igrac
GROUP BY i.prezime
HAVING k.tip_kazne = 'zuti'
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
