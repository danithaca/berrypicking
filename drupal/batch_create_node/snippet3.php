<?php
// Bootstrap Drupal
include_once "includes/bootstrap.inc";
include_once("includes/common.inc");
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

// Import some useful functions for formating and importing data, nothing fancy
include_once('import_functions.php');

$active = FALSE;

if ($active && user_access("administer content types")) {
  print 'Great success!<br />';
  //Importing data from html table
  $data = get_table($import_data_folder . '/chat.html');

  // Quick and dirty cleanup
  $data = array_map('cleanup', $data);
  function cleanup( $line ) {
    $line = preg_replace('/&#\d*;/', ' ', $line);
    return array_map('trim', array_map('strip_tags', $line));
  }
  // Array mapping usernames in old database to user names in drupal database
  global $old_to_new;
   
  foreach($data as $line) {
    $skip = FALSE;
    $old_uname = current(explode(' ', $line[2]));
   
    // Checking just to be sure
    if(!isset($old_to_new[$old_uname])) {
      print('Warning: User: ' . $old_uname . ' missing in $old_to_new.<br/>');
      $skip = TRUE;
    }
    if(empty($line[1])) {
      die("This should never happen, time to panic..");
      //$skip = TRUE;
    }
    // We skip post if post to short or user unknown
    if(!$skip && strlen($line[1]) >= 100) {
     
      $node = new StdClass();
      $node->name = $old_to_new[$old_uname];
      $account = user_load(array('name' => $node->name));
      if(!$account){
        die('User: '. $node->name .' does not exist, check mapping for '. $old_uname .'.<br />');
      }
      // Assigned when calling node_submit (if $node->name is set), so not really necessary to set value here
      $node->uid = $account->uid;
      $node->type = 'nyhet';
      $node->created = olddate_to_unix_time($line[3]);
      $node->changed = $node->created;
      // Must set this so that created is not overwritten some where else
      $node->date = format_date($node->created, 'custom', 'Y-m-d H:i:s O');
      $node->title =  mktitle(html_entity_decode($line[1]), 30);
      $node->body = $line[1];
      // Format set to filtered html
      $node->format = 1;
      $node->log = 'Importerad frŒn HEABNET '. date('d/m-y H:m') .'.';
      // Status set to published
      $node->status = 1;
      // Promote to first page
      $node->promote = 1;
      $node->sticky = 0;
      $node->revision = 0;
      // Enable read/write comments
      $node->comment = 2;
      $node->pathauto_perform_alias = 1;
     
      print '<pre>';
      print '<em>Before submit:</em><br />';
      print_r($node);
      $node = node_submit($node);
      print '<em>After:</em><br />';
      print_r($node);
      print '</pre><hr />';
      //node_save($node);
      // Just testing, only need one post
      break;
    }
  }
}
else {
  print 'Script ' . __FILE__ . ' is not set to active, or access denied';
}

/*
Some pitfalls:
Found out that if node->date is not set the following code in node_submit will result in the 'created' property losing its value:
<?php
$node->created = !empty($node->date) ? strtotime($node->date) : time();
?>
 */
?>