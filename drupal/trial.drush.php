<?php

function trial_run_script() {
  //drush_print('Hello, world');
  $entity = entity_property_values_create_entity('node', array(
    'type' => 'article',
    'language' => LANGUAGE_NONE,
    'title' => 'Created from entity_property_values_create_entity',
    'uid' => 1,
    'status' => 1,
    'created' => time(),
    'updated' => time(),
    'body' => array('value' => 'hello, world'),
  ));
  $entity->save();
  //print_r($entity);
}


trial_run_script();