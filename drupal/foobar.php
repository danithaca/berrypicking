<?php
function foobar1() {
  $a = array(
    'a' => 1,
    'b' => 2,
    'c' => 3,
  );

  $b = array('a' => 'a', 'b' => 'b');

  var_dump(array_intersect_key($a, $b));
}

function foobar2() {
  //echo drupal_json_encode(node_load(1));
  //$id = computing_create_record('common', 'pingme', 'test', array('id4' => 1));
  //echo "ID: $id\n";
  $results = computing_query_records(array('id'=>1));
  foreach ($results as $r) {
    var_dump($r);
  }
}

foobar2();
