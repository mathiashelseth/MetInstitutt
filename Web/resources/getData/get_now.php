<?php
$db = mysqli_connect("***REMOVED***","***REMOVED***","***REMOVED***","***REMOVED***") or die('Feil ved oppkobling til server. ERROR: 109');

$datepick = $_POST['date'];
        $ascdesc = $_POST['ascdesc'];
        $limitby = $_POST['limitby'];

        $query = "SELECT * FROM data_main_min ORDER BY ID DESC LIMIT 1";
        
       
        mysqli_query($db, $query) or die('FEILMELDING: Feil i inntasting');

        $result = mysqli_query($db, $query);
        print($result);

?>