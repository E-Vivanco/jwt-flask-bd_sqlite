-- Active: 1673006522058@@127.0.0.1@3306@bdwsmysql
CREATE TABLE users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NULL,
    first_lastname VARCHAR(50) NOT NULL,
    second_lastname VARCHAR(50) NULL,
    email VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL,
    rut VARCHAR(15) NOT NULL,
    password VARCHAR(120) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY(email),
    UNIQUE KEY (username),
    UNIQUE KEY (rut)
);

