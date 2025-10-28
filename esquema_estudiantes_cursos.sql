SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS;
SET @OLD_SQL_MODE = @@SQL_MODE;

-- Ajustar configuraciones para la creación del esquema
SET UNIQUE_CHECKS = 0;
SET FOREIGN_KEY_CHECKS = 0;
SET SQL_MODE = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,
                NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- ==========================================
-- ==========================================
DROP DATABASE IF EXISTS `esquema_estudiantes_cursos`;
CREATE DATABASE IF NOT EXISTS `esquema_estudiantes_cursos`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;

USE `esquema_estudiantes_cursos`;

-- ==========================================
-- ==========================================
DROP TABLE IF EXISTS `cursos`;

CREATE TABLE `cursos` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255),
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

-- ==========================================
-- ==========================================
DROP TABLE IF EXISTS `estudiantes`;

CREATE TABLE `estudiantes` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `edad` INT,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `curso_id` INT NOT NULL,
    INDEX (`curso_id`),
    CONSTRAINT `fk_estudiantes_cursos`
        FOREIGN KEY (`curso_id`)
        REFERENCES `cursos` (`id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_0900_ai_ci;

-- ==========================================
-- ==========================================
SET SQL_MODE = @OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;
