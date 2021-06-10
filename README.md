
# Requirements

- docker-compose
- python3
- unix system, linux or mac should be fine

# How to run

To run the kafka container and zookeper do:
```
docker-compose up
```
This will create the docker containers to run kafka, you will need another terminal to do the following:

You need to install the python dependencies do:

```
pip3 install -r requirements.txt
```

Then, for running the kafka consumer run:
```
python3 consumer.py
```

For running the kafka producer run:

```
python3 producer.py
```

The kafka producer at the moment produces 10 messages everytime is run with the same pageId and userId, obviously we can add more complex testing like random users and pages for further testing.
