import rclpy 
from rclpy.node import Node 

from std_msgs.msg import Float32 # Librería de msgs, uso de float

import random # Para simular datos del sensor ultrasónico


class MinimalPublisher(Node):  

    def __init__(self):
        super().__init__('minimal_publisher') 
        self.publisher_ = self.create_publisher(Float32, 'robot_velocity', 10) 
        self.publisher2_ = self.create_publisher(Float32, 'robot_batery', 10)
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.timer = self.create_timer(timer_period, self.timer_callback2)
                                    

    def timer_callback(self):
        msg = Float32() # Definir el tipo de la variable de mensaje
        # Generar un decimal entre 0.0 y 1.0  // numero_simple = random.random()

        # Generar un decimal en un rango específico
        lmInf = 0.0
        lmSup = 2.5
        msg.data = random.uniform(lmInf, lmSup)
        self.publisher_.publish(msg) 
        self.get_logger().info('Publishing velocity: "%s"' % msg.data)

    def timer_callback2(self):
        msg = Float32() # Definir el tipo de la variable de mensaje
        # Generar un decimal entre 0.0 y 1.0  // numero_simple = random.random()

        # Generar un decimal en un rango específico
        lmInf = 0.0
        lmSup = 100.0
        msg.data = random.uniform(lmInf, lmSup)
        self.publisher2_.publish(msg) 
        self.get_logger().info('Publishing batery: "%s"' % msg.data)
        


def main(args=None):
    rclpy.init(args=args) 

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher) 

    minimal_publisher.destroy_node() 
    rclpy.shutdown()


if __name__ == '__main__':
    main()