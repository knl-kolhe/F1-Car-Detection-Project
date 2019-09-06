<?php
// array for JSON response
$response = array();
 
// include db connect class
require_once __DIR__ . '/db_connect.php';
 
// connecting to db
$db = new DB_CONNECT();
 
// get all products from products table
$result = mysql_query("SELECT * FROM Race1") or die(mysql_error());
 
// check for empty result
if (mysql_num_rows($result) > 0) {
    // looping through all results
    // products node
    $response["Race"] = array();
 
    while ($row = mysql_fetch_array($result)) {
        // temp user array
        $Race = array();
        $Race["ID"] = $row["ID"];
        $Race["Car_No"] = $row["Car_No"];
        $Race["lap_start_time"] = $row["lap_start_time"];
	$Race["lap_end_time"] = $row["lap_end_time"];
 
        // push single product into final response array
        array_push($response["Race"], $Race);
    }
    // success
    $response["success"] = 1;
 
    // echoing JSON response
    echo json_encode($response);
} else {
    // no products found
    $response["success"] = 0;
    $response["message"] = "No parts inserted";
 
    // echo no users JSON
    echo json_encode($response);
}
?>