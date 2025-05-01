# Host: localhost:3307  (Version 5.5.5-10.2.14-MariaDB)
# Date: 2025-02-27 07:48:29
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "clientes"
#

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `Id_cliente` bigint(20) NOT NULL AUTO_INCREMENT,
  `cliente` varchar(40) DEFAULT NULL,
  `Celular` varchar(20) DEFAULT NULL,
  `Domicilio` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`Id_cliente`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

#
# Data for table "clientes"
#

/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Adrian Eduardo','6623454245','Ernesto Dany #7'),(2,'Pepe segundo','6622222222','Ernesto Dany #9'),(3,'Carlos Gamez','6623321685','Ernesto Dany #11'),(10,'','','');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

#
# Structure for table "componentes"
#

DROP TABLE IF EXISTS `componentes`;
CREATE TABLE `componentes` (
  `id_componen` bigint(20) NOT NULL AUTO_INCREMENT,
  `componente` varchar(40) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `Disponible` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_componen`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

#
# Data for table "componentes"
#

/*!40000 ALTER TABLE `componentes` DISABLE KEYS */;
INSERT INTO `componentes` VALUES (1,'Intel Core i3-4150',5500,12),(2,'amd Radeon RX 560',2100,15),(3,'kingston fury ddr3 8gb',3700,10);
/*!40000 ALTER TABLE `componentes` ENABLE KEYS */;

#
# Structure for table "usuarios"
#

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `Id_usuario` bigint(20) NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(40) DEFAULT NULL,
  `Cuenta` varchar(20) DEFAULT NULL,
  `Clave` varchar(128) DEFAULT NULL,
  `nivel` int(11) DEFAULT NULL,
  `Idioma` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

#
# Data for table "usuarios"
#

/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Sadrach','admin','827ccb0eea8a706c4c34a16891f84e7b',1,1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

#
# Structure for table "ventas"
#

DROP TABLE IF EXISTS `ventas`;
CREATE TABLE `ventas` (
  `id_ventas` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_cliente` bigint(20) DEFAULT NULL,
  `id_componen` bigint(20) DEFAULT NULL,
  `Monto` decimal(10,0) DEFAULT NULL,
  `FechaHora` date DEFAULT NULL,
  PRIMARY KEY (`id_ventas`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

#
# Data for table "ventas"
#

/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,1,1,99,'2024-02-12'),(2,2,2,550,'2024-01-11'),(3,3,3,10000,'2023-12-29');
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
