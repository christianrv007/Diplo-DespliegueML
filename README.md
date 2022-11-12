# todo list
This is a refactor project todo list

# Setup
* Create a virtual environment with:
```
python3 -m venv venv
```

* Activate the virtual environment

```
source venv/bin/activate
```

# Install the other libraries
Run the following command to install the other libraries.

```
pip install -r requirements.txt
```

# Tests

````
$ pytest tests/integration/ -v
````
````
tests/integration/test_integration.py::test_integration PASSED                                                                                [ 33%]
tests/integration/test_integration.py::test_integration_parametrize[5-5-5/4-3/4-5] PASSED                                                     [ 66%]
tests/integration/test_integration.py::test_integration_parametrize[8-7/5-15-3/8-137.475] PASSED                                              [100%]
````