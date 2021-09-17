# kafka-project
### This project requires kafka server. Please make sure your Kafka broker service and ZooKeeper service are started.
#### If you don't have them please install them. 
* STEP 1: GET KAFKA
Download the latest Kafka release and extract it:
```
$ tar -xzf kafka_2.13-2.8.0.tgz
$ cd kafka_2.13-2.8.0
```
* STEP 2: START THE KAFKA ENVIRONMENT
NOTE: Your local environment must have Java 8+ installed.
```
# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties
```

# Let's start
### Clone this repo then go to the kafka-project folder ```cd kafka-project```
### Decompress dataset which is called ```data.json.zip```
### Create python virtual environment and install packages.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Run db.py file - it will create tables in sqlite database called testdb.db
##### Note: if there is testdb.db file in this folder, it will remove it then create again.
```python db.py```

### Run producer in new terminal 
```
source venv/bin/activate
python producer.py
```

### Run consumer in new terminal
```
source venv/bin/activate
python consumer.py
```



