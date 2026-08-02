import asyncio
import smbus2

class AsyncI2CBus:
    """Thread-safe asynchronous wrapper for SMBus/I2C operations."""
    
    def __init__(self, bus_number=1):
        self.bus_number = bus_number
        self._bus = smbus2.SMBus(self.bus_number)
        self._lock = asyncio.Lock()

    async def read_byte_data(self, address, register):
        async with self._lock:
            return await asyncio.to_thread(self._bus.read_byte_data, address, register)

    async def write_byte_data(self, address, register, value):
        async with self._lock:
            await asyncio.to_thread(self._bus.write_byte_data, address, register, value)
            
    async def read_i2c_block_data(self, address, register, length):
        async with self._lock:
            return await asyncio.to_thread(self._bus.read_i2c_block_data, address, register, length)
            
    def close(self):
        self._bus.close()
