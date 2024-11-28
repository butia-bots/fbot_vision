from setuptools import find_packages, setup
import os
import glob

package_name = 'fbot_recognition'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), ['launch/yolov8_object_recognition.launch.py']),
        ('share/' + package_name + '/config', ['config/yolov8_object_recognition.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gdorneles',
    maintainer_email='dorneles1215@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolov8_recognition = fbot_recognition.yolov8_recognition.yolov8_recognition:main',
        ],
    },
)