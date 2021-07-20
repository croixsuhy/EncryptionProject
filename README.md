# Encrpytion Project

This encryption project introduces data serializing (pickling) and data encryption.

To run this project, you need to install the latest version of [Python 3](https://python.org/) first.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the encryption package

```bash
pip install cryptography  # This package handles all of the data encryption
```

## Usage

```
Enter what you want to be encrypted and serialized: (Enter what you want encrypted)
```

```
Decrypt data? (Y/N/clear):

Y: decrypt and display data
N: display encrypted data
clear: clears data.txt

Note: time.txt holds seralized and encrypted data
```

```
Would you like to encrypt more? (Y/N)

Y: restarts program
N: stops program
```

## Key expiration

This program has a special feature; the key will expire

By default it expires after one minute, but you can change it to what ever you want in ```combiningboth.py```

```python
"""Lines 7-10"""

# Time to make key expire, change to whatever you want here
# If you set it to None it will never expire
# Time is in minutes
EXPIRATION_TIME = 1
```

## Special Thanks

Special thanks to [TheCoderSchool](https://www.thecoderschool.com/), a place where kids (like myself!) can learn how to code and develop.

## License

[MIT](https://choosealicense.com/licenses/mit/)
