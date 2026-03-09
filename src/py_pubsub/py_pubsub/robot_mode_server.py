from more_interfaces.srv import AddNumbers

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddNumbers, 'clnt_srv', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        if request.mode == 0:
            response.result = "Manual"
        if request.mode == 1:
            response.result = "Autonomous"
        if request.mode == 2:
            response.result = "Safe mode"
        ###self.get_logger().info('Incoming request\na: %d' % (request.a))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()