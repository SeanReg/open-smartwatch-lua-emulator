# Opensource Smartwatch Lua Emulator

This is a simple Python emulator capable of running/displaying OSW Lua based apps. This allows apps to be created and tested on a PC before integrated into the Osw firmware.


## Setting up the emulator

### Prerequisites
Python 3 is required and can be downloaded from here: https://www.python.org/download/releases/3.0/

### Install Dependencies

Navigate to the Lua Emulator folder and run the following to install the Python dependencies:

```
pip install -r requirements.txt
```

## Running a Lua Script


```
python emulate.py <SCRIPT NAME>
```

### Running the example

Included is an `example.lua` script. This script is a Lua port of `stopwatch.cpp`

```
python emulate.py example.lua
```

## Supported HAL Functions
- btn1Down, btn2Down, btn3Down
  - These are mapped to keyboard buttons 1, 2, 3
- getCanvas()
  - This will return a Python Canvas implementation which supports most drawing and printing functions
- getLocalTime()