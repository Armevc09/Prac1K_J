import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

class MinimalSubscriber(Node): 

    def __init__(self):
        super().__init__('minimal_subscriber')
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
            self.get_logger().info(f'ALERTA VELOCIDAD: {msg.data} m/s')
    
    def listener_callback2(self, msg):
        if msg.data < 20.0 and msg.data > 10.1:
            self.get_logger().info(f'ALERTA BATERIA: {msg.data} %')
        elif msg.data < 10.0:
            self.get_logger().info(f'CRITICAL BATERY: {msg.data} %')
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()