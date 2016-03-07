<?php

include __DIR__ . '/../vendor/autoload.php';

use Silex\Application;

$app = new Application(['debug' => true]);

$app->register(new Silex\Provider\TwigServiceProvider(), array(
    'twig.path' => __DIR__.'/../views',
));

$app['modbusReader'] = $app->protect(function() {
    $client = new \GearmanClient();
    $client->addServer();
    $handle = $client->doNormal('modbusReader', 'modbusReader');
    $returnCode = $client->returnCode();
    if ($returnCode != \GEARMAN_SUCCESS) {
        throw new \Exception($this->client->error(), $returnCode);
    } else {
        return json_decode($handle, true);
    }
});

$app->get("/", function(Application $app) {
    return $app['twig']->render('home.twig', $app['modbusReader']());
});

$app->run();