DROP TABLE IF EXISTS `user_table`
DROP TABLE IF EXISTS `songlist_table`
DROP TABLE IF EXISTS `song_table`
DROP TABLE IF EXISTS `comment_table`
DROP TABLE IF EXISTS `friends_table`
DROP TABLE IF EXISTS `collect_table`

CREATE TABLE `user_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(11) NOT NULL,
  `password` varchar(11) NOT NULL,
  `name` varchar(11) NOT NULL,
  `signature` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `songlist_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(11) NOT NULL,
  `user_idfk` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_idfk_1` (`user_idfk`),
  CONSTRAINT `user_idfk_1` FOREIGN KEY (`user_idfk`) REFERENCES `user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `song_table` (
  `id` int(11) unsigned NOT NULL,
  `song_name` varchar(20) NOT NULL,
  `singer` varchar(11) NOT NULL,
  `lyrics` varchar(500) DEFAULT NULL,
  `user_idfk` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_idfk_2` (`user_idfk`),
  CONSTRAINT `user_idfk_2` FOREIGN KEY (`user_idfk`) REFERENCES `user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `comment_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `comment` varchar(255) DEFAULT NULL,
  `song_idfk` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `song_idfk` (`song_idfk`),
  CONSTRAINT `song_idfk` FOREIGN KEY (`song_idfk`) REFERENCES `song_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

--双向多对多
CREATE TABLE `friends_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `one_idfk` int(11) unsigned NOT NULL,
  `another_idfk` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `one_idfk` (`one_idfk`),
  KEY `another_idfk` (`another_idfk`),
  CONSTRAINT `another_idfk` FOREIGN KEY (`another_idfk`) REFERENCES `user_table` (`id`),
  CONSTRAINT `one_idfk` FOREIGN KEY (`one_idfk`) REFERENCES `user_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

--单向多对多
CREATE TABLE `collect_table` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `songlist_idfk` int(11) unsigned NOT NULL,
  `song_idfk` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `songlist_idfk` (`songlist_idfk`),
  KEY `song_idfk_2` (`song_idfk`),
  CONSTRAINT `song_idfk_2` FOREIGN KEY (`song_idfk`) REFERENCES `song_table` (`id`),
  CONSTRAINT `songlist_idfk` FOREIGN KEY (`songlist_idfk`) REFERENCES `songlist_table` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
