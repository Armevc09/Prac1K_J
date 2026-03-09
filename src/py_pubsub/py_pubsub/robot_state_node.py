import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import String

class MinimalSubscriber(Node): 

    def __init__(self):
        super().__init__('minimal_subscriber')

        self.normal = True

        self.subscription = self.create_subscription(
            Float32,
            'robot_velocity',
            self.listener_callback,
            10)
        ###------------
        self.subscription2 = self.create_subscription(
            Float32,
            'robot_batery',
            self.listener_callback2,
            10)
        self.subscription 
        self.subscription2

    def listener_callback(self, msg):
        if msg.data > 2.0:
            self.get_logger().info('OVER SPEED')
            self.normal = False
        else:
            self.normal = True
    
    def listener_callback2(self, msg):
        if msg.data < 20.0 and msg.data > 10.1:
            self.get_logger().info('LOW BATERY')
            self.normal = False
        elif msg.data < 10.0:
            self.get_logger().info('CRITICAL')
            self.normal = False
        elif self.normal == True:
            self.get_logger().info('NORMAL')
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()