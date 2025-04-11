# Python Client

This project contains a Python 3 application that subscribes to a topic on a Confluent Cloud Kafka cluster and sends a sample message, then consumes it and prints the consumed record to the console.

## Prerequisites

This project assumes that you already have:
- A Linux/UNIX environment. If you are using Windows, see the tutorial below in the "Learn More" section to download WSL.
- Python 3 installed. The template was last tested against Python 3.13.1.

The instructions use `virtualenv` but you may use other virtual environment managers like `venv` if you prefer.

## Check compatibility

Go through the [Built Distributions](https://pypi.org/project/confluent-kafka/#files) list and make sure that a distribution with the combination of your Python version, OS, and system architecture exists. If not, you will need to switch to a different Python version.

## Installation

Create and activate a Python environment, so that you have an isolated workspace:

```shell
virtualenv env
source env/bin/activate
```

Install the dependencies of this application:

```shell
pip3 install -r requirements.txt
```

If the above command fails with an error message indicating that librdkafka cannot be found, please double check that you've completed the "Check compatibility" step above.

## Usage

You can execute the consumer script by running:

```shell
python3 client.py
```

## Learn more

- For the Python client API, check out the [kafka-clients documentation](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
- Check out the full [getting started tutorial](https://developer.confluent.io/get-started/python/)

