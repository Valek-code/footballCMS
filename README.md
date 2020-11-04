# Football CMS


## Upute
* Bitan je samo "mainFile.py" file iz ovog projekta⋅⋅
* Da bi radilo trebaju vam biblioteke iz lib foldera⋅⋅
* Biblioteke iz lib foldera nece raditi ako nemate dobro postavljen "virtual enviroment"
* [WIP]"projekt.sql" sadrzi kod za generiranje baze podataka, relacija i unos privremenih vrijednosti u iste (note: Nije konacan dizajn)
#


## Instalacija potrebnih biblioteka

Biblioteke koje se koriste:
* mysql-connector-python

Da bi instalirali potrebne biblioteke locirajte python terminal i upisite sljedecu liniju koda:
```shell
pip install mysql-connector-python
```

## Tablice

**Tablice nistu konacne ( keep that in mind )*

### Tim
| ID | ime | kratica | drzava_id | grad_id |
|----|-----|---------|-----------|---------|
|    |     |         |           |         |
|    |     |         |           |         |
|    |     |         |           |         |
|    |     |         |           |         |

### Drzava

| ID | ime_drzave |
|----|------------|
|    |            |
|    |            |
|    |            |
|    |            |

### Grad

| ID | ime_grada |
|----|-----------|
|    |           |
|    |           |
|    |           |
|    |           |

### Igrac

| ID | ime | prezime | datum_rodenja | drzava_id | grad_id | tim_id |
|----|-----|---------|---------------|-----------|---------|--------|
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |

### Trener

| ID | ime | prezime | datum_rodenja | drzava_id | grad_id | tim_id |
|----|-----|---------|---------------|-----------|---------|--------|
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |
|    |     |         |               |           |         |        |

### Sesija

| ID | tim_id - 1 | tim_id - 2 | pocetak | kraj | id_stadion |
|----|------------|------------|---------|------|------------|
|    |            |            |         |      |            |
|    |            |            |         |      |            |
|    |            |            |         |      |            |
|    |            |            |         |      |            |


### Statistika

| tim_id | rezultat | posjed lopte | out | sutevi | sutevi unutar okvira |
|--------|----------|--------------|-----|--------|----------------------|
|        |          |              |     |        |                      |
|        |          |              |     |        |                      |
|        |          |              |     |        |                      |
|        |          |              |     |        |                      |

### Zamjene

| igrac_id | tim_id |
|----------|--------|
|          |        |
|          |        |
|          |        |
|          |        |


### Statistika-zamjene

| id_sesija | igrac_id - 1 | igrac_id | tim_id |
|-----------|--------------|----------|--------|
|           |              |          |        |
|           |              |          |        |
|           |              |          |        |
|           |              |          |        |

### Statistika-kazne

| id_sesija | igrac_id | tip kazne(karton) | sudac_id |
|-----------|----------|-------------------|----------|
|           |          |                   |          |
|           |          |                   |          |
|           |          |                   |          |
|           |          |                   |          |

### Igrac-Tim-Postava

| id_igrac | id_tim | postava |
|----------|--------|---------|
|          |        |         |
|          |        |         |
|          |        |         |
|          |        |         |

### Stadion

| ID | naziv_stadiona | drzava_id | grad_id | kapacitet_gledatelja |
|----|----------------|-----------|---------|----------------------|
|    |                |           |         |                      |
|    |                |           |         |                      |
|    |                |           |         |                      |
|    |                |           |         |                      |


### Sudci

| ID | ime | prezime | datum_rodenja | drzava_id | grad_id |
|----|-----|---------|---------------|-----------|---------|
|    |     |         |               |           |         |
|    |     |         |               |           |         |
|    |     |         |               |           |         |
|    |     |         |               |           |         |


