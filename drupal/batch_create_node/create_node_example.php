<?php
// Written by Victor Kane - victorkane at awebfactory dot com dot ar
// *** This script affects your database
//
// Edits by Jeff Vogelsang - jeffvogelsang at pqa dot com

// CONFIGURATION

// Change the value below to TRUE when you want to run the script After running,
// immediately change back to FALSE in order to prevent accidentally executing
// this script twice.
// NOTE: I find the best way to do this is to leave it false. When you are ready
// to execute, set to this variable to true, and then click Preview. The script
// will execute, but will not be saved with the value set to true. This prevents
// accidentally saving the script with the value set to true. Also, it prevents
// the unfortunate situation where the cron job runs while it's set to true,
// and you get double imports.
$active = false;

// Bootstrap Drupal
include_once "includes/bootstrap.inc";
include_once("includes/common.inc");
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

// CSV file containing the data to import.
// For simplicity I place this in the root of the Drupal
// site and remove it when done.
$data_archive = 'mn1.csv';

// Content information... This is the CCK type data you wish to import to.
// It needs to match exactly your created content type information.
$content_type = 'eis_meeting_notes';
$content_name = 'EIS Meeting Notes';

// Check for the script being enabled, and for appropriate permissions.
if ($active) {
    if (user_access("administer content types")) {
        insert_content($content_type, $data_archive);
    } else {
        print "You don't have permission to administer content types.";
    }
  } else {
        print "Variable active is set to false.";
}

function insert_content ($content_type, $data_archive) {
    // Open the CSV file read only.
    $handle = fopen($data_archive, "r");
    // Read the headers from the first line.
    $theHeaders = fgetcsv ($handle);
    // Keep count of how many lines we have processed.
    $lineno = 0;
    while ($line = fgetcsv ($handle)) {
        $output = '';
    $valueno = 0;
    $lineno++;
    $output .= '<ul>Line: '. $lineno;
    $observaciones = '';
    foreach ($line as $value) {
      if ($value) {
        $output .= '<li>'.$theHeaders[$valueno].': '.$value.'</li>';
        $observaciones .= '<li>'.$theHeaders[$valueno].': '.$value.'</li>';
      }
      $valueno++;
    }
    $output .= '</ul>';

    // Create new node
    $node = array();
    // Node is of type $content_type/$content_name
    $node['type'] = $content_type;
    $node['name'] = $content_name;
    // Formats on CCK nodes apply to fields, so no format set here.
    $node['format'] = 0;
    // Enable read/write comments.
    $node['comment'] = 2;
    // Published
    $node['status'] = 1;
    // Not promoted to front page.
    $node['promote'] = 0;
    // Not sticky.
    $node['sticky'] = 0;
    // Create a log entry for the first revision.
    $log = 'Imported from csv.' . date('g:i:s a');
    $node['log'] = $log;

    // Node fields here, mapped to CSV file data.
    $node['title'] = $line[1];
    $node['created'] = $line[4];
    $node['name'] = $line[7];
    $node['uid'] = $line[8];

    // CCK fields here, mapped to CSV file data.
    // For each, we set the value, and the desired input/output format.
    // In this case, format 4 is a non-html-filtering input type.
   
    $node['field_eis_action_items'] = array
    (
        0 => array
            (
                'value' =>  $line[16],
                'format' => 4
            )
    );

    $node['field_eis_agenda'] = array
    (
        0 => array
            (
                'value' =>  $line[14],
                'format' => 4
            )
    );

    $node['field_eis_attendees'] = array
    (
        0 => array
            (
                'value' =>  $line[9],
                'format' => 4,
            )
    );

    $node['field_eis_meeting_date'] = array
    (
        0 => array
            (
                'value' =>  $line[10]
            )
    );

    $node['field_eis_notes'] = array
    (
        0 => array
            (
                'value' =>  $line[22],
                'format' => 4
            )
    );

    $node['field_eis_open_issues'] = array
    (
        0 => array
            (
                'value' =>  $line[20],
                'format' => 4
            )
    );

    $node['field_eis_purpose'] = array
    (
        0 => array
            (
                'value' =>  $line[12],
                'format' => 4
            )
    );

    $node['field_eis_requirements'] = array
    (
        0 => array
            (
                'value' => $line[18],
                'format' => 4
            )
    );

    // Basic check for having a non-blank title.
    // Then submit/save node, and output the data we used for this node.
    if ($node['title']) {
      $node = (object)$node;
        // This is the unique TID from the taxonomy table. It can also be an array of values.
        // Set it here after we turn the node into an object...
        $node->taxonomy[] = 1;
      $node = node_submit($node);
      node_save($node);
      print $output;
    };
  }
}
?>