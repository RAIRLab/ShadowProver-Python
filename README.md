# ShadowProver Python Interface

A python interface to ShadowProver. Requires a ShadowProver container to be running. Note that the dependency Py4j does not support Python versions >3.9.

## ShadowProver Docker Setup

1. Clone the ShadowProver repository.
2. Within the ShadowProver repository, build the shadowprover image `docker build -t shadowprover .`
3. Run the shadowprover docker container `docker run -p 25333:25333 shadowprover`

## Python Installation

1. Set up a virtual environment via the method of your choice.
2. Once within your virtual environment, within this repository
install the dependencies via `pip install -r requirements.txt`
3. Test to make sure interface works by `python example.py`

