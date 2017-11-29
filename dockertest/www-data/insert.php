<?php
	
	require 'includes/init.php';

	$message = $db->escape_string($_POST['message']);

	$result = $db->query("INSERT INTO `guestbook` (`message`) VALUES ('{$message}');");

	if ($result)
		header('Location: /');
	else
		echo $db->error();

?>