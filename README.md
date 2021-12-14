# kafka-example
A simple Kafka app with easy to set up configuration

## Problem to solve:

When you will need to deliver a new feature where a Kafka broker needs to be use. <br />
Sometimes you will need to set up a local env for that.
It can be painful to find a proper Kafka and Zookeeper configuration. <br />
So this repo can solve your problem just with a single command. <br />
It will create Kafka, Zookeeper and WebUI instances that helps you monitor new events and their messages <br />
Thanks to obsidiandynamics company <br />
Enjoy :)

## Hot to run
```
docker-compose up
```

You will create all required containers
Your Kafka instance will run on `9092` port and web-ui on `9000`
