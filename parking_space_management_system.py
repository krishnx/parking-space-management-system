from interfaces.vehicle import Vehicle
from interfaces.parking_space_management_system import ParkingSpaceManagementSystem
from parking_space import ParkingSpaceImpl


class ParkingManagementSystem(ParkingSpaceManagementSystem):
    def __init__(self, spaces: list[ParkingSpaceImpl]):
        self.spaces = spaces
        self.vehicle_to_space = {}

    def park(self, vehicle: Vehicle) -> str:
        if vehicle.vehicle_id in self.vehicle_to_space:
            raise ValueError("Vehicle is already parked")

        suitable_spaces = [
            space
            for space in self.spaces
            if space.can_fit(vehicle)
        ]

        if not suitable_spaces:
            raise ValueError("No suitable parking space available")

        space = min(
            suitable_spaces,
            key=lambda space: space.size.value
        )

        space.park(vehicle)
        self.vehicle_to_space[vehicle.vehicle_id] = space

        return space.space_id

    def retrieve(self, vehicle_id: str) -> Vehicle:
        space = self.vehicle_to_space.get(vehicle_id)

        if space is None:
            raise ValueError("Vehicle is not parked")

        vehicle = space.retrieve()
        del self.vehicle_to_space[vehicle_id]

        return vehicle
