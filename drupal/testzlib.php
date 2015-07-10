<?php
//$fp = gzopen('/tmp/test.txt.gz', 'wb9');
//gzwrite($fp, file_get_contents('/tmp/test.txt'));
//gzclose($fp);

$zp = gzopen('/tmp/test.txt.gz', 'rb');
$fp = fopen('/tmp/test.txt', 'w');
while ($string = gzread($zp, 4096)) {
  echo $string;
  fwrite($fp, $string, strlen($string));
}
gzclose($zp);
fclose($fp);