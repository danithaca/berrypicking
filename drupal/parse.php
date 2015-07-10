<?php

function remove_comments() {
  $fileStr = file_get_contents('/Users/danithaca/Development/drupal7/sites/d7dev1.localhost/settings.php');
  $newStr  = '';

  $commentTokens = array(T_COMMENT);

  if (defined('T_DOC_COMMENT'))
    $commentTokens[] = T_DOC_COMMENT; // PHP 5
  if (defined('T_ML_COMMENT'))
    $commentTokens[] = T_ML_COMMENT;  // PHP 4

  $tokens = token_get_all($fileStr);

  foreach ($tokens as $token) {
    if (is_array($token)) {
      if (in_array($token[0], $commentTokens))
        continue;

      $token = $token[1];
    }

    $newStr .= $token;
  }

  echo $newStr;
}

function print_tokens() {
  $fileStr = file_get_contents('/Users/danithaca/Development/drupal7/sites/d7dev1.localhost/settings.php');
  $tokens = token_get_all($fileStr);

  foreach ($tokens as $token) {
    if (is_array($token)) {
      echo '>> '. token_name($token[0]) ." -- ". $token[1] ."\n";
    }
    else {
      echo '>> '. $token ."\n";
    }
  }
}

function extract_variable_hard_code() {
  $fileStr = file_get_contents('/Users/danithaca/Development/drupal7/sites/d7dev1.localhost/settings.php');
  $tokens = token_get_all($fileStr);
  $code = '';

  $phase = 'skip';
  foreach ($tokens as $token) {
    if (is_array($token) && $token[0] == T_VARIABLE && $token[1] == '$databases') {
      $phase = 'accept';
      $code .= $token[1];
    }
    else if ($phase == 'accept') {
      // processing variables.
      $code .= is_array($token) ? $token[1] : $token;
      // the first ; marks the end of variable definition.
      if ($token == ';') {
        $phase = 'skip';
        $code .= "\n";
      }
    }
  }

  echo $code;
}

function extract_variable($file, $var_name) {
  $content = file_get_contents($file);
  $tokens = token_get_all($content);
  $code = '';

  $phase = 'skip';
  foreach ($tokens as $token) {
    if (is_array($token) && $token[0] == T_VARIABLE && $token[1] == $var_name) {
      $phase = 'accept';
      $code .= $token[1];
    }
    else if ($phase == 'accept') {
      $code .= is_array($token) ? $token[1] : $token;
      if ($token == ';') {
        $phase = 'skip';
        $code .= "\n";
      }
    }
  }

  return $code;
}

//extract_variable('/Users/danithaca/Development/drupal7/sites/d7dev1.localhost/settings.php', '$databases');
print_tokens();
//remove_comments();