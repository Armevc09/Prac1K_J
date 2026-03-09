from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yorch',
    maintainer_email='yorch.academico@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',
            'listener = py_pubsub.subscriber_member_function:main',
            'talk_ci = py_pubsub.pub_custom_interfaces:main',
            'listener_ci = py_pubsub.sub_custom_interfaces:main',
            'server = py_pubsub.service_member_function:main',
            'client = py_pubsub.client_member_function:main',
            'rob_v = py_pubsub.robot_sensor_publisher:main',
            'rob_e = py_pubsub.robot_monitor:main',
            'rob_s = py_pubsub.robot_state_node:main',
        ],
    },
)
