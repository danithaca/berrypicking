snippet from the forum, using node_submit and node_save

<?php
   
// over here you connect to your old database and retrieve the values like this till the end

      while ($row= mysql_fetch_array($resultwithlimit)) {

      $a1 = $row["YourTitlefield"];
      $a2 = $row["firstnameauthor"];
      $a3 = $row["lastnameauthor"];
      $a4 = $row["otherfield42"];
      $a5 = $row["themistfield"];
      $a6 = $row["body"];
      $a7 = $row["field2"];
      $a8 = $row["wordsvalley"];
      $a9 = $row["randomfield29"];



$mynode = array();

$mynode['title'] = "$a1";

$mynode['type'] = "yourcontenttype"; // all content types have names which are given at the time of the content type creation. visible at content types page when you drag your mouse over the list of content types

$mynode['name'] = "thenameoftheusersubmittingthepage";//not necessary

$mynode['body'] = "$a6"; // You can remove the body field from your content type if you want.

$mynode['status'] = 1;//stands for published=1 or unpublished=0 content

$mynode['uid'] = 121;//uid is user id, the user id 1 being the id of the one who makes first id after a drupal installation, uid 1 has all prvilleged, make sure your user id comes with all privileges,preferably use userid 1 to save yourself from the hassle.

$mynode['promote'] = 0; // promote =0 doesn't promote the content to the front page , whereas promote=1 promotes the content to the front page

$mynode['comment'] = '2'; // comment 0=off , comment 1=readonly, comment 2=allowed

$mynode['field_friendlytitle'] = array(array('value' => "$a4" ));// field_friendlytitle is the field I presumably created using cck for the content type. Notice how I am filling in the value for field_friendlytitle using array in an array.

$mynode['field_firstnameauthor'] = array(array('value' => "$a2" ));
$mynode['field_lastnameauthor'] = array(array('value' => "$a3" ));
$mynode['field_fieldIcreatedwithcck'] = array(array( 'value' => "$a9"));
$mynode['field_fieldIcreatedwithcck1'] = array(array('value' => "$a8" ));
$mynode['field_fieldIcreatedwithcck2sjhdshjdj'] = array(array('value' => "$a7" ));

$mynode['format'] = '2'; // inputformat, format=1 means Filtered HTML,format=1 means PHP code , format=2 means Full HTML


//You can also specify $mynode['nid'] followed by a number which will be the nid but I presume that it wont be of use to you at the moment. Not mentioning it will lead to a sequential auto generation whereas mentioning a static number will overwrite the old content each type you save the node!;




$mynode = node_submit($mynode);
node_save($mynode);

unset($mynode);

}
?>