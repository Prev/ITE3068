<?php
	
	session_cache_limiter(false);
	session_start();

	date_default_timezone_set('Asia/Seoul');
	error_reporting(E_ALL & ~E_NOTICE);


	require 'functions.php';

	echo "Hello world!<br>";

	echo "<p>";

	$timestamp = filemtime(__FILE__);
	$date = date('Y-m-d H:i:s', $timestamp);
	echo $date;

	echo "</p>";


	$db = connect_db();
	var_dump($db);