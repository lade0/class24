# to create a class vehicle and create amn object of it to print max speed and mileage
class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
BMW=vehicle(250,18)
print("BMW max speed:",BMW.max_speed,"mileage:",BMW.mileage)