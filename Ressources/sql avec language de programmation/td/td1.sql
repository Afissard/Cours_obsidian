/*
EMPLOYE : (nuempl,nomempl,hebdo,affect)
SERVICE : (nuserv,nomserv,chef)
PROJET : (nuproj,nomproj,resp)
TRAVAIL : (nuempl,nuproj,duree)
CONCERNE : (nuserv,nuproj)
*/

-- Reset
DROP TABLE concerne;
DROP TABLE travail;
DROP TABLE projet;
DROP TABLE employe;
DROP TABLE service;

-- Creation des tables
-- employe
CREATE table employe AS SELECT * FROM basetd.employe;
ALTER TABLE employe ADD CONSTRAINT PK_employe PRIMARY KEY (nuempl);
SELECT * from employe;

-- service
CREATE table service AS SELECT * FROM basetd.service;
ALTER TABLE service ADD CONSTRAINT PK_service PRIMARY KEY (nuserv);
SELECT * FROM service;

-- projet
CREATE table projet AS SELECT * FROM basetd.projet;
ALTER TABLE projet ADD CONSTRAINT PK_projet PRIMARY KEY (nuproj);
SELECT * FROM projet;

-- travail
CREATE table travail AS SELECT * FROM basetd.travail;
-- ALTER TABLE travail ADD CONSTRAINT PK_travail PRIMARY KEY (nuempl);
SELECT * FROM travail;

-- concerne
CREATE table concerne AS SELECT * FROM basetd.concerne;
-- ALTER TABLE concerne ADD CONSTRAINT PK_concerne PRIMARY KEY (nuserv);
SELECT * FROM concerne;


-- Ajout des clefs étranère
ALTER TABLE employe add CONSTRAINT FK_affect FOREIGN KEY (affect) REFERENCES service (nuserv);
