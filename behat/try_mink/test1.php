<?php

require_once(__DIR__ .'/../vendor/autoload.php');

// Choose a Mink driver. More about it in later chapters.
$driver = new \Behat\Mink\Driver\GoutteDriver();
//$driver = new \Behat\Mink\Driver\Selenium2Driver();

$session = new \Behat\Mink\Session($driver);

// start the session
$session->start();

$session->visit('http://google.com');

// get the current page URL:
echo $session->getCurrentUrl();

// use history controls:
$session->reload();
//$session->back();
//$session->forward();


// set cookie:
$session->setCookie('cookie name', 'value');
// get cookie:
echo $session->getCookie('cookie name');
// delete cookie:
$session->setCookie('cookie name', null);

echo $session->getStatusCode();


// evaluate JS expression:
//echo $session->evaluateScript(
//  "return 'something from browser';"
//);