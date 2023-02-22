-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: fly_fishing_store_info
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
-- Table structure for table `cart_items`
--

DROP TABLE IF EXISTS `cart_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_items` (
  `cart_id` varchar(50) NOT NULL,
  `quantity` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `shopping_cart_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `product_id` (`product_id`),
  KEY `shopping_cart_id` (`shopping_cart_id`),
  CONSTRAINT `cart_items_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `cart_items_ibfk_2` FOREIGN KEY (`shopping_cart_id`) REFERENCES `shopping_carts` (`shopping_cart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_items`
--

LOCK TABLES `cart_items` WRITE;
/*!40000 ALTER TABLE `cart_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customer_id` varchar(50) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('2dc74860-cd56-4f51-aab8-b546b082bd71','Milenko','Milenkovic','771ee659-9b4f-4cc5-ad3d-7e3c32e4f16f'),('7ae62936-7651-4113-aea5-a6b583372017','Mile','Milic','8a8c9002-f3d1-41f2-9e03-3aaa82047ef4'),('ba3908ef-8e1a-4b5f-83e1-42215ce399c5','Milenko','Milenkovic','771ee659-9b4f-4cc5-ad3d-7e3c32e4f16f');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_type`
--

DROP TABLE IF EXISTS `employee_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_type` (
  `employee_type_id` varchar(50) NOT NULL,
  `employee_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`employee_type_id`),
  UNIQUE KEY `employee_type` (`employee_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_type`
--

LOCK TABLES `employee_type` WRITE;
/*!40000 ALTER TABLE `employee_type` DISABLE KEYS */;
INSERT INTO `employee_type` VALUES ('f164e2fe-c066-44db-9578-cace2841ab99','menadzer'),('e2c7cf90-4247-41d6-8a08-e40778a07a98','prodavac'),('839b319a-d7b5-4b92-bbec-dc301dd0470f','tester');
/*!40000 ALTER TABLE `employee_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` varchar(50) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `employee_type_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `employee_type_id` (`employee_type_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`employee_type_id`) REFERENCES `employee_type` (`employee_type_id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES ('57a40d2a-63da-4272-9158-5a99754092a1','Milos','Cvijovic','f164e2fe-c066-44db-9578-cace2841ab99','2869660c-e085-4f2d-aa22-2900028c5985'),('c1bfbec0-a4e0-4f3d-8f9f-89f177f6bee2','Ljubisa','Ljubisic','839b319a-d7b5-4b92-bbec-dc301dd0470f','2a1725cf-3c5f-4544-b22a-c1afe90f4089'),('d07793c6-bbbc-458a-9460-f062879ef1b8','Miodrag','Miodragovic','e2c7cf90-4247-41d6-8a08-e40778a07a98','3a8a783f-1a59-499c-a31b-c7e4542aee65');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flies`
--

DROP TABLE IF EXISTS `flies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flies` (
  `fly_id` varchar(50) NOT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `in_stock` tinyint(1) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `product_type_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fly_id`),
  KEY `product_id` (`product_id`),
  KEY `product_type_id` (`product_type_id`),
  CONSTRAINT `flies_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `flies_ibfk_2` FOREIGN KEY (`product_type_id`) REFERENCES `product_types` (`product_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flies`
--

LOCK TABLES `flies` WRITE;
/*!40000 ALTER TABLE `flies` DISABLE KEYS */;
INSERT INTO `flies` VALUES ('5d0bb228-eb91-4b03-b1f2-a174e4a93fa9','Tigofly','brown-olive flyy',5,4,5,200,'Flies for trout',1,'14263cbe-555c-499d-8ad7-5f2f28a630c7','be137d9b-a56d-4a72-8855-748a0052aa15'),('63932d37-3e04-4259-bd3a-10e5c3400baa','Tigofly','Wounded minnow fly',7,9,5,200,'Flies for ASP',1,'77169a14-0f5f-481e-8bac-348c555e9813','be137d9b-a56d-4a72-8855-748a0052aa15');
/*!40000 ALTER TABLE `flies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lines`
--

DROP TABLE IF EXISTS `lines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lines` (
  `line_id` varchar(50) NOT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `AFTM` varchar(10) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `in_stock` tinyint(1) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `product_type_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`line_id`),
  KEY `product_id` (`product_id`),
  KEY `product_type_id` (`product_type_id`),
  CONSTRAINT `lines_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `lines_ibfk_2` FOREIGN KEY (`product_type_id`) REFERENCES `product_types` (`product_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lines`
--

LOCK TABLES `lines` WRITE;
/*!40000 ALTER TABLE `lines` DISABLE KEYS */;
INSERT INTO `lines` VALUES ('0094216c-4dfb-4c9e-8261-9170b3ef30c2','AnglerDream','FlyFishingLine 7',30,'7',65,10,'Fly fishing line',1,'707ab786-5f42-42dc-9004-f1280b7a4e54','febd4d98-6eca-4a49-a2fd-bffc44008296'),('6eef94cd-513e-4c0d-9a4a-bb0954f44ebf','AnglerDream','FlyFishingLine 5',30,'5 (5-6)',65,10,'Fly fishing line',1,'8e02078a-631d-43df-b7a9-6e6f0d380f1e','febd4d98-6eca-4a49-a2fd-bffc44008296');
/*!40000 ALTER TABLE `lines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` varchar(50) NOT NULL,
  `shopping_cart_id` varchar(50) DEFAULT NULL,
  `sent` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `shopping_cart_id` (`shopping_cart_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`shopping_cart_id`) REFERENCES `shopping_carts` (`shopping_cart_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_types`
--

DROP TABLE IF EXISTS `product_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_types` (
  `product_type_id` varchar(50) NOT NULL,
  `product_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`product_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_types`
--

LOCK TABLES `product_types` WRITE;
/*!40000 ALTER TABLE `product_types` DISABLE KEYS */;
INSERT INTO `product_types` VALUES ('9fce0ad6-5145-4681-9fce-bdcf13d52e31','reels'),('be137d9b-a56d-4a72-8855-748a0052aa15','flies'),('c9613ab4-b47d-4682-aed5-5e4db6a5ee5a','rods'),('febd4d98-6eca-4a49-a2fd-bffc44008296','lines');
/*!40000 ALTER TABLE `product_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` varchar(50) NOT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('14263cbe-555c-499d-8ad7-5f2f28a630c7','Tigofly','brown-olive fly',5),('27aaee15-0547-4a79-b726-3befbaae2380','Shimano','Freestone XT',330),('2b8eff28-a611-4bfd-90fc-806177c590c0','Shimano','Stone XT',300),('2f1cddcb-2d92-43c1-b6f6-cadc1e9ad96e','Shimano','Biocraft XTC',370),('707ab786-5f42-42dc-9004-f1280b7a4e54','AnglerDream','FlyFishigLine 7',65),('77169a14-0f5f-481e-8bac-348c555e9813','Tigofly','Wounded minnow fly',5),('8e02078a-631d-43df-b7a9-6e6f0d380f1e','AnglerDream','FlyFishigLine 5',65),('9e165333-2f20-42e5-aca9-add3eb82ae0c','Shimano','Biocraft XT',270);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reels`
--

DROP TABLE IF EXISTS `reels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reels` (
  `reel_id` varchar(50) NOT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `AFTM` varchar(10) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `in_stock` tinyint(1) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `product_type_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`reel_id`),
  KEY `product_id` (`product_id`),
  KEY `product_type_id` (`product_type_id`),
  CONSTRAINT `reels_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `reels_ibfk_2` FOREIGN KEY (`product_type_id`) REFERENCES `product_types` (`product_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reels`
--

LOCK TABLES `reels` WRITE;
/*!40000 ALTER TABLE `reels` DISABLE KEYS */;
INSERT INTO `reels` VALUES ('78e3fd90-75b0-4fcb-8f88-c78c2a4b2323','Shimano','Stone XT',120,'5-6',300,10,'fly fishing reel',1,'2b8eff28-a611-4bfd-90fc-806177c590c0','9fce0ad6-5145-4681-9fce-bdcf13d52e31'),('b05553b7-7dd0-4737-8ed9-db6086b226af','Shimano','Freestone XT',125,'5-6',330,10,'fly fishing reel',1,'27aaee15-0547-4a79-b726-3befbaae2380','9fce0ad6-5145-4681-9fce-bdcf13d52e31');
/*!40000 ALTER TABLE `reels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rods`
--

DROP TABLE IF EXISTS `rods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rods` (
  `rod_id` varchar(50) NOT NULL,
  `brand` varchar(50) DEFAULT NULL,
  `model` varchar(50) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `AFTM` varchar(10) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `in_stock` tinyint(1) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `product_type_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rod_id`),
  KEY `product_id` (`product_id`),
  KEY `product_type_id` (`product_type_id`),
  CONSTRAINT `rods_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `rods_ibfk_2` FOREIGN KEY (`product_type_id`) REFERENCES `product_types` (`product_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rods`
--

LOCK TABLES `rods` WRITE;
/*!40000 ALTER TABLE `rods` DISABLE KEYS */;
INSERT INTO `rods` VALUES ('e4292cf4-6a4e-462c-a3dc-8f8fe51895dd','Shimano','Biocraft XT',3,120,'5-6',270,10,'Fly fishing rod',1,'9e165333-2f20-42e5-aca9-add3eb82ae0c','c9613ab4-b47d-4682-aed5-5e4db6a5ee5a'),('ec0b62b8-55e7-4261-9fec-18144bd1a312','Shimano','Biocraft XTC',3,97,'5-6',370,10,'Fly fishing rod',1,'2f1cddcb-2d92-43c1-b6f6-cadc1e9ad96e','c9613ab4-b47d-4682-aed5-5e4db6a5ee5a');
/*!40000 ALTER TABLE `rods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_carts`
--

DROP TABLE IF EXISTS `shopping_carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_carts` (
  `shopping_cart_id` varchar(50) NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  `total_price` int DEFAULT NULL,
  PRIMARY KEY (`shopping_cart_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `shopping_carts_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_carts`
--

LOCK TABLES `shopping_carts` WRITE;
/*!40000 ALTER TABLE `shopping_carts` DISABLE KEYS */;
/*!40000 ALTER TABLE `shopping_carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(50) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telephone_number` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2869660c-e085-4f2d-aa22-2900028c5985','Milos','Cvijovic','milos@example.com','013/111222','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','neka ulica 11',1,1),('2a1725cf-3c5f-4544-b22a-c1afe90f4089','Ljubisa','Ljubisic','ljubisa@example.com','013/333444','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','neka ulica 13',1,0),('3a8a783f-1a59-499c-a31b-c7e4542aee65','Miodrag','Miodragovic','miodrag@example.com','013/444555','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','neka ulica 16',1,0),('771ee659-9b4f-4cc5-ad3d-7e3c32e4f16f','Milenko','Milenkovic','milenko@example.com','013/222333','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','neka ulica 14',1,0),('7f8a1243-368c-4026-8013-12c55d462905','Misa','Misic','misa@example.com','013/222333','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','neka ulica 12',1,0),('8a8c9002-f3d1-41f2-9e03-3aaa82047ef4','Mile','Milic','mile@example.com','013/333444','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3','neka ulica 15',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 14:34:31
