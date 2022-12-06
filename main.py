import time


class General:
    def __init__(self, model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag):
        self.model = model
        self.weight = weight
        self.acceleration = acceleration
        self.horsepower = horsepower
        self.max_torque = max_torque
        self.max_speed = max_speed
        self.brake_dist = brake_dist
        self.air_drag = air_drag


class Porsche911(General):
    def __init__(self, model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag, launch_control):
        super().__init__(model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag)
        self.launch_control = launch_control


class Bmw_m4(General):
    def __init__(self, model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag):
        super().__init__(model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag)


class Tesla_plaid(General):
    def __init__(self, model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag):
        super().__init__(model, acceleration, horsepower, max_torque, max_speed, weight, brake_dist, air_drag)


Porsche = Porsche911("Porsche 911 turbo s", 2.7, 650, 900, 360, 1650, 33, 0.23, "yes")
BMW = Bmw_m4("BMW M4", 3.5, 510, 700, 310, 1700, 39, 0.26)
Tesla = Tesla_plaid("Tesla Model S Plaid", 2.5, 1000, 1100, 250, 1900, 45, 0.29)


# def compare():
#     print("Porsche VS BMW VS Tesla")
#     p_points = 0
#     b_points = 0
#     t_points = 0
#     accel = [Porsche.acceleration, BMW.acceleration, Tesla.acceleration]
#     horsepower = [Porsche.horsepower, BMW.horsepower, Tesla.horsepower]
#     max_toque = [Porsche.max_torque, BMW.max_torque, Tesla.max_torque]
#     max_speed = [Porsche.max_speed, BMW.max_speed, Tesla.max_speed]
#     weight = [Porsche.weight, BMW.weight, Tesla.weight]
#     brake_dist = [Porsche.brake_dist, BMW.brake_dist, Tesla.brake_dist]
#     air_drag = [Porsche.air_drag, BMW.air_drag, Tesla.air_drag]
#
#
# compare()


def drag_race(distance):
    # distance = 1608
    distance_2 = distance
    distance_3 = distance

    while distance > 0 and distance_2 > 0 and distance_3:
        time.sleep(1)
        print(f"Porsche drives at {distance}")
        print(f"BMW drives at {distance_2}")
        print(f"Tesla drives at {distance_3}")
        print("_______________________")

        distance -= Porsche.max_speed
        distance_2 -= BMW.max_speed
        distance_3 -= Tesla.max_speed

        if distance < distance_2 and distance_3:
            print(f"The winner is {Porsche}")
        elif distance_2 < distance and distance_3:
            print(f"The winner is {BMW}")
        elif distance_3 < distance and distance_2:
            print(f"The winner is {Tesla}")
        else:
            print("Dues")


drag_race(1608)
