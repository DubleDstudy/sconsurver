<?php
	//쿼리
	$query = "select * from comment_info";
	$conn = mysql_connect("52.195.16.33:8000","admin","qwer1234");
	mysql_select_db("scon", $conn);
	
	//한글 깨짐문제 해결방법. 
	/*
	mysql_query("set session character_set_connection=utf8;");
	mysql_query("set session character_set_results=utf8;");
	mysql_query("set session character_set_client=utf8;");
	*/
	mysql_query("set names utf8"); //간단히 이거 한줄이면 되네

	$result = mysql_query($query, $conn);

	while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) {
		$res['user_id'] = urlencode($row["user_id"]);
		$res['id'] = urlencode($row["id"]);
		$res['comment'] =urlencode($row["comment"]);
	}
	
	$json = json_encode ($arr);
	$json = urldecode ($json);
	print $json;
	mysql_close($conn);
?>
