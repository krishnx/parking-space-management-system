from enums import Size
from vehicle import VehicleImpl
from parking_space import ParkingSpaceImpl
from parking_space_management_system import ParkingManagementSystem


def main():
    spaces = [
        ParkingSpaceImpl("S1", Size.SMALL),
        ParkingSpaceImpl("S2", Size.SMALL),
        ParkingSpaceImpl("M1", Size.MEDIUM),
        ParkingSpaceImpl("M2", Size.MEDIUM),
        ParkingSpaceImpl("L1", Size.LARGE),
        ParkingSpaceImpl("L2", Size.LARGE),
    ]

    system = ParkingManagementSystem(spaces)

    v1 = VehicleImpl("V1", Size.SMALL)
    v2 = VehicleImpl("V2", Size.MEDIUM)
    v3 = VehicleImpl("V3", Size.LARGE)
    v4 = VehicleImpl("V4", Size.SMALL)

    print("Parking vehicle V1 (SMALL):", system.park(v1))
    print("Parking vehicle V2 (MEDIUM):", system.park(v2))
    print("Parking vehicle V3 (LARGE):", system.park(v3))
    print("Parking vehicle V4 (SMALL):", system.park(v4))

    print("Retrieving vehicle V1:", system.retrieve("V1").vehicle_id)
    print("Retrieving vehicle V2:", system.retrieve("V2").vehicle_id)

    print("Parking V1 again:", system.park(v1))
    print("All operations completed successfully!")


if __name__ == "__main__":
    main()
