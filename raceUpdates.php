<?php
// Settings
// host, user and password settings
$host = "localhost";
$user = "user";
$password = "user";
$database = "F1Track";

// make connection to database
$connectdb = mysqli_connect($host,$user,$password)
or die ("Cannot reach database");

// select db
mysqli_select_db($connectdb,$database)
or die ("Cannot select database");

// sql command that selects all entires from current time and X hours backwards
$sql="SELECT * FROM Race2";

//NOTE: If you want to show all entries from current date in web page uncomment line below by removing //
//$sql="select * from temperaturedata where date(dateandtime) = curdate();";

// set query to variable
$results = mysqli_query($connectdb,$sql);

// create content to web page
?>
<html>
<head>
<title>Race Results</title>
<style>
	.header{
		padding: 20px;
		text-align: center;
		background: #1abc9c;
		color: white;
		font-size: 15px;}
	.tablehead{
		background-color: #1abc9c;
		color: white;
		font-size: 15px;
		padding: 0px;
		cellpadding:0px;
	}
	table{
		/*border: solid 2px #1abc9c;
		color: #1abc9c;*/
		border-collapse:collapse;
		width:60%;		
	}
	table, td,th{
		/*border-right: solid 2px #1abc9c;
		border-left: solid 2px #1abc9c;*/
		border: solid 2px #1abc9c;
		text-align: center;
		height: 50px;
	}
	
	
</style>
</head>

<body>
</body>
<div class="header">
	<h1>Race Updates</h1>
</div>
<br><br>
<!--table width="800" border="1" cellpadding="1" cellspacing="1" align="center">
<tr>
<th>Car No</th>
<th>Race start time</th>
<th>Lap end time</th>
<th>Lap Time</th>
<tr-->
<table>
<thead>
	<tr class="tablehead">
		<th>Car No</th>
		<th>Race start time</th>
		<th>Lap end time</th>
		<th>Lap Time</th>
	</tr>
</thead>
<?php
// loop all the results that were read from database and "draw" to web page
while($result=mysqli_fetch_assoc($results)){
echo "<tr>";
echo "<td>".$result['Car_No']."</td>";
echo "<td>".$result['lap_start_time']."</td>";
$Start_time=$result['lap_start_time'];
echo "<td>".$result['lap_end_time']."</td>";
echo "<td>".abs(strtotime($result['lap_end_time'])-strtotime($result['lap_start_time']))." seconds</td>";
echo "<tr>";
}
echo "Race Start Time:".$Start_time." Go!<br><br>";
?>
</table>
<br>
<br>

</html>
