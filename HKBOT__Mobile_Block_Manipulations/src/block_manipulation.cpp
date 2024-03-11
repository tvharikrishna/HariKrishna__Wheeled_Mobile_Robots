#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Int32MultiArray.h>
#include <std_msgs/ColorRGBA.h>
#include <thread>
#include <chrono>

class RosRobot {
public:
    
    RosRobot() {
        // Initialize ROS node handles and publishers
        ros::NodeHandle nh;
        motion_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
        servo_pub = nh.advertise<std_msgs::Int32MultiArray>("/servo_cmd", 10);
        light_pub = nh.advertise<std_msgs::ColorRGBA>("/light_cmd", 10);
    }

    void set_robot_velocity(double linear_x, double linear_y, double angular_z) {
        geometry_msgs::Twist msg;
        msg.linear.x = linear_x;
        msg.linear.y = linear_y;
        msg.angular.z = angular_z;
        motion_pub.publish(msg);
    }

    void set_servo_angles(const std::vector<int>& angles) {
        std_msgs::Int32MultiArray msg;
        msg.data = angles;
        servo_pub.publish(msg);
    }

    void set_light_color(uint8_t r, uint8_t g, uint8_t b, uint8_t a = 0xff) {
        std_msgs::ColorRGBA msg;
        msg.r = r;
        msg.g = g;
        msg.b = b;
        msg.a = a; // alpha channel, for transparency (if supported)
        light_pub.publish(msg);
    }

private:
    ros::Publisher motion_pub;
    ros::Publisher servo_pub;
    ros::Publisher light_pub;
};

class RobotController {
public:
    RobotController() : bot(new RosRobot()) {}

        Robot() : bot(new Rosmaster()) {}

    void car_motion(double V_x, double V_y, double V_z) {
        double speed_x = V_x / 10.0;
        double speed_y = V_y / 10.0;
        double speed_z = V_z / 10.0;
        bot->set_car_motion(speed_x, speed_y, speed_z);
    }

    void move_servos(int angle1, int angle2, int angle3, int angle4, int angle5, int angle6) {
        std::vector<int> angles = {angle1, angle2, angle3, angle4, angle5, angle6};
        bot->set_uart_servo_angle_array(angles);
    }

    void set_rgb_color(int r, int g, int b) {
        bot->set_colorful_lamps(0xff, r, g, b);
    }

    void turn_on_rgb(int r, int g, int b) {
        set_rgb_color(r, g, b);
    }

    void turn_off_rgb() {
        bot->set_colorful_lamps(0xff, 0, 0, 0);
    }

    // Method to include all servo movements for the robot's sequence of actions
    void perform_actions() {
        // STEP 0: Flashing green lights as it's safe
        turn_on_rgb(0, 255, 0);

        // STEP 1: With green lights, robot moves forward
        bot->set_car_motion(0.2, 0, 0);
        std::this_thread::sleep_for(std::chrono::seconds(4));
        bot->set_car_motion(0, 0, 0);

        // STEP 2: Flashing red lights, since robotic arm is in action
        turn_on_rgb(255, 0, 0);

        // STEP 3: Pick and place the block on robot

        // From POSITION: Arm Start --> POSITION: Hold the block w/ end effector  
        move_servos(0, 180, 0, 0, 90, 40);
        move_servos(90, 180, 0, 10, 90, 40);
        move_servos(90, 120, 50, 10, 90, 40);
        move_servos(90, 90, 50, 5, 90, 40);
        time.sleep(0.3);
        move_servos(90, 30, 90, 1, 90, 40);
        time.sleep(0.3);
        move_servos(90, 0, 90, 0, 100, 40);
        time.sleep(0.7);
        move_servos(90, 0, 90, 0, 100, 150);
        time.sleep(1);

        // From POSITION: End Effector w/ Block --> POSITION: Read to Place on Robot
        move_servos(90, 0, 90, 0, 100, 150);
        move_servos(90, 20, 80, 2, 98, 150);
        move_servos(90, 80, 60, 8, 92, 150);
        move_servos(90, 100, 55, 9, 91, 150);
        move_servos(90, 120, 50, 10, 90, 150);
        time.sleep(1);

        // From POSITION: Place Block on Chassis
        move_servos(180, 120, 50, 10, 90, 150);
        time.sleep(1);
        move_servos(180, 180, 0, 0, 90, 150);
        time.sleep(1);

        // GRIPPER PLACEING THE BLOCK - BLOCK IN CONTACT WITH ROBOT  
        move_servos(180, 120, 0, 0, 90, 150);
        time.sleep(0.5);
        move_servos(177, 110, 0, 0, 90, 150);
        time.sleep(0.5);
        move_servos(177, 100, 0, 0, 90, 150);
        time.sleep(1);

        // GRIPPER PUSHING FOR SPACE AND RETURNING BACK
        move_servos(177, 90, 10, 0, 90, 150);
        time.sleep(0.8);
        move_servos(177, 80, 20, 0, 90, 150);
        time.sleep(0.8);
        move_servos(177, 75, 30, 0, 90, 150);
        time.sleep(0.8);
        move_servos(177, 70, 35, 0, 90, 150);
        time.sleep(1);
        
        // UNHOCK THE END EFFECTOR 
        move_servos(177, 70, 35, 0, 90, 80);
        time.sleep(1);

        // RETURN TO INITIAL ROBOTIC ARM POS
        move_servos(177, 80, 20, 0, 90, 80);
        time.sleep(1);
        move_servos(177, 90, 10, 0, 90, 80);
        time.sleep(0.8);
        move_servos(177, 100, 0, 0, 90, 80);
        time.sleep(0.3);
        move_servos(177, 110, 0, 0, 90, 80);
        time.sleep(0.3);
        move_servos(180, 120, 0, 0, 90, 80);
        time.sleep(0.3);
        move_servos(90, 90, 90, 0, 90, 40);
        time.sleep(0.3);
        move_servos(0, 180, 0, 0, 90, 40);
    }

private:
    std::unique_ptr<RosRobot> bot;
};

int main(int argc, char **argv) {
    // Initialize the ROS system
    ros::init(argc, argv, "robot_controller");
    RobotController robot;

    // Call methods on the robot object to perform actions
    robot.perform_actions();
    return 0;

    ros::spin();
    return 0;
}
