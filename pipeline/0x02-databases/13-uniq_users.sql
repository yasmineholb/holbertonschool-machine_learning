-- SQL script that creates a table users

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users`(
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `email` CHAR(255) NOT NULL UNIQUE,
    `name` CHAR(255),
    PRIMARY KEY (`id`)
);