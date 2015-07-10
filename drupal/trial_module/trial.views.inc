<?php

function trial_views_data() {
  return array(
    'node' => array(
      'nid_selected' => array(
        'real field' => 'nid',
        'title' => t('Selected Node'),
        'help' => t('Filter node based on arbitrary node selection.'),
        'filter' => array(
          'handler' => 'views_handler_filter_selected_node',
          'type' => 'yes-no',  // this is the option for boolean filter.
        ),
      ),
    ),
  );
}


function trial_views_query_substitutions($view) {
  return array('***SELECTED_NODE***' => '(1)');
  //return array('***SELECTED_NODE***' => '('. implode(',', array(1)) .')');
}


class views_handler_filter_selected_node extends views_handler_filter_boolean_operator {
  function construct() {
    parent::construct();
    $this->value_value = t('Throw away selected node');
  }

  function query() {
    $this->ensure_my_table();

    $field = $this->table_alias . '.' . $this->real_field . ' ';
    //$value = '***SELECTED_NODE***';
    $value = array(1);
    $operator = empty($this->value) ? 'in' : 'not in';
    $this->query->add_where($this->options['group'], $field, $value, $operator);
  }
}
