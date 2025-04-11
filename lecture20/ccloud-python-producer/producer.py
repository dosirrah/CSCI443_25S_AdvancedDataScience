from confluent_kafka import Producer
import json

# Set up the Kafka producer configuration
conf = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',  # Your Kafka endpoint
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'IYUBBTUXZD5ETGS6',  # Your API key
    'sasl.password': 'Eg4V2LXIGws8/tXXfYoKBrI/iA5oYbGP7DzMR+Gy5BqemMVAVVeNoxLe8coUUTuN' # secret
}

# Create the Kafka producer instance
producer = Producer(conf)

# Simulate reactor data (e.g., temperature and pressure)
data = {'temperature': 350, 'pressure': 5.5}

# Send data to Kafka topic 'fusion-topic'
producer.produce('TestTopic', key='core1', value=json.dumps(data))

# Wait for all messages to be delivered
producer.flush()

print(f"Sent data to 'TestTopic': {data}")

