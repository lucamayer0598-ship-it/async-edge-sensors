import asyncio

class DummyTempSensor:
    """Example implementation of a sensor using the AsyncI2CBus."""
    
    def __init__(self, bus, address=0x76):
        self.bus = bus
        self.address = address
        self._calibration_data = None
        
    async def initialize(self):
        self._calibration_data = await self.bus.read_i2c_block_data(self.address, 0x88, 24)
        
    async def read_temperature(self):
        raw_data = await self.bus.read_byte_data(self.address, 0xFA)
        await asyncio.sleep(0.05)
        return 22.5 + (raw_data * 0.01)
