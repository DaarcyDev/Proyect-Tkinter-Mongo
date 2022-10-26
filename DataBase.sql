CREATE DATABASE IF NOT EXISTS tkinternotes;
use tkinternotes; 

CREATE TABLE usuarios(
    id       int(25) AUTO_INCREMENT NOT NULL,
    nombre   varchar(100),
    apellido varchar(255),
    email    varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    fecha    date NOT NULL,
    CONSTRAINT pk_usuarios PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE (email)
)   ENGINE=InnoDb;

CREATE TABLE notas(
    id           int(25) AUTO_INCREMENT NOT NULL,
    usuario_id   int(25) NOT NULL,
    titulo       varchar(255) NOT NULL,
    descripcion  MEDIUMTEXT,
    fecha    date NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) 
)   ENGINE=InnoDb; 