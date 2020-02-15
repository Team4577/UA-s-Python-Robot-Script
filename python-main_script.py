// To complete the VEXcode V5 Text project upgrade process, please follow the
// steps below.
// 
// 1. You can use the Robot Configuration window to recreate your V5 devices
//   - including any motors, sensors, 3-wire devices, and controllers.
// 
// 2. All previous code located in main.cpp has now been commented out. You
//   will need to migrate this code to the new "int main" structure created
//   below and keep in mind any new device names you may have set from the
//   Robot Configuration window. 
// 
// If you would like to go back to your original project, a complete backup
// of your original (pre-upgraded) project was created in a backup folder
// inside of this project's folder.

// ---- START VEXCODE CONFIGURED DEVICES ----
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;




//#region config_globals
vex::brain Brain;
vex::motor motor_l1(vex::PORT20, vex::gearSetting::ratio18_1, false);
vex::motor motor_r1(vex::PORT11, vex::gearSetting::ratio18_1, true);
vex::motor motor_l2(vex::PORT10, vex::gearSetting::ratio18_1, false);
vex::motor motor_r2(vex::PORT1, vex::gearSetting::ratio18_1, true);
vex::motor motor_as1(vex::PORT9, vex::gearSetting::ratio36_1, false);
vex::motor motor_as2(vex::PORT2, vex::gearSetting::ratio36_1, true);
vex::motor motor_ah1(vex::PORT19, vex::gearSetting::ratio36_1, false);
vex::motor motor_ah2(vex::PORT12, vex::gearSetting::ratio36_1, true);

vex::motor motor_ap(vex::PORT1, vex::gearSetting::ratio36_1, false);  



vex::controller con(vex::controllerType::primary);


//#endregion config_globals


// Creates a competition object that allows access to Competition methods.
vex::competition Competition;

void pre_auton() {
    // All activities that occur before competition start
    // Example: setting initial positions

}

void autonomous() {
    // Place autonomous code here

}

void drivercontrol() {
    // Place drive control code here, inside the loop
    double left_power = 0; //Left-power
    double right_power = 0; //Right-power


    while (true) {
        while(con.ButtonR1.pressing()) {

          left_power = con.Axis3.position();
          right_power = con.Axis2.position();

          motor_l1.spin(vex::directionType::fwd, left_power, velocityUnits::rpm);
          motor_r1.spin(vex::directionType::fwd, right_power, velocityUnits::rpm);

        }
        
        left_power = 0;
        right_power = 0;
        motor_l1.spin(vex::directionType::fwd, left_power, velocityUnits::rpm);
        motor_r1.spin(vex::directionType::fwd, right_power, velocityUnits::rpm);

        // This is the main loop for the driver control.
        // Each time through the loop you should update motor
        // movements based on input from the controller.
        
        
        
        //joystick is being wasted on forward/backward movement
         if (con.ButtonUp.pressing()) {
        motor_as1.spin(vex::directionType::fwd, 100, velocityUnits::rpm);
        motor_as2.spin(vex::directionType::fwd, 100, velocityUnits::rpm);
    }
    
    if (con.ButtonDown.pressing()) {
        motor_as1.spin(vex::directionType::rev, 100, velocityUnits::rpm);
        motor_as2.spin(vex::directionType::rev, 100, velocityUnits::rpm);
    }
    if (con.ButtonA.pressing()) {
        motor_ah1.spin(vex::directionType::fwd, 100, velocityUnits::rpm);
    motor_ah2.spin(vex::directionType::fwd, 100, velocityUnits::rpm);
    }
     if (con.ButtonY.pressing()) {
        motor_ah1.spin(vex::directionType::rev, 100, velocityUnits::rpm);
    motor_ah2.spin(vex::directionType::rev, 100, velocityUnits::rpm);
    }

    }
    
   
    
    
    
    
}

int main() {
    // Do not adjust the lines below

    // Set up (but don't start) callbacks for autonomous and driver control periods.
    Competition.autonomous(autonomous);
    Competition.drivercontrol(drivercontrol);

    // Run the pre-autonomous function.
    pre_auton();

    // Robot Mesh Studio runtime continues to run until all threads and
    // competition callbacks are finished.
}


