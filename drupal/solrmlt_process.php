<?php
include_once './includes/bootstrap.inc';
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);


// directly copied from the apachesolr_mlt, with some modification:
// return items rather than the block
function solrmlt_suggestions($block_id, $nid) {

  try {
    $solr = apachesolr_get_solr();
    $fields = array('mlt.mintf', 'mlt.mindf', 'mlt.minwl', 'mlt.maxwl', 'mlt.maxqt', 'mlt.boost', 'mlt.qf');
    $block = apachesolr_mlt_load_block($block_id);

    $params = array(
        'qt' => 'mlt',
        'fl' => 'nid,title,url',
        'mlt.fl' => implode(',', $block['mlt_fl']),
    );

    foreach ($fields as $field) {
      $drupal_fieldname = str_replace('.', '_', $field);
      if (!empty($block[$drupal_fieldname])) {
        $params[$field] = check_plain($block[$drupal_fieldname]);
      }
    }
    $query = apachesolr_drupal_query('id:' . apachesolr_document_id($nid));

    // This hook allows modules to modify the query and params objects.
    apachesolr_modify_query($query, $params, 'apachesolr_mlt');
    if (empty($query)) {
      return;
    }

    $response = $solr->search($query->get_query_basic(), 0, $block['num_results'], $params);
    if ($response->response) {
      $docs = (array) end($response->response);
    }
    return $docs;
  } 
  catch ( Exception $e ) {
    watchdog('Apache Solr', $e->getMessage(), NULL, WATCHDOG_ERROR );
  }
}


// assume we have project_top100 and mlt_relation tables
function solrmlt_run() {
  $block_id = 1;
  $results = db_query("SELECT nid FROM {project_top100}");
  while ($project = db_fetch_array($results)) {
    $nid = $project['nid'];
    $items = solrmlt_suggestions($block_id, $nid);
    foreach ($items as $item) {
      db_query("INSERT INTO {mlt_relation} VALUE(%d, %d)", $nid, $item->nid);
    }
  }
}

solrmlt_run();