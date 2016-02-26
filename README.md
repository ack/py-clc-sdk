py-clc-sdk
==========================

[![Build Status](https://travis-ci.org/CenturyLinkCloud/py-clc-sdk.png?branch=master)](https://travis-ci.org/CenturyLinkCloud/py-clc-sdk)
[![Requires.io](https://requires.io/github/CenturyLinkCloud/py-clc-sdk/requirements.svg?branch=master)](https://requires.io/github/CenturyLinkCloud/py-clc-sdk/requirements?branch=master)

Python SDK for CenturyLinkCloud

## Usage

```python

import clc
config = clc.Config(username, password, alias, abc=def)
client = clc.Client(config)
client.v2.authenticate()

```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.
