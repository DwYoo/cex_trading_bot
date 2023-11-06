import asyncio
from abc import abstractmethod
import logging

class Market:
    market_data = {}

    async def stream(self):
        """
        Asynchronously start streaming market data.
        This method creates tasks for connecting to the market and printing market data periodically.
        """
        task1 = asyncio.create_task(self.aconnect())
        await asyncio.sleep(10)
        task2 = asyncio.create_task(self._aprint_market_data())
        await asyncio.gather(task1, task2)

    @abstractmethod
    async def aconnect(self):
        """
        An abstract method for connecting to the market. Subclasses should implement this method to connect to a specific market.
        """
        pass

    async def _aprint_market_data(self, time_interval: int = 5):
        """
        Asynchronously print market data periodically.

        :param time_interval: Time interval in seconds between prints.
        """
        while True:
            print(self.market_data)
            await asyncio.sleep(time_interval)