from abc import ABC, abstractmethod

from interfaces.vehicle import Vehicle


class ParkingSpaceManagementSystem(ABC):
    @abstractmethod
    def park(self, vehicle: Vehicle) -> str:
        pass

    @abstractmethod
    def retrieve(self, vehicle_id: str) -> Vehicle:
        pass
