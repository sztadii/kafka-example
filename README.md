# kafka-example
A simple Kafka app with easy to set up configuration

## Problem to solve:

When you need to deliver a new feature where you need to use Kafka broker to communicate <br />
sometimes we need to set up our own local env.
It can be painful to find proper Kafka and Zookeeper configuration. <br />
So this repo can solve your problem, cause everything you will need to do is run just a single command. <br />
It will create Kafka, Zookeeper instances and WebUI that helps you to monitor new events and their messages <br />
Thanks to obsidiandynamics company <br />
Enjoy :)

## Hot to run
```
docker-compose up
```

You will create all required containers
Your Kafka instance will run on `9092` port and web-ui on `9000`
