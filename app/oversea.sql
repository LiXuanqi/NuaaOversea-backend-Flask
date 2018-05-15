# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.20)
# Database: oversea
# Generation Time: 2018-05-14 13:29:13 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table applicant
# ------------------------------------------------------------

DROP TABLE IF EXISTS `applicant`;

CREATE TABLE `applicant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `college` varchar(30) DEFAULT NULL,
  `major` varchar(30) DEFAULT NULL,
  `gpa` float(2,1) DEFAULT NULL,
  `language_type` enum('TOEFL','IELTS') DEFAULT NULL,
  `language_reading` int(11) DEFAULT NULL,
  `language_listening` int(11) DEFAULT NULL,
  `language_speaking` int(11) DEFAULT NULL,
  `language_writing` int(11) DEFAULT NULL,
  `gre_verbal` int(11) DEFAULT NULL,
  `gre_quantitative` int(11) DEFAULT NULL,
  `gre_writing` float(2,1) DEFAULT NULL,
  `research_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `recommendation_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `research_id` (`research_id`),
  KEY `project_id` (`project_id`),
  KEY `recommendation_id` (`recommendation_id`),
  CONSTRAINT `applicant_ibfk_1` FOREIGN KEY (`research_id`) REFERENCES `research` (`id`),
  CONSTRAINT `applicant_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `applicant_ibfk_3` FOREIGN KEY (`recommendation_id`) REFERENCES `recommendation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table application
# ------------------------------------------------------------

DROP TABLE IF EXISTS `application`;

CREATE TABLE `application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_id` int(11) NOT NULL,
  `university` varchar(64) DEFAULT NULL,
  `major` varchar(64) DEFAULT NULL,
  `degree` enum('Master','Ph.D') DEFAULT NULL,
  `term` varchar(64) DEFAULT NULL,
  `result` enum('ad','offer','rej') DEFAULT NULL,
  `applicant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  KEY `applicant_id` (`applicant_id`),
  CONSTRAINT `application_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`),
  CONSTRAINT `application_ibfk_2` FOREIGN KEY (`applicant_id`) REFERENCES `applicant` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table application_tag
# ------------------------------------------------------------

DROP TABLE IF EXISTS `application_tag`;

CREATE TABLE `application_tag` (
  `application_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`application_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `application_tag_ibfk_1` FOREIGN KEY (`application_id`) REFERENCES `application` (`id`),
  CONSTRAINT `application_tag_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table country
# ------------------------------------------------------------

DROP TABLE IF EXISTS `country`;

CREATE TABLE `country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_country_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;

INSERT INTO `country` (`id`, `name`)
VALUES
	(3,'加拿大'),
	(5,'德国'),
	(9,'新加坡'),
	(8,'日本'),
	(6,'法国'),
	(4,'澳大利亚'),
	(1,'美国'),
	(2,'英国'),
	(7,'香港');

/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table project
# ------------------------------------------------------------

DROP TABLE IF EXISTS `project`;

CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `value` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_project_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;

INSERT INTO `project` (`id`, `name`, `value`)
VALUES
	(1,'无相关实习经历，有个人项目',2),
	(2,'国内小公司实习',2),
	(3,'国内大公司实习',3),
	(4,'BAT实习',4),
	(5,'外企实习',5);

/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table recommendation
# ------------------------------------------------------------

DROP TABLE IF EXISTS `recommendation`;

CREATE TABLE `recommendation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `value` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_recommendation_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `recommendation` WRITE;
/*!40000 ALTER TABLE `recommendation` DISABLE KEYS */;

INSERT INTO `recommendation` (`id`, `name`, `value`)
VALUES
	(1,'无推荐信',1),
	(2,'国内普通推',2),
	(3,'海外普通推',3),
	(4,'国内牛推',4),
	(5,'海外牛推',5);

/*!40000 ALTER TABLE `recommendation` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table research
# ------------------------------------------------------------

DROP TABLE IF EXISTS `research`;

CREATE TABLE `research` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `value` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_research_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `research` WRITE;
/*!40000 ALTER TABLE `research` DISABLE KEYS */;

INSERT INTO `research` (`id`, `name`, `value`)
VALUES
	(1,'无科研经历',1),
	(2,'初步的科研经历',2),
	(3,'大学实验室做过较深入的研究',3),
	(4,'1~3个月的海外研究经历',4),
	(5,'大于3个月的海外研究经历',5);

/*!40000 ALTER TABLE `research` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table tag
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tag`;

CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tag_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;

INSERT INTO `tag` (`id`, `name`)
VALUES
	(1,'渣三维'),
	(2,'转专业'),
	(4,'高GPA'),
	(3,'高GT');

/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) NOT NULL,
  `password` varchar(250) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `role` enum('root','admin','stuff','student') DEFAULT NULL,
  `applicant_id` int(11) DEFAULT NULL,
  `login_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`),
  KEY `applicant_id` (`applicant_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`applicant_id`) REFERENCES `applicant` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
