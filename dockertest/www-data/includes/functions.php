<?php

	function connect_db() {
		if ($GLOBALS['db_connection']) return $GLOBALS['db_connection'];

		$server = 'db';
		$user = 'root';
		$pass = 'root';
		$database = 'test';
		$port = 3306;

		$connection = new mysqli($server, $user, $pass, $database, $port);

		if ($connection->connect_error) {
			echo('Connect Error (' . $connection->connect_errno . ') '. $connection->connect_error);
		}

		$connection->query('SET NAMES utf8');

		$GLOBALS['db_connection'] =  $connection;

		return $connection;
	}

	function init_table() {
		$db = connect_db();

		$r = $db->query(
			"CREATE TABLE IF NOT EXISTS `guestbook` (
			  `id` int(11) NOT NULL AUTO_INCREMENT,
			  `message` text COLLATE utf8mb4_unicode_ci NOT NULL,
			  `register_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
			  PRIMARY KEY (`id`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci AUTO_INCREMENT=1 ;"
		);
	}