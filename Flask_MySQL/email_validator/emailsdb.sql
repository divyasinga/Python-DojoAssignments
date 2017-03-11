-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


CREATE SCHEMA IF NOT EXISTS `friendsdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `emailssdb` ;


CREATE TABLE IF NOT EXISTS `emailsdb`.`emaillist` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_email` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB