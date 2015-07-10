<?php
/**
 * @file
 * devel_features.features.inc
 */

/**
 * Implements hook_ctools_plugin_api().
 */
function devel_features_ctools_plugin_api($module = NULL, $api = NULL) {
  if ($module == "strongarm" && $api == "strongarm") {
    return array("version" => "1");
  }
}
