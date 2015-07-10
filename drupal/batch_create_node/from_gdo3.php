<?php

// Original written by Victor Kane - victorkane at awebfactory dot com dot ar
// Modifications by Jesse Mortenson - aka greenmachine on drupal.org

// *** This script affects your database

// CONFIGURATION

// Change the value below to TRUE when you want to run the script After running, immediately
// change back to FALSE in order to prevent accidentally executing this script twice.

$active = FALSE;

//This modified script inputs data based upon the first row in your CSV file, the header row. Your headers must match the fields of the node object in order for any data to be saved. For example, you should have columns for title, body, and type (type is the node type).

//Look at the translate_value function to see field types I've already accounted for. You will need to match the key values for special things like organic groups and CCK.

//If you're using CCK, make sure to include YOUR custom field machine-readable field names in the list of cases. For most fields, you can just include them in the big list of cases. If the field needs to be submitted with something other than the [0] => [value] => "value" format, you need to add a special case.

// CODE
include_once("includes/bootstrap.inc");
include_once("includes/common.inc");
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

$archive_data = 'files/data_file.csv'; // must point to your data file, which must have proper header row
print "Script working<br />";

if ($active) {
  if (user_access("administer content types")) {
    print "Processing begins \n";
    print '<pre>';
    $nodes_array = insert_content($archive_data);
    print_r($nodes_array); // prints the array of nodes the script gathered from your file, for debugging purposes only
    print '</pre>';
  } else {
    print "You don't have permission to administer this content type";
  }
} else {
  print "Import script is not active. Change the active variable to TRUE to activate";
}


// this function translates a cell in your CSV file and inserts it into the $node array
// the postpone variable is for fields that should be added to the node object AFTER _validate and _submit for whatever reason; I use it here for organic groups

function translate_value($key, $value, $headers, &$node, &$postpone) {
  switch ($headers[$key]) {
    // this first batch is generic node stuff
    case 'title': 
    case 'body':
    case 'created':
      $node[$headers[$key]] = $value;
      break;
    case 'uid':   // using UID for author, then loads username based on that
      $node['uid'] = $value;
      $user = user_load(array('uid' => $node['uid']));
      $node['name'] = $user->name;
      break;
      $node['body'] = $value;
      break;
    case 'type':
      $node['type'] = $value;
        switch ($node['type']) {   // optional: I have comment settings conditional on type
          case 'forum':
          case 'blog':
          case 'story':
            $node['comment'] = 2;
            break;
        }
      break;

    // taxonomy should be a comma separated list in the CSV file
    case 'taxonomy': 
      $node['taxonomy'] = explode(',', $value);
      break;

    // CCK stuff here, these will need to be changed if your nodes use CCK
    case 'field_company':
    case 'field_title':
    case 'field_article_name':
    case 'field_media_outlet':
    case 'field_author':
    case 'field_notes':
      $node[$headers[$key]] = array(array('value' => $value));
      break;
    case 'field_link':
      $node['field_link'] = array(array('url' => $value, 'title' => '', 'attributes' => 'N;'));
      break;
    case 'field_date_published':
      $node['field_date_published'] = array(array('value' => array(
                                      'mon' => substr($value,5,2),
                                      'mday' =>substr($value,8,2),
                                      'year' => substr($value,0,4),
                                      'hour' => 0,
                                      'minute' => 0,
                                      )));
      break;

    // Organic groups values. Group ID numbers should be a comma-separated list in the CSV
    case 'og_groups':  
      $postpone['og_groups'] = explode(',', $value);
      foreach ($postpone['og_groups'] as $gid) {
        $gnode = node_load($gid);
        $postpone['og_groups_names'][] = $gnode->title;
      }
      break;

    default:
      break;
  } 
  // nothing is returned because the $node and $postpone arguments are accepted by reference
}


// this function actually inserts content. See opportunities to comment out the two lines that actually change your database. With those commented out, you just get debug data to look at.

function insert_content ($archive_data) {
  $handle = fopen($archive_data, "r");
  $headers = fgetcsv ($handle, 4096);

  //print_r($theHeaders);
  while ($line = fgetcsv ($handle, 4096)) {
    //print_r($line);

    $node = array();
    $postpone = array();

    foreach ($line as $key => $value) {
      translate_value($key, $value, $headers, $node, $postpone);
    }

    // defaults for all imported nodes. feel free to change
    $node['format'] = 3;
    $node['status'] = 1;
    $node['promote'] = 0;
    $node['sticky'] = 0;
    $log = 'Imported node using import script at ' . date('g:i:s a');
    $node['log'] = $log;


    if ($node['title']) {
      $node = (object)$node;
      $nodes_array['pre'][] = $node; // adding to node array for debug info
      node_validate($node);
      $error = form_get_errors();
      if (!$error) {
        $node = node_submit($node); // comment this out to test first before changing the database

        foreach ($postpone as $key => $value) {
          switch ($key) {
            case 'og_groups':
              $node->og_public = 0;
              $node->og_groups = $value;
              break;
            case 'og_groups_names':
              $node->og_public = 0;
              $node->og_groups_names = $value;
              break;
          }
        }

        node_save($node); // comment this out to test first before changing the database
      } else {
        print_r($error);
      }
      $nodes_array['post'][] = $node; // adding to "post" node array for debug info
    }
  } // end while

  /*
  The nodes_array variable includes two arrays: pre and post. This shows you how your nodes look before Drupal takes a look at them (pre), and after the node submission process takes place (post). This helps to debug any problems you're having with field values being stored inccorectly

  Of course, if you  commented out the node_submit and node_save comamnds, (post) will not be as useful.
  */
  return $nodes_array;

} // end function



?>
