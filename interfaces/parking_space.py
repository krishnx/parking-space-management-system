from abc import ABC, abstractmethod

from interfaces.vehicle import Vehicle


class ParkingSpace(ABC):
    @abstractmethod
    def __init__(self, space_id, size):
        self.space_id = space_id
        self.size = size
        self._vehicle: Vehicle | None = None

    @property
    def is_available(self):
        return self._vehicle is None

    @abstractmethod
    def can_fit(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def park(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def retrieve(self):
        pass
