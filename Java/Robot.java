package frc.robot;

import edu.wpi.first.wpilibj.TimedRobot;
import edu.wpi.first.wpilibj.command.Command;
import edu.wpi.first.wpilibj.command.Subsystem;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;

/**
 * This is the main robot class that extends TimedRobot.
 * It controls the robot's movement and autonomous mode.
 */
public class Robot extends TimedRobot {
    // Create a Drivetrain subsystem to control the robot's movement
    private Drivetrain drivetrain;
    // Create a Command to drive the robot in arcade mode
    private Command driveArcade;

    /**
     * This method is called when the robot is initialized.
     * It sets up the Drivetrain subsystem and the driveArcade command.
     */
    @Override
    public void robotInit() {
        drivetrain = new Drivetrain();
        driveArcade = new DriveArcade(drivetrain);
        drivetrain.setDefaultCommand(driveArcade);
    }

    /**
     * This method is called periodically during teleop mode.
     * It gets the joystick input and drives the robot using the arcadeDrive method.
     */
    @Override
    public void teleopPeriodic() {
        // Get the joystick input
        Joystick driverController = new Joystick(Constants.DRIVER_CONTROLLER);
        double moveSpeed = driverController.getY();
        double rotateSpeed = driverController.getX();

        // Drive the robot
        drivetrain.arcadeDrive(moveSpeed, rotateSpeed);
    }

    /**
     * This method is called when the autonomous mode is initialized.
     * It schedules the autonomous command to run.
     */
    @Override
    public void autonomousInit() {
        // Get the autonomous command from the RobotContainer
        Command autonomousCommand = RobotContainer.getAutonomousCommand();

        // Schedule the autonomous command
        if (autonomousCommand!= null) {
            autonomousCommand.schedule();
        }
    }
}

/**
 * This is the Drivetrain subsystem class.
 * It controls the robot's movement using the DifferentialDrive class.
 */
class Drivetrain extends Subsystem {
    private DifferentialDrive differentialDrive;

    public Drivetrain() {
        // Initialize the Talons
        Talon leftFrontTalon = new Talon(0);
        Talon leftBackTalon = new Talon(1);
        Talon rightFrontTalon = new Talon(2);
        Talon rightBackTalon = new Talon(3);

        // Initialize the SpeedControllerGroups
        SpeedControllerGroup leftMotors = new SpeedControllerGroup(leftFrontTalon, leftBackTalon);
        SpeedControllerGroup rightMotors = new SpeedControllerGroup(rightFrontTalon, rightBackTalon);

        // Initialize the DifferentialDrive
        differentialDrive = new DifferentialDrive(leftMotors, rightMotors);
    }

    public void arcadeDrive(double moveSpeed, double rotateSpeed) {
        differentialDrive.arcadeDrive(moveSpeed, rotateSpeed);
    }
}

/**
 * This is the DriveArcade command class.
 * It drives the robot in arcade mode using the Drivetrain subsystem.
 */
class DriveArcade extends Command {
    private Drivetrain drivetrain;

    public DriveArcade(Drivetrain drivetrain) {
        this.drivetrain = drivetrain;
        requires(drivetrain);
    }

    @Override
    protected void execute() {
        // Get the joystick input
        Joystick driverController = new Joystick(Constants.DRIVER_CONTROLLER);
        double moveSpeed = driverController.getY();
        double rotateSpeed = driverController.getX();

        // Drive the robot
        drivetrain.arcadeDrive(moveSpeed, rotateSpeed);
    }

    @Override
    protected boolean isFinished() {
        return false;
    }
}
