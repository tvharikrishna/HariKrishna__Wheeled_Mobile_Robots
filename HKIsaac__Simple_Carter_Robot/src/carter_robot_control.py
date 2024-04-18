import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

msg = """
Control Your Robot!
---------------------------
Moving around:
   w
a  s  d
w: move forward
s: move backward
a: turn left
d: turn right

Press CTRL-C to quit the program.
"""

moveBindings = {
    'w': (1, 0),   # Move forward
    's': (-1, 0),  # Move backward
    'a': (0, 1),   # Turn left
    'd': (0, -1),  # Turn right
}

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed, turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('robot_teleop')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)

    # Linear velocity (m/s)
    speed = 0.2 

    # Angular velocity (rad/s)
    turn = 0.1   

    try:
        print(msg)
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                twist = Twist()
                twist.linear.x = x*speed
                twist.angular.z = th*turn
                pub.publish(twist)
                print(vels(speed, turn))
            else:
                if (key == '\x03'):
                    break
                
    except Exception as e:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        pub.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
