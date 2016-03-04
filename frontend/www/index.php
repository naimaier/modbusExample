<?php

include __DIR__ . '/../vendor/autoload.php';

use Silex\Application;
use G\Gearman\Builder;

$app = new Application(['debug' => true]);

$app->register(new Silex\Provider\TwigServiceProvider(), array(
    'twig.path' => __DIR__.'/../views',
));

$app['modbusReader'] = $app->protect(function() {
    $client = Builder::createClient();
    $client->onSuccess(function ($response) {
        return $response;
    });

    return json_decode($client->doNormal('modbusReader'), true);
});

$app->get("/", function(Application $app) {
    return $app['twig']->render('home.twig', $app['modbusReader']());
});

$app->run();