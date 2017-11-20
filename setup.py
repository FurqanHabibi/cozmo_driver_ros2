from setuptools import setup

package_name = 'cozmo_driver_ros2'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'cozmo_driver',
        'transformations'
    ],
    include_package_data=True,
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('shared/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    maintainer='Muhammad Furqan Habibi',
    maintainer_email='furqan.habibi1@gmail.com',
    author='Muhammad Furqan Habibi',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Unofficial ROS2 node for Anki Cozmo.',
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'cozmo_driver = cozmo_driver:main'
        ],
    },
)
