CREATE DATABASE `reserva_turno` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `dni` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `habilitado` tinyint NOT NULL,
  `fecha_creacion` date NOT NULL,
  `fecha_update` date NOT NULL,
  `direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `complejo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_complejo` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `cuil_cuit` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `cuil_cuit_UNIQUE` (`cuil_cuit`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `actividad_deportiva` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `cantidad_jugadores` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `complejo_actividad` (
  `id` int NOT NULL,
  `id_actividad` int NOT NULL,
  `id_complejo` int NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `id_complejo_idx` (`id_complejo`),
  KEY `id_actividad_idx` (`id_actividad`),
  CONSTRAINT `id_actividad` FOREIGN KEY (`id_actividad`) REFERENCES `actividad_deportiva` (`id`),
  CONSTRAINT `id_complejo` FOREIGN KEY (`id_complejo`) REFERENCES `complejo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `medio_pago` (
  `id` int NOT NULL,
  `entidad_bancaria` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `is_credito` tinyint NOT NULL,
  `cantidad_cuotas` int NOT NULL,
  `monto` int NOT NULL,
  `fecha_vencimiento` date NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `reserva` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_reserva` varchar(45) NOT NULL,
  `hora_inicio` date NOT NULL,
  `hora_fin` date NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `observaciones` varchar(45) DEFAULT NULL,
  `total` double NOT NULL,
  `estado_pago` varchar(45) NOT NULL,
  `id_mediopago` int NOT NULL,
  `id_usuario` int NOT NULL,
  `id_complejo` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `id_complejo_idx` (`id_complejo`),
  KEY `id_usuario_idx` (`id_usuario`),
  KEY `id_medio_pago_idx` (`id_mediopago`),
  CONSTRAINT `id_complejo_reserva` FOREIGN KEY (`id_complejo`) REFERENCES `complejo` (`id`),
  CONSTRAINT `id_medio_pago` FOREIGN KEY (`id_mediopago`) REFERENCES `medio_pago` (`id`),
  CONSTRAINT `id_usuario_reserva` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
