-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `Account_number` int NOT NULL AUTO_INCREMENT,
  `Account_name` varchar(50) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Balance` int NOT NULL,
  `Account_type` varchar(20) DEFAULT 'Saving',
  `Branch_code` int NOT NULL,
  PRIMARY KEY (`Account_number`)
) ENGINE=InnoDB AUTO_INCREMENT=9609371 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (2108301,'Veena Kumer','F','41, Model Town, Chennai - 148013',41415,'Saving',17992),(2108948,'Ghalib Sharad Sekhon','M','27, Model Town, Bhubhaneshwar - 255861',5520,'Saving',27769),(2110728,'Azhar Divan','M','38, Andheri, Gurgaon - 100213',1312031,'Saving',35269),(3713933,'Sid Sahil Sen','M','67, UrmilaGarh, Jaipur - 359987',0,'Saving',69282),(4509323,'Faraz Rao Khalsa','F','21, Sukriti Villas, Hadapsar Nashik - 580693',0,'Saving',17992),(5982769,'Mohanlal Singh Kunda','M','59, Juhi Nagar, Delhi - 243638',0,'Saving',69282),(6005245,'Deepesh Pratap Kumar','M','48, Yasmin Heights, Virar Mysore - 267864',0,'Saving',27769),(8387945,'Ragini Usman','F','46, Model Town, Bengaluru - 312030',0,'Saving',27769),(9609342,'Elias Parmer','M','46, Chinmay Villas, Andheri Ajmer - 294786',0,'Saving',27769),(9609367,'Ravi Ranjan Kumar Prajapati','M','Check Post, Piska Nagri, Ranchi',10000,'Saving',17992),(9609369,'Raj Ankit','M','Naro Bazaar',150,'Saving',17992);
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-22 21:50:18
