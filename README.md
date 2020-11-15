# Function Analyzer

## Index

1. Introduction 
2. Requirements
3. Installation 
4. Tests
5. Getting started


## Introduction

This project contains a function analyzer that allows to print function graphs on a given domain from expressions such 
as "xe2+1*(x-2)".


## Requirements

* System requirements

python >= 3.8 
pip >= 20.2.4

* Application requirements

Required python packages are listed on the requirements.txt file.


## Installation

To use the app, install the python dependencies:

~~~
pip install -r requirements.txt
~~~


## Tests

To test the application run one of the following commands:

~~~~
pytest tests
pytest tests/unit
pytest tests/integration
pytest tests/validation
~~~~


## Getting started

To print one function graph run the following command:

~~~~
python cli.py expression_string from_domain to_domain domain_step
~~~~

Where:

* expression_string is the expression whose function graph we want to print

* from_domain is the origin of the function graph domain

* to_domain is the end of the function graph domain

* domain_step is the interval between abscissas of the function graph
