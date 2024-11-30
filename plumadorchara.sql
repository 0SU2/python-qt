-- -----------------------------------------------------
-- Base de datos y configuración inicial
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8;
USE `mydb`;

-- -----------------------------------------------------
-- Tabla Cargo
-- -----------------------------------------------------
CREATE TABLE `Cargo` (
  `idCargo` INT NOT NULL,
  `Descripcion` VARCHAR(500) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Sueldo_Base` DECIMAL(10,2) NOT NULL,
  `Horario_Entrada` TIME NOT NULL,
  `Horario_Salida` TIME NOT NULL,
  PRIMARY KEY (`idCargo`)
) ENGINE = InnoDB;

INSERT INTO `Cargo` VALUES
(1, 'Responsable de supervisión', 'Supervisor', 30000.00, '08:00:00', '17:00:00'),
(2, 'Encargado de desarrollo', 'Desarrollador', 45000.00, '09:00:00', '18:00:00');

-- -----------------------------------------------------
-- Tabla Departamento
-- -----------------------------------------------------
CREATE TABLE `Departamento` (
  `idDepartamento` INT NOT NULL,
  `Gerente` INT,
  `Descripcion` VARCHAR(500) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idDepartamento`)
) ENGINE = InnoDB;

INSERT INTO `Departamento` VALUES
(1, NULL, 'Desarrollo de software', 'TI'),
(2, NULL, 'Recursos Humanos', 'RH');

-- -----------------------------------------------------
-- Tabla Empleado
-- -----------------------------------------------------
CREATE TABLE `Empleado` (
  `idEmpleado` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Apellidos` VARCHAR(50) NOT NULL,
  `Num_telefono` VARCHAR(12) NOT NULL,
  `Puesto` INT NOT NULL,
  `Departamento` INT NOT NULL,
  `Tiempo_Activo` DECIMAL(5,2) NOT NULL,
  `Sueldo` DECIMAL(10,2) NOT NULL,
  `Activo` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  FOREIGN KEY (`Puesto`) REFERENCES `Cargo` (`idCargo`),
  FOREIGN KEY (`Departamento`) REFERENCES `Departamento` (`idDepartamento`)
) ENGINE = InnoDB;

INSERT INTO `Empleado` VALUES
(1, 'Juan', 'Pérez', '5551234567', 1, 1, 2.5, 32000.00, 1),
(2, 'Ana', 'López', '5559876543', 2, 2, 1.0, 47000.00, 1);

-- -----------------------------------------------------
-- Tabla Proveedor
-- -----------------------------------------------------
CREATE TABLE `Proveedor` (
  `idProveedor` INT NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Material` INT NOT NULL,
  PRIMARY KEY (`idProveedor`)
) ENGINE = InnoDB;

INSERT INTO `Proveedor` VALUES
(1, 'Proveedor A', 1),
(2, 'Proveedor B', 2);

-- -----------------------------------------------------
-- Tabla Materiales
-- -----------------------------------------------------
CREATE TABLE `Materiales` (
  `idMateriales` INT NOT NULL,
  `Proveedor` INT NOT NULL,
  `Existencia_almacen` INT NOT NULL,
  `Necesario_lote` DECIMAL(10,2) NOT NULL,
  `Registro_Compra` INT,
  PRIMARY KEY (`idMateriales`),
  FOREIGN KEY (`Proveedor`) REFERENCES `Proveedor` (`idProveedor`)
) ENGINE = InnoDB;

INSERT INTO `Materiales` VALUES
(1, 1, 100, 50.00, NULL),
(2, 2, 200, 30.00, NULL);

-- -----------------------------------------------------
-- Tabla Compra
-- -----------------------------------------------------
CREATE TABLE `Compra` (
  `idCompra` INT NOT NULL,
  `Proveedor` INT NOT NULL,
  `Cantidad` DECIMAL(10,2) NOT NULL,
  `Costo` DECIMAL(10,2) NOT NULL,
  `Producto` INT NOT NULL,
  PRIMARY KEY (`idCompra`),
  FOREIGN KEY (`Proveedor`) REFERENCES `Proveedor` (`idProveedor`),
  FOREIGN KEY (`Producto`) REFERENCES `Materiales` (`idMateriales`)
) ENGINE = InnoDB;

INSERT INTO `Compra` VALUES
(1, 1, 50, 15000.00, 1),
(2, 2, 30, 9000.00, 2);

-- -----------------------------------------------------
-- Tabla Lote
-- -----------------------------------------------------
CREATE TABLE `Lote` (
  `IdLote` INT NOT NULL,
  `Cantidad_Piezas` INT NOT NULL,
  `Fecha_lote` DATE NOT NULL,
  PRIMARY KEY (`IdLote`)
) ENGINE = InnoDB;

INSERT INTO `Lote` VALUES
(1, 500, '2024-11-01'),
(2, 300, '2024-11-10');

-- -----------------------------------------------------
-- Tabla Venta
-- -----------------------------------------------------
CREATE TABLE `Venta` (
  `idVenta` INT NOT NULL,
  `Cliente` INT NOT NULL,
  `Cantidad` INT NOT NULL,
  `Costo` DECIMAL(10,2) NOT NULL,
  `Fecha_venta` DATE NOT NULL,
  `Lotes_vendidos` INT NOT NULL,
  PRIMARY KEY (`idVenta`),
  FOREIGN KEY (`Lotes_vendidos`) REFERENCES `Lote` (`IdLote`)
) ENGINE = InnoDB;

INSERT INTO `Venta` VALUES
(1, 1, 100, 50000.00, '2024-11-15', 1),
(2, 2, 150, 75000.00, '2024-11-20', 2);

-- -----------------------------------------------------
-- Tabla Distribuidores
-- -----------------------------------------------------
CREATE TABLE `Distribuidores` (
  `idDistribuidores` INT NOT NULL,
  `Venta` INT NOT NULL,
  `Fecha_desde_cliente` DATE NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Num_Telefono` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idDistribuidores`),
  FOREIGN KEY (`Venta`) REFERENCES `Venta` (`idVenta`)
) ENGINE = InnoDB;

INSERT INTO `Distribuidores` VALUES
(1, 1, '2024-11-10', 'Distribuidor A', '5551112222'),
(2, 2, '2024-11-12', 'Distribuidor B', '5553334444');
