<?php
include_once './includes/bootstrap.inc';
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

// definiton
$magic_str = "trash";
$sid_creation = 1;
$sid_open = 2;
$sid_inaccessible = 3;
$sid_corrected = 4;
global $user;
$tickets_result = db_query("SELECT nid, 'ticket' as type, field_url_value FROM content_type_ticket");
while($ticket = db_fetch_object($tickets_result)) {
	$nid = $ticket->nid;
	$n = node_load($ticket->nid);
	$url = $ticket->field_url_value;
	$sid = workflow_node_current_state($ticket);
print $sid;
	// we only give chance to tickets that are newly created or previously inaccessible (perhaps due to network failure)
	if ($sid == $sid_creation || $sid == $sid_inaccessible || $sid == $sid_corrected) {
		$content = file_get_contents($url);
		if ($content) {  // if the URL is readable
			if (strpos($content, $magic_str)) {  // if we find the magic string
				print "we found the string";
				$user->uid = 1;
				workflow_execute_transition(&$n,  $sid_corrected, $comment = NULL,TRUE);
				
				$user->uid =0;
			}
			else {
			print "No string, reopen";
				$user->uid = 1;
				print $nid ." ". $sid_open;
				workflow_execute_transition(&$n,  $sid_open, $comment = NULL,TRUE);
				                                
				$user->uid =0;
			}
		}
		else { // url open error
			print "no open";
			$user->uid=1;
			workflow_execute_transition(&$n,  $sid_inaccessible, $comment = NULL,TRUE);
			$user->uid=0;                                
		}
	}
}
?>
