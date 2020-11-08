CREATE DATABASE projekt;
USE projekt;


CREATE TABLE drzava(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL
);

CREATE TABLE grad(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL
);

CREATE TABLE tim(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime VARCHAR(100) NOT NULL,
	kratica VARCHAR(5) NOT NULL,
    id_drzava INT NOT NULL,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id),
    FOREIGN KEY (id_grad) REFERENCES grad(id)
);

CREATE TABLE igrac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_drzava INT NOT NULL,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id),
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

CREATE TABLE trener(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_drzava INT NOT NULL,
    id_grad INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id),
    FOREIGN KEY (id_grad) REFERENCES grad(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

CREATE TABLE sudac(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ime varchar(100) NOT NULL,
	prezime varchar(100) NOT NULL,
    datum_rodenja DATETIME,
    id_drzava INT NOT NULL,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id),
    FOREIGN KEY (id_grad) REFERENCES grad(id)
);

CREATE TABLE postava(   /* igrac u kojem timu i na kojem polozaju */ 
	id_igrac INT NOT NULL,
	id_tim INT NOT NULL,
    postava VARCHAR(25) NOT NULL,
    FOREIGN KEY (id_igrac) REFERENCES igrac(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

CREATE TABLE stadion(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	naziv VARCHAR(255) NOT NULL,
    kapacitet_gledatelja INT NOT NULL,
	id_drzava INT NOT NULL,
    id_grad INT NOT NULL,
    FOREIGN KEY (id_drzava) REFERENCES drzava(id),
    FOREIGN KEY (id_grad) REFERENCES grad(id)
);

CREATE TABLE sesija(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tim1_id INT NOT NULL,
    tim2_id INT NOT NULL,
    id_stadion INT NOT NULL,
    CONSTRAINT CHK_tim2 CHECK ( tim1_id != tim2_id ),
    FOREIGN KEY (tim1_id) REFERENCES tim(id),
    FOREIGN KEY (tim2_id) REFERENCES tim(id),
    FOREIGN KEY (id_stadion) REFERENCES stadio(id)
);

CREATE TABLE sudac_sesija(
	id_sesija INT NOT NULL,
	id_sudac INT NOT NULL,
    tip VARCHAR(25),
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_sudac) REFERENCES sudac(id)
);

CREATE TABLE statistika_opcenito(
	id_sesija INT NOT NULL,
	id_tim1 INT NOT NULL,
    id_tim2 INT NOT NULL,
    golovi_tim1 INT NOT NULL,
    golovi_tim2 INT NOT NULL,
    posjed_lopte_tim1 INT NOT NULL,
    posjed_lopte_tim2 INT NOT NULL,
    out_tim1 INT NOT NULL,
    out_tim2 INT NOT NULL,
    sutevi_ukupno_tim1 INT NOT NULL,
    sutevi_ukupno_tim2 INT NOT NULL,
    sutevi_okvir_tim1 INT NOT NULL,
    sutevi_okvir_tim2 INT NOT NULL,
	FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_tim1) REFERENCES tim(id),
    FOREIGN KEY (id_tim2) REFERENCES tim(id)
);

CREATE TABLE statistika_kazne(
	id_sesija INT NOT NULL,
	id_igrac INT NOT NULL,
	id_tim INT NOT NULL,
    id_sudac INT NOT NULL,
    tip_kazne VARCHAR(25),
    FOREIGN KEY (id_tim) REFERENCES tim(id),
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_igrac) REFERENCES igrac(id),
    FOREIGN KEY (id_sudac) REFERENCES sudac(id)
);

CREATE TABLE statistika_zamjene(
	id_sesija INT NOT NULL,
    id_igrac1 INT NOT NULL,
    id_igrac2 INT NOT NULL,
    id_tim INT NOT NULL,
    FOREIGN KEY (id_sesija) REFERENCES sesija(id),
    FOREIGN KEY (id_igrac1) REFERENCES igrac(id),
    FOREIGN KEY (id_igrac2) REFERENCES igrac(id),
    FOREIGN KEY (id_tim) REFERENCES tim(id)
);

INSERT INTO drzava(ime) 
VALUES
("Hrvatska"),
("Srbija"),
("Brazil"),
("Njemačka"),
("Francuska");

INSERT INTO grad(ime) 
VALUES
("Zagreb"),
("Beograd"),
("Brasilia"),
("Berlin"),
("Paris");

SELECT * FROM grad;
SELECT * FROM drzava;
SELECT * FROM tim;

INSERT INTO tim(ime, kratica, id_drzava, id_grad) 
VALUES
("Dinamo", "DZG", 1, 1),
("Crvena Zvezda", "CZV", 2, 2),
("Sport Club Mangueira", "SCM", 3,3),
("Bayern", "FCB",4,4),
("Paris Saint-Germain","PSG", 5,5);