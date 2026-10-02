from abc import ABC, abstractmethod


class Vehicle(ABC):
    @property
    @abstractmethod
    def vehicle_id(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass
