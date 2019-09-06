<?php
// array for JSON response
$response = array();
 
// check for required fields
if (isset($_POST['Car_No']) && isset($_POST['lap_start_time']) && isset($_POST['lap_end_time'])) {
 
    $Car_No = $_POST['Car_No'];
    $lap_start_time = $_POST['lap_start_time'];
    $lap_end_time = $_POST['lap_end_time'];
 
    // include db connect class
    require_once __DIR__ . '/db_connect.php';
 
    // connecting to db
    $db = new DB_CONNECT();
 
    // mysql inserting a new row
    $result = mysql_query("INSERT INTO Race1(Car_No, lap_start_time, lap_end_time) VALUES('$Car_No','$lap_start_time', '$lap_end_time')");
 
    // check if row inserted or not
    if ($result) {
        // successfully inserted into database
        $response["success"] = 1;
        $response["message"] = "Part successfully inserted.";
 
        // echoing JSON response
        echo json_encode($response);
    } else {
        // failed to insert row
        $response["success"] = 0;
        $response["message"] = "Oops! An error occurred.";
 
        // echoing JSON response
        echo json_encode($response);
    }
} else {
    // required field is missing
    $response["success"] = 0;
    $response["message"] = "Required field(s) is missing";
 
    // echoing JSON response
    echo json_encode($response);
}
?>