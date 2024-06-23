import wpilib

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.motor = wpilib.SparkMotorController(1)
        self.sensor = wpilib.AnalogInput(0)

    def teleopPeriodic(self):
        value = self.sensor.getVoltage()
        error = self.setpoint - value
        output = self.kp * error
        self.motor.set(output)

if __name__ == "__main__":
    wpilib.run(Robot)