-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: atm
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `personal_data`
--

DROP TABLE IF EXISTS `personal_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_data` (
  `person_id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(100) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` varchar(14) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  PRIMARY KEY (`person_id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=607 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_data`
--

LOCK TABLES `personal_data` WRITE;
/*!40000 ALTER TABLE `personal_data` DISABLE KEYS */;
INSERT INTO `personal_data` VALUES (578,'DK0Q@11584','Latoya Spencer','1970-12-10','xufh.vuho@gmail.com','+8801838473303','Jeanine9'),(579,'j3Ndt6#316','Casey Leonard','1975-06-30','pskm@gmail.com','+8801645384741','Tabatha'),(580,'a8BSH1@922','Lakeisha Montes','1953-12-23','wdnl@gmail.com','+8801939877374','Clinton'),(581,'0EEOY@42428','Colleen Proctor','1995-02-04','pazii8@du.ac.bd','+8801905673741','Casey626'),(582,'2DG9#923','Alice Velazquez','1953-10-04','dcmrui34@gmail.com','+8801434571633','Alexis'),(583,'iL59#854','Bernard Wilkins','1982-08-02','kicqtx6@gmail.com','+8801735623977','Orlando'),(584,'DOMaJ@71553','Howard Randall','1972-01-06','monlt963@du.ac.bd','+8801635417017','Autumn'),(585,'GT2Z@816','Hector Dickson','1980-03-18','mrcf.njia@gmail.com','+8801791124759','Kendall'),(586,'6J8i#401','Vernon Rodgers','1962-09-24','juxl.nqrd@isrt.ac.bd','+8801816547754','Brad'),(587,'SvDP#160','Mike Finley','1997-09-24','hnguyso.qcbat@gmail.com','+8801858665549','Sharon4'),(588,'N23QJ1@52075','Marissa Escobar','1986-12-24','yyxh.xvbqyse@yahoo.com','+8801946727135','Ted5'),(589,'Jhsw#488','Ruby Robinson','1969-10-04','nmgy95@isrt.ac.bd','+8801508538647','Curtis'),(590,'5hPy65@296','Joni Larsen','1995-03-05','nvpf.hoqhb@yahoo.com','+8801537372113','Alissa3'),(591,'sip3@434','Duane Dickerson','1953-09-22','zkhdck83@isrt.ac.bd','+8801511184808','Terry860'),(592,'0VOX@6058','Harry Brennan','1951-09-02','wdune@isrt.ac.bd','+8801825745241','Cecil1'),(593,'WQXfT@0376','Luz Bass','1973-01-18','hwgh6@yahoo.com','+8801651548707','Marcella'),(594,'7n4W#415','Salvatore Morse','1995-06-05','hqzp5@gmail.com','+8801561381992','Janet895'),(595,'7Inm1#466','Byron Boone','1983-07-28','vfglw555@gmail.com','+8801586431616','Katina69'),(596,'bToy@376','Sammy Herring','2002-12-11','xuurr2@isrt.ac.bd','+8801867336167','Donald868'),(597,'Q5o2x7#224','Anthony Martin','1993-06-07','rkef371@isrt.ac.bd','+8801412608529','Stephen'),(604,'Ibrahim@970','Ibrahim All-Mamun','2000-12-24','mimamun@isrt.ac.bd','+8801581101890','Ibrahim@970'),(605,'trueWarrior1@','shohel','2001-06-05','shohels171@gmail.com','+8801777687299','shohel171'),(606,'ibraNaj@5822','Najmun Nahar','2001-10-30','najmunanahar302001@gmail.com','+8801794434223','nahar@970');
/*!40000 ALTER TABLE `personal_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-28 14:09:19
