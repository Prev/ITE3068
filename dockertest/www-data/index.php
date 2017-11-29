<?php
	require 'includes/init.php';
?>
<!DOCTYPE html>
<html>
<head>
	<title>Guest book</title>

	<style type="text/css">
		#wrap{
			width: 500px;
			margin: 30px auto;
			font-size: 18px;
		}

		form{
			margin-left: 15px;
			padding-top: 10px;
			border-top: 1px solid #ccc;
		}
	</style>
</head>
<body>
	<div id="wrap">
		<h1>Guest book</h1>
		<ul>
			<?php
			$result = $db->query("SELECT * FROM `guestbook`");
			if (!$result->num_rows) {
				echo 'no message yet!';
			}else {
				while ($row = $result->fetch_object()) {
				echo "<li>{$row->message} - {$row->register_time}</li>";
				}
			}
			?>
		</ul>

		<div>
			<form action="insert.php" method="POST">
				<input type="text" name="message">
				<input type="submit" name="submit">
			</form>
		</div>
	</div>
</body>
</html>