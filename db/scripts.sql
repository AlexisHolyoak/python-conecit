create database Usuarios;
CREATE TABLE `usuarios`.`usuarios` (
  `idUsuarios` INT NOT NULL,
  `Nombres` VARCHAR(45) NULL,
  `Usuario` VARCHAR(45) NULL,
  `Passw` VARCHAR(45) NULL,
  PRIMARY KEY (`idUsuarios`));
SELECT * FROM usuarios.usuarios;
ALTER TABLE `usuarios`.`usuarios` 
CHANGE COLUMN `Passw` `Passw` VARCHAR(415) NULL DEFAULT NULL;
ALTER TABLE `usuarios`.`usuarios` 
CHANGE COLUMN `idUsuarios` `idUsuarios` INT(11) NOT NULL AUTO_INCREMENT;
SELECT * FROM usuarios.usuarios;
INSERT INTO `usuarios`.`usuarios` (`Nombres`, `Usuario`, `Passw`) VALUES ('ALEXIS', 'holy', '35f319ca1dfc9689f5a33631c8f93ed7c3120ee7afa05b1672c7df7b71f63a6753def5fd3ac9db2eaf90ccab6bff31a486b51c7095ff958d228102b84efd7736');
SELECT * FROM usuarios.usuarios;
SELECT * FROM usuarios.usuarios;
UPDATE `usuarios`.`usuarios` SET `Passw`='b7988f752287de03b6b2ed737061573e5264cb56908d799593ddd3df5f00f54a1060793a3d212a949bb985a7c4e2a2c5e9051197593e465037b2538d4f6c0863' WHERE `idUsuarios`='1';
