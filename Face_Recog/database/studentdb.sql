-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: student_details
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `attendancetable`
--

DROP TABLE IF EXISTS `attendancetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendancetable` (
  `ID` varchar(45) NOT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Department` varchar(45) DEFAULT NULL,
  `Time` varchar(45) DEFAULT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Attendance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendancetable`
--

LOCK TABLES `attendancetable` WRITE;
/*!40000 ALTER TABLE `attendancetable` DISABLE KEYS */;
/*!40000 ALTER TABLE `attendancetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Department` varchar(45) DEFAULT NULL,
  `Course` varchar(45) DEFAULT NULL,
  `Year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `Student_id` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `RollNo` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Teacher` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('Computer','BE','2021-22','Semester 7','1','APURV','G2','12','Male','11/06/2000','18comp.apurv.rathod@gmail.com','9428510585','Rajkot','Dipesh Sir','Yes'),('IT','BE','2021-22','Semester 7','2','SITA','G2','13','Female','21/05/2000','18comp.sita.sharma@gmail.com','9427510585','Surat','Dipesh Sir','Yes'),('Mechnical','BE','2021-22','Semester 1','3','SWAMI','G1','1','Male','12/01/2000','18comp.narendra.dutt@gmail.com','9427510585','Balur','Dipesh Sir','Yes'),('Computer','BE','2021-22','Semester 1','4','HETAV','G1','21','Male','21/03/2005','18comp.hetav.rathod@gmail.com','9427510585','Rajkot','Dipesh Sir','Yes');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-14 19:14:43
