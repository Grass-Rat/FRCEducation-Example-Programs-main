import wpilib

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.shoulder_motor = wpilib.SparkMotorController(1)
        self.elbow_motor = wpilib.SparkMotorController(2)
        self.shoulder_sensor = wpilib.AnalogInput(0)
        self.elbow_sensor = wpilib.AnalogInput(1)

    def teleopPeriodic(self):
        shoulder_value = self.shoulder_sensor.getVoltage()
        elbow_value = self.elbow_sensor.getVoltage()
        self.shoulder_motor.set(shoulder_value)
        self.elbow_motor.set(elbow_value)

if __name__ == "__main__":
    wpilib.run(Robot)