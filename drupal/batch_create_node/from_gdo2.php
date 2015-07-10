<?php

// Written by Victor Kane - victorkane at awebfactory dot com dot ar
// *** This script affects your database
//
// CONFIGURATION

    // Change the value below to TRUE when you want to run the script After running, immediately
    // change back to FALSE in order to prevent accidentally executing this script twice.
  $active = TRUE;

// CODE
  include_once "includes/bootstrap.inc";
  include_once("includes/common.inc");
  drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);

  $content_type = 'contacto';
  $content_name = 'Contacto';
  $archivo_datos = 'backup/test.csv';

  if ($active) {
    if (user_access("administer content types")) {
      insertar_contenido($content_type, $archivo_datos);
    } else {
      print "No tiene permisos para administer content types";
    }
  } else {
      print "exportar-empresas no ha sido activado. Ver variable $active al principio del c—digo fuente";
  }

function insertar_contenido ($content_type, $archivo_datos) {
  $handle = fopen($archivo_datos, "r");
  $theHeaders = fgetcsv ($handle, 4096, "\t");
  $lineno = 0;
  while ($line = fgetcsv ($handle, 4096, "\t")) {
    $output .= '';
    $valueno = 0;
    $lineno++;
    $output .= '<ul>L’nea: '.$lineno;
    $observaciones = '';
    foreach ($line as $value) {
      if ($value) {
        $output .= '<li>'.$theHeaders[$valueno].': '.$value.'</li>';
        $observaciones .= '<li>'.$theHeaders[$valueno].': '.$value.'</li>';
      }
      $valueno++;
    }
    $output .= '</ul>';
    $node = array();
    $node['title'] = $line[3];
    $node['body'] = $observaciones;
    $node['type'] = $content_type;
    $node['format'] = 3;
    //$node['taxonomy'] = $_REQUEST['taxonomy'];
    $node['name'] = $content_name;
    //$node['date'] = $_REQUEST['date'];
    $node['status'] = 1;
    $node['promote'] = 0;
    $node['sticky'] = 0;
    $log = 'Importado por importar-contactos el ' . date('g:i:s a');
    $node['log'] = $log;

    $node['field_empresa'] = array (
    0 => array(
      'nid' => db_result(db_query("SELECT nid FROM {node} WHERE title = '%s'", $line[2])),
      ),
    );

    $node['field_cargo'] = array (
      0 => array(
        'value' => $line[22],
        ),
      );
    $node['field_saludo'] = array (
      0 => array(
        'value' => $line[17],
        ),
      );
    $node['field_nombres'] = array (
      0 => array(
        'value' => $line[54],
        ),
      );
    $node['field_apellidos'] = array (
      0 => array(
        'value' => $line[55],
        ),
      );
    $node['field_mvil'] = array (
      0 => array(
        'value' => $line[15],
        ),
      );
    $node['field_telfono_particular'] = array (
      0 => array(
        'value' => $line[14],
        ),
      );
    $node['field_buscapersonas'] = array (
      0 => array(
        'value' => $line[16],
        ),
      );
    $node['field_e_mail'] = array (
      0 => array(
        'value' => $line[89],
        ),
      );

    // Marc of funnymonkey.com suggestion: the integer '2' is tid
    $node['taxonomy'] = array(2);

/*
  // this code, from the autosave module, is unnecessary, since node_save will do it for us :)
  $node['nid'] = db_result(db_query("SELECT id FROM {sequences} WHERE name = '%s'", 'node_nid')) + 1;
  $node['vid'] = db_result(db_query("SELECT id FROM {sequences} WHERE name = '%s'", 'node_revisions_vid')) + 1;
*/
    if ($node['title']) {
      $node = (object)$node;
      $node = node_submit($node);
      node_save($node);
      print $output;
      /*
      $nid = $node->nid;
      $tid = 6;
      db_query("INSERT INTO {term_node} (nid, tid) VALUES (%d, %d)", $nid, $tid);
      */
    }
  }
}
