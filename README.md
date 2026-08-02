# Async Edge Sensors

A lightweight, asynchronous hardware interface library bridging complex sensor arrays (I2C/SPI) with modern `asyncio` Python environments for edge devices (Raspberry Pi, ESP32).

## Why this exists
Most sensor libraries (like `smbus2` or Adafruit's standard CircuitPython libs) use blocking I/O. When reading from multiple sensors, this freezes the entire event loop, causing latency spikes in robotics and home automation setups.

This library provides a true `asyncio` compatible thread-safe wrapper for I2C and SPI buses, which is essential for continuous data logging in edge computing without blocking other concurrent asynchronous tasks.

## Installation
*(Currently in beta - PyPI release pending)*
```bash
git clone [https://github.com/YOUR_USERNAME/async-edge-sensors.git](https://github.com/YOUR_USERNAME/async-edge-sensors.git)
cd async-edge-sensors
pip install -e .
