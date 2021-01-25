# scurri-zipcode
This library supports validating post codes from UK.

## Install
`pip install scurri_zipcode`

## Usage
To check whether a post code is valid or not:
```
from scurri_zipcode.functions import is_valid

is_valid('EC1A 1BB')
# returns True
```

To format a valid post code:
```
from scurri_zipcode.functions import format

format('ec1a 1bb')
# returns EC1A 1BB

format('EC1A 111')
# raises an exception because inward code is invalid
```