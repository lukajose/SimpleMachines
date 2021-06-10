
# Requirements

- docker-compose
- python3
- unix system, linux or mac should me fine

# How to run

To run the kafka containers do:
```
docker-compose up
```

You need to install python dependencies do:

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
