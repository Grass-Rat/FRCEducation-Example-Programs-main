# This example shows a TimedRobot class that controls a robot's movement using two ctre.PWM motors. 

# The robotInit() method initializes the motors
# The autonomousPeriodic() and teleopPeriodic() methods run the autonomous and teleop code, respectively.

import wpilib
import wpilib.drive

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.leftDrive = wpilib.PWMSparkMax(0)
        self.rightDrive = wpilib.PWMSparkMax(1)
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.leftDrive, self.rightDrive
        )
        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer()

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        self.rightDrive.setInverted(True)

    def autonomousInit(self):
        """
        This function is called once each time the robot enters autonomous mode.
        """
        self.timer.restart()

    def autonomousPeriodic(self):
        """
        This function is called periodically during autonomous.
        """
        if self.timer.get() < 2.0:
            self.robotDrive.arcadeDrive(0.5, 0.0)
        else:
            self.robotDrive.stopMotor()

    def teleopInit(self):
        """
        This function is called once each time the robot enters teleoperated mode.
        """

    def teleopPeriodic(self):
        """
        This function is called periodically during teleoperated mode.
        """
        self.robotDrive.arcadeDrive(-self.controller.getLeftY(),
                                   -self.controller.getRightX())

    def testInit(self):
        """
        This function is called once each time the robot enters test mode.
        """

    def testPeriodic(self):
        """
        This function is called periodically during test mode.
        """
        pass
