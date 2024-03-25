import os
from glob import glob

from setuptools import setup

PACKAGE_NAME = 'mqtt_ros_bridge'

setup(
    name=PACKAGE_NAME,
    version='1.1.0',
    packages=[PACKAGE_NAME],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        ('share/' + PACKAGE_NAME, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', PACKAGE_NAME, 'launch'),
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='benjamin',
    maintainer_email='bwp18@case.edu',
    description='MQTT ROS Bridge',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)