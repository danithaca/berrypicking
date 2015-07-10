<?php
/**
 * @file
 * admin_features.features.inc
 */

/**
 * Implements hook_ctools_plugin_api().
 */
function admin_features_ctools_plugin_api($module = NULL, $api = NULL) {
  if ($module == "strongarm" && $api == "strongarm") {
    return array("version" => "1");
  }
}
