-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Creato il: Giu 21, 2019 alle 14:07
-- Versione del server: 5.7.26
-- Versione PHP: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `storiedallabirinto`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `roles_users`
--

CREATE TABLE `roles_users` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `survey`
--

CREATE TABLE `survey` (
  `id` int(11) NOT NULL,
  `sessionid` varchar(100) NOT NULL,
  `age` tinyint(1) DEFAULT NULL,
  `freetext` varchar(500) DEFAULT NULL,
  `gender` enum('M','F','A') DEFAULT NULL,
  `history` varchar(45) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  `q1` varchar(1) DEFAULT NULL,
  `q2` varchar(1) DEFAULT NULL,
  `q3` varchar(1) DEFAULT NULL,
  `q4` varchar(1) DEFAULT NULL,
  `q5` varchar(1) DEFAULT NULL,
  `q6` varchar(1) DEFAULT NULL,
  `q7` varchar(1) DEFAULT NULL,
  `residence` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `survey`
--

INSERT INTO `survey` (`id`, `sessionid`, `age`, `freetext`, `gender`, `history`, `path`, `q1`, `q2`, `q3`, `q4`, `q5`, `q6`, `q7`, `residence`) VALUES
(1, 'df78b748-f013-4c22-b03d-0f75d095e5a4', 23, 'BHO', 'M', '.0.1.3.4.5.7.16.17.20.21', 'books/AriannaELuca', '3', '3', '3', '3', 'Y', 'N', 'Y', 'MiCity'),
(2, '1eccdc4b-ba72-4c87-b9f3-0ba765d20a7f', 23, '', 'M', '.0.1.3.4.5.7.16.17.20.21', 'books/AriannaELuca', '3', '3', '3', '3', NULL, NULL, NULL, 'MiCity');

-- --------------------------------------------------------

--
-- Struttura della tabella `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `last_login_at` datetime DEFAULT NULL,
  `current_login_at` datetime DEFAULT NULL,
  `last_login_ip` varchar(100) DEFAULT NULL,
  `current_login_ip` varchar(100) DEFAULT NULL,
  `login_count` int(11) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `confirmed_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `last_login_at`, `current_login_at`, `last_login_ip`, `current_login_ip`, `login_count`, `active`, `confirmed_at`) VALUES
(19, 'admin@admin.it', '$2b$12$dpUurBg/teryUdQEwgs5E.YzgkoQ1IJVga/35dYTaDlGDURsFQHgC', NULL, NULL, NULL, NULL, NULL, 1, NULL);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indici per le tabelle `roles_users`
--
ALTER TABLE `roles_users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indici per le tabelle `survey`
--
ALTER TABLE `survey`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `roles_users`
--
ALTER TABLE `roles_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `survey`
--
ALTER TABLE `survey`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT per la tabella `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `roles_users`
--
ALTER TABLE `roles_users`
  ADD CONSTRAINT `roles_users_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `roles_users_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
