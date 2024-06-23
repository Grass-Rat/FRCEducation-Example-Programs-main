import wpilib

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.left_motor = wpilib.SparkMAXMotorController(1)
        self.right_motor = wpilib.SparkMAXMotorController(2)

    def teleopPeriodic(self):
        left_stick = self.driver_controller.getLeftY()
        right_stick = self.driver_controller.getRightY()
        self.left_motor.set(-left_stick)
        self.right_motor.set(right_stick)

if __name__ == "__main__":
    wpilib.run(Robot)