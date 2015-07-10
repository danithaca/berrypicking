<?php
$vid = 5;    //vocab we're adding to
$parent = 1;   //parent tid
$terms = array(    //array of terms
'Ireland',
'Scotland',
'Wales',
'England'
); 

foreach ($terms as $term) {
   $edit = array ("vid" => $vid, "name" => $term, "parent"=>$parent );
   $msg = taxonomy_save_term($edit);
   print $edit['name'] . ": $msg<BR />\n";
}
?>