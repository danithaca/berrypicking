<?php
/**
 * @file
 * This is the math helper functions file
 */

class Math {
  
  // this is the all-in-one function of mean(), covariance(), covariance_matrix() and correlation_matrix()
  // intended to be more efficient.
  // $matrix has to be indexed by [0..m][0..n]
  // NOTE: $matrix WILL BE MODIFIED to save mem space!!!
  static function &fast_correlation_matrix(&$matrix) {
    if (!isset($matrix) || !is_array($matrix)) {
      return null;
    }
    
    $m = count($matrix);
    $n = count($matrix[0]); // assume the matrix has the same width
    foreach($matrix as &$vector) {
      if (count($vector) != $n) {
        return null;
      }
      // adjust each element in the vector by the mean.
      $mean = array_sum($vector) / $n;
      for ($i=0; $i<$n; $i++) {
        $vector[$i] = $vector[$i] - $mean;
      }
    }
    
    $cov_matrix = array();
    $variance = array();
    for ($v1=0; $v1<$m; $v1++) {
      for ($v2=$v1; $v2<$m; $v2++) {
        $vector_1 = &$matrix[$v1];
        $vector_2 = &$matrix[$v2];
        for ($i=0; $i<$n; $i++) {     
          $variance[$i] = $vector_1[$i] * $vector_2[$i];
        }
        $cov = array_sum($variance) / $n;
        $cov_matrix[$v1][$v2] = $cov;
        $cov_matrix[$v2][$v1] = $cov;
      }
    }
    
    $vector_diagnal = array();
    for ($i=0; $i<$m; $i++) {
      $vector_diagnal[$i] = sqrt($cov_matrix[$i][$i]);
    }
    for ($v1=0; $v1<$m; $v1++) {
      for ($v2=$v1; $v2<$m; $v2++) {
        $cov_matrix[$v1][$v2] = $cov_matrix[$v1][$v2] / ($vector_diagnal[$v1] * $vector_diagnal[$v2]);
        $cov_matrix[$v2][$v1] = $cov_matrix[$v1][$v2];
      }
    }
    return $cov_matrix;
  }
  
  static function mean($vector) {
    if (!isset($vector) || !is_array($vector)) {
      return null;
    }
    return array_sum($vector) / count($vector);
  }
  
  static function covariance($vector_a, $vector_b) {
    if (!isset($vector_a) || !is_array($vector_a) || !isset($vector_b) || !is_array($vector_b)) {
      return null;
    }
    if (count($vector_a) != count($vector_b)) {
      return null;
    }
    $n = count($vector_a);
    $mean_a = Math::mean($vector_a);
    $mean_b = Math::mean($vector_b);
    $variance = array();
    for ($i=0; $i<$n; $i++) {     
      $variance[] = ($vector_a[$i] - $mean_a) * ($vector_b[$i] - $mean_b);
    }
    return Math::mean($variance);
  }
  
  static function covariance_matrix($matrix) {
    if (!isset($matrix) || !is_array($matrix)) {
      return null;
    }
    $m = count($matrix);
    $n = count($matrix[0]); // assume the matrix has the same width
    $cov_matrix = array();
    for ($v1=0; $v1<$m; $v1++) {
      for ($v2=$v1; $v2<$m; $v2++) {
        $vector_1 = $matrix[$v1];
        $vector_2 = $matrix[$v2];
        if (count($vector_1)!=$n || count($vector_2)!=$n) {
          return null;
        }
        $cov = Math::covariance($vector_1, $vector_2);
        $cov_matrix[$v1][$v2] = $cov;
        $cov_matrix[$v2][$v1] = $cov;
      }
    }
    return $cov_matrix;
  }
  
  static function correlation_matrix($matrix) {
    $cov_matrix = Math::covariance_matrix($matrix);
    $m = count($cov_matrix);
    $vector_diagnal = array();
    for ($i=0; $i<$m; $i++) {
      if (count($cov_matrix) != $m) {
        return null;
      }
      $vector_diagnal[] = sqrt($cov_matrix[$i][$i]);
    }
    for ($v1=0; $v1<$m; $v1++) {
      for ($v2=$v1; $v2<$m; $v2++) {
        $cov_matrix[$v1][$v2] = $cov_matrix[$v1][$v2] / ($vector_diagnal[$v1] * $vector_diagnal[$v2]);
        $cov_matrix[$v2][$v1] = $cov_matrix[$v1][$v2];
      }
    }
    return $cov_matrix;
  }
}

function test_matrix() {
  $a = array(5,6,7,1,8,9,4);
  $b = array(0,5,8,1,9,4,5);
  $c = array(1,5,4,2,4,7,4);
  $m[] = $a;
  $m[] = $b;
  $m[] = $c;
  $cov_matrix = Math::correlation_matrix($m);
  print_r($cov_matrix);
}

test_matrix();