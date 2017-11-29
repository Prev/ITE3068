<?php
	
	session_cache_limiter(false);
	session_start();

	date_default_timezone_set('Asia/Seoul');
	error_reporting(E_ALL & ~E_NOTICE);

	require 'functions.php';

	$db = connect_db();
	init_table();