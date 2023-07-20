CREATE DATABASE datalake;

CREATE SCHEMA staging;

CREATE TABLE staging.tb_zona_sul (
  names varchar(255),
  price float,
  source varchar(255),
  dh_extraction timestamp
);