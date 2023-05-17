from launch import launchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return launchDescription([
        Node(
        package='demo_node_py',
        executable='listner'
        )
    ])