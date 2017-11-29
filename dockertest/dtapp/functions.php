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

	
