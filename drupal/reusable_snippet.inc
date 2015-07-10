<?php

// create content type, fields
function reccloud_create_content_type() {
    // config the rec_task "module" content type, which is defined by hook_node_info.
  node_types_rebuild();
  $types = node_type_get_types();
  assert(isset($types['rec_task']));  // this content type has to be existed first.

  node_add_body_field($types['rec_task'], 'Description');
  // Default options: not promoted.
  //variable_set('node_options_rec_task', array('status'));

  // create the "Recommender Task Settings" field using Encrypted Settings
  $field = array(
    'field_name' => 'settings_plain',
    'type' => 'encset', // encrypted setting from encset module
    'entity_types' => array('node'),
    'cardinality' => 1,
    //'locked' => TRUE,  // users can't create instance
    'settings' => array(
      'encryption' => 'none',
      'usage' => 'ini',
    ),
  );
  field_create_field($field);

  // create instances to node.
  $instance = array(
    'field_name' => 'settings_plain',
    'label' => t('Recommender Task Settings'),
    'entity_type' => 'node',
    'bundle' => 'rec_task',
    'description' => t('This field stores settings (database access info, etc) for this recommender task'),
    //'default_value' => array(array('value' => "access_key=\nsecret_key=")),
    'widget' => array(
      'type' => 'encset_textarea',
    ),
    'display' => array(
      'default' => array(
        'label' => 'hidden',
        'type' => 'hidden',
      ),
    )
  );
  field_create_instance($instance);
}


// delete stuff
function reccloud_delete_content_type()
{ // find rec_task node and delete
  $result = db_query('SELECT nid FROM {node} n WHERE n.type = :type', array(':type' => 'rec_task'));
  $nids = $result->fetchCol();
  node_delete_multiple($nids);

  // delete fields
  field_delete_field('settings_plain');

  // delete instances
  $instances = field_info_instances('node', 'rec_task');
  foreach ($instances as $instance_name => $instance) {
    field_delete_instance($instance);
  }

  // Purge all field infromation
  field_purge_batch(1000);
}


// hook_theme
/**
 * Impelements hook_theme().
 */
function reccloud_theme($existing, $type, $theme, $path) {
  return array(
    'server_status' => array(
      'variables' => array(
        'status' => NULL,
        'queue_length' => 0,
      ),
      'template' => 'server_status',
    ),
    'task_status' => array(
      'variables' => array(
        'position' => -1,
      ),
      'template' => 'task_status',
    ),
  );
}


/**
 * This form_validate callback is able to handle arbitrarily added fields data.
 */
function megan_create_request_form_validate($form, &$form_state) {
  $errors = array();
  $field_list = array_keys($form_state['field']);
  foreach ($field_list as $field_name) {
    $field = field_info_field($field_name);
    $instance = field_info_instance('model', $field_name, 'request');

    $items = array();
    field_default_extract_form_values('model', NULL, $field, $instance, LANGUAGE_NONE, $items, $form, $form_state);
    field_default_validate('model', NULL, $field, $instance, LANGUAGE_NONE, $items, $errors);

    $function = "{$field['module']}_field_validate";
    if (function_exists($function)) {
      $function('model', NULL, $field, $instance, LANGUAGE_NONE, $items, $errors);
    }

    foreach (module_implements('field_attach_validate') as $module) {
      $function = $module . '_field_attach_validate';
      $function('model', NULL, $errors);
    }

    if (isset($errors[$field_name])) {
      $field_errors = $errors[$field_name];
      foreach ($field_errors as $langcode => $errors_data) {
        $field_state = field_form_get_state($form['#parents'], $field_name, $langcode, $form_state);
        $field_state['errors'] = $errors_data;
        field_form_set_state($form['#parents'], $field_name, $langcode, $form_state, $field_state);
        field_default_form_errors('model', NULL, $field, $instance, $langcode, $items, $form, $form_state);
      }
    }
  }
}


/**
 * This form_submit callback is able to handle arbitrarily added fields data.
 */
function megan_create_request_form_submit($form, &$form_state) {
  global $user;
  $type = 'request';
  $timestamp = time();
  $values = $form_state['values'];

  $request = entity_create('model', array(
    //'bundle' => $type,  // not needed. use 'type' is ok.
    'type' => $type,
    'uid' => $user->uid,
    'language' => LANGUAGE_NONE,
    'created' => $timestamp,
    'changed' => $timestamp,
  ));

  $field_list = array_keys($form_state['field']);
  foreach ($field_list as $field_name) {
    $field = field_info_field($field_name);
    $instance = field_info_instance('model', $field_name, 'request');
    $items = array();
    field_default_extract_form_values('model', $request, $field, $instance, LANGUAGE_NONE, $items, $form, $form_state);
    field_default_submit('model', $request, $field, $instance, LANGUAGE_NONE, $items, $form, $form_state);
    $request->{$field_name}[$request->language] = $items;
  }

  $request->field_itemref[$request->language][0]['target_id'] = $values['item_nid'];

  entity_save('model', $request);
}


