-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 27-02-2025 a las 14:51:47
-- Versión del servidor: 5.7.21
-- Versión de PHP: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ensambladora`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `Id_cliente` bigint(20) NOT NULL AUTO_INCREMENT,
  `cliente` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Celular` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Domicilio` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `suspendido` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id_cliente`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`Id_cliente`, `cliente`, `Celular`, `Domicilio`, `suspendido`) VALUES
(1, 'Adrian Eduar', '66234542', 'Ernesto Dany ', 'N'),
(2, 'Pepe segundo', '6622222222', 'Ernesto Dany #9', 'N'),
(3, 'Carlos Gamez', '6623321685', 'Ernesto Dany #11', 'S');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `componentes`
--

DROP TABLE IF EXISTS `componentes`;
CREATE TABLE IF NOT EXISTS `componentes` (
  `id_componen` bigint(20) NOT NULL AUTO_INCREMENT,
  `componente` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `Disponible` int(11) DEFAULT NULL,
  `baja` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_componen`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `componentes`
--

INSERT INTO `componentes` (`id_componen`, `componente`, `precio`, `Disponible`, `baja`) VALUES
(1, 'Intel Core i3-4150', 5500, 12, 'N'),
(2, 'amd Radeon RX 560', 2100, 15, 'S'),
(3, 'kingston fury ddr3 8gb', 77, 10, 'S');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `Id_usuario` bigint(20) NOT NULL AUTO_INCREMENT,
  `Usuario` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Cuenta` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Clave` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nivel` int(11) DEFAULT NULL,
  `Idioma` int(11) DEFAULT NULL,
  `activo` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id_usuario`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Id_usuario`, `Usuario`, `Cuenta`, `Clave`, `nivel`, `Idioma`, `activo`) VALUES
(1, 'Sadrach', 'admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 1, 1, 'S'),
(33, '1', '2', 'c6f3ac57944a531490cd39902d0f777715fd005efac9a30622d5f5205e7f6894', 4, 1, 'S'),
(32, '1', '2', '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', 4, 5, 'S'),
(31, '2', '3', '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', 5, 6, 'S'),
(30, 'jperez', 'juan.perez', 'password', 1, 1, 'S');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

DROP TABLE IF EXISTS `ventas`;
CREATE TABLE IF NOT EXISTS `ventas` (
  `id_ventas` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_cliente` bigint(20) DEFAULT NULL,
  `id_componen` bigint(20) DEFAULT NULL,
  `Id_usuario` bigint(20) DEFAULT NULL,
  `Monto` decimal(65,30) DEFAULT NULL,
  `FechaHora` datetime(3) DEFAULT CURRENT_TIMESTAMP(3),
  `cancelado` char(1) COLLATE utf8mb4_unicode_ci DEFAULT 'N',
  PRIMARY KEY (`id_ventas`)
) ENGINE=MyISAM AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id_ventas`, `id_cliente`, `id_componen`, `Id_usuario`, `Monto`, `FechaHora`, `cancelado`) VALUES
(1, 1, 1, 1, '9.000000000000000000000000000000', '2024-02-12 00:00:00.000', 'N'),
(2, 2, 2, 1, '550.000000000000000000000000000000', '2024-01-11 00:00:00.000', 'N'),
(3, 3, 3, 1, '9999.000000000000000000000000000000', '2023-12-29 00:00:00.000', 'N'),
(44, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 22:03:42.820', 'S'),
(45, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:37.818', 'S'),
(46, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.094', 'S'),
(47, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.245', 'S'),
(48, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.393', 'S'),
(49, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.553', 'S'),
(50, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.696', 'S'),
(51, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.840', 'S'),
(52, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:38.982', 'S'),
(53, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:39.128', 'S'),
(54, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:39.288', 'S'),
(55, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:39.434', 'S'),
(56, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:39.594', 'S'),
(57, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:39.721', 'S'),
(58, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:39.882', 'S'),
(59, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.039', 'S'),
(60, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.183', 'S'),
(61, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.322', 'S'),
(62, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.483', 'S'),
(63, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.661', 'S'),
(64, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.822', 'S'),
(65, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:40.969', 'S'),
(66, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:41.112', 'S'),
(67, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:41.270', 'S'),
(68, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:41.413', 'S'),
(69, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:41.558', 'S'),
(70, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:41.720', 'S'),
(71, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:42.005', 'S'),
(72, 2, 3, 4, '5.000000000000000000000000000000', '2025-02-14 23:43:42.163', 'S'),
(73, 1, 1, 1, '1.000000000000000000000000000000', '2025-02-17 02:32:08.939', 'S'),
(74, 1, 2, 3, '100.500000000000000000000000000000', '2025-02-17 02:32:16.735', 'N');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
