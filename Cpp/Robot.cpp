#include <frc/TimedRobot.h>
#include <frc/drive/DifferentialDrive.h>
#include <frc/motorcontrol/MotorControllerGroup.h>
#include <frc/XboxController.h>

// Create a class for the robot's drivetrain
class RobotContainer {
public:
    RobotContainer() {
        // Initialize the left and right sides of the drivetrain
        leftMotor = new WPI_TalonFX(1);
        rightMotor = new WPI_TalonFX(2);

        // Create a motor controller group for the left and right sides
        leftDrive = new MotorControllerGroup(leftMotor);
        rightDrive = new MotorControllerGroup(rightMotor);

        // Create a differential drive object to control the robot's movement
        drivetrain = new DifferentialDrive(leftDrive, rightDrive);

        // Create an Xbox controller object to get input from the driver
        driverController = new XboxController(0);
    }

    // Set the left and right motor speeds
    void setMotorSpeeds(double leftSpeed, double rightSpeed) {
        leftMotor->Set(leftSpeed);
        rightMotor->Set(rightSpeed);
    }

private:
    // Motor controllers for the left and right sides of the drivetrain
    WPI_TalonFX* leftMotor;
    WPI_TalonFX* rightMotor;

    // Motor controller groups for the left and right sides of the drivetrain
    MotorControllerGroup* leftDrive;
    MotorControllerGroup* rightDrive;

    // Differential drive object to control the robot's movement
    DifferentialDrive* drivetrain;

    // Xbox controller object to get input from the driver
    XboxController* driverController;
};

class Robot : public frc::TimedRobot {
public:
    Robot() : frc::TimedRobot(10_ms) {} // Set the update rate to 10 ms

    void robotInit() override {
        // Initialize the robot container
        robotContainer = new RobotContainer();
    }

    void teleopPeriodic() override {
        // Get the left and right joystick values from the Xbox controller
        double leftJoystick = robotContainer->driverController->GetLeftY();
        double rightJoystick = robotContainer->driverController->GetRightY();


        // Set the motor speeds based on the joystick values
        robotContainer->setMotorSpeeds(leftJoystick, rightJoystick);
    }

private:
    // Robot container object to control the robot's subsystems
    RobotContainer* robotContainer;
};


// In this example, we create a RobotContainer class to control the robot's drivetrain. The RobotContainer constructor initializes the left and right motors, creates a motor controller group for each side, and creates a DifferentialDrive object to control the robot's movement. It also creates an XboxController object to get input from the driver.

// The Robot class extends TimedRobot and sets the update rate to 10 ms. In the robotInit method, we initialize the RobotContainer object. In the teleopPeriodic method, we get the left and right joystick values from the Xbox controller and set the motor speeds based on those values.

// This example uses a differential drive, where the left and right motors are used together to move the robot forward or backward. The DifferentialDrive object is used to control the robot's movement.

// Note that this example uses the WPILib C++ framework and requires a functioning Xbox controller connected to the robot's driver station.
