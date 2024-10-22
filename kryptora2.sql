-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2024 at 12:38 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kryptora2`
--

-- --------------------------------------------------------

--
-- Table structure for table `student_management`
--

CREATE TABLE `student_management` (
  `STUDENT_ID` int(11) NOT NULL,
  `NAME` varchar(255) DEFAULT NULL,
  `EMAIL` varchar(255) DEFAULT NULL,
  `PHONE_NO` varchar(15) DEFAULT NULL,
  `GENDER` varchar(10) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `STREAM` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_management`
--

INSERT INTO `student_management` (`STUDENT_ID`, `NAME`, `EMAIL`, `PHONE_NO`, `GENDER`, `DOB`, `STREAM`) VALUES
(86, ' 1', ' ', ' ', ' ', '0000-00-00', ' ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student_management`
--
ALTER TABLE `student_management`
  ADD PRIMARY KEY (`STUDENT_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
