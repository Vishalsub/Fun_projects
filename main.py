import os

def create_package(package_name, destination_directory, package_format, version, description, maintainer, licenses, build_type, dependencies, node_name):
    package_directory = os.path.join(destination_directory, package_name)
    source_directory = os.path.join(package_directory, package_name)
    resource_directory = os.path.join(package_directory, 'resource')
    test_directory = os.path.join(package_directory, 'test')

    # Create package directory
    os.makedirs(package_directory)

    # Create package.xml
    package_xml_content = f'''\
<?xml version="1.0"?>
<package format="{package_format}">
  <name>{package_name}</name>
  <version>{version}</version>
  <description>{description}</description>
  <maintainer email="{maintainer[1]}">{maintainer[0]}</maintainer>
  <license>{licenses}</license>
  <build_type>{build_type}</build_type>
  <dependencies>{'\n'.join(f'    <depend>{dep}</depend>' for dep in dependencies)}</dependencies>
</package>
'''
    with open(os.path.join(package_directory, 'package.xml'), 'w') as package_xml:
        package_xml.write(package_xml_content)

    # Create source folder and __init__.py
    os.makedirs(source_directory)
    with open(os.path.join(source_directory, '__init__.py'), 'w') as init_file:
        pass

    # Create setup.py
    setup_py_content = f'''\
from setuptools import setup

package_name = '{package_name}'

setup(
    name=package_name,
    version='{version}',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/{package_name}']),
        (f'share/{package_name}', ['resource/{package_name}/package.xml']),
    ],
    install_requires=[
        'setuptools',
        'ament_index_python',
        'ament_package',
        'setuptools',
        'pytest',
    ],
    zip_safe=True,
    maintainer='{maintainer[0]}',
    maintainer_email='{maintainer[1]}',
    description='{description}',
    license='{licenses}',
    tests_require=['pytest'],
    entry_points={{
        'console_scripts': [
            '{node_name} = {package_name}.{node_name}:main',
        ],
    }},
)

setup()
'''
    with open(os.path.join(package_directory, 'setup.py'), 'w') as setup_py:
        setup_py.write(setup_py_content)

    # Create setup.cfg
    setup_cfg_content = f'''\
[develop]
script_dir=$base/lib/{package_name}
'''
    with open(os.path.join(package_directory, 'setup.cfg'), 'w') as setup_cfg:
        setup_cfg.write(setup_cfg_content)

    # Create resource folder
    os.makedirs(resource_directory)

    # Create test folder and test files
    os.makedirs(test_directory)
    with open(os.path.join(test_directory, 'test_copyright.py'), 'w') as test_copyright:
        pass
    with open(os.path.join(test_directory, 'test_flake8.py'), 'w') as test_flake8:
        pass
    with open(os.path.join(test_directory, 'test_pep257.py'), 'w') as test_pep257:
        pass

    # Create node Python file
    node_py_content = f'''\
import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('{node_name}')

    # Your node logic goes here

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
'''
    with open(os.path.join(source_directory, f'{node_name}.py'), 'w') as node_py:
        node_py.write(node_py_content)

if __name__ == '__main__':
    create_package(
        package_name='my_package',
        destination_directory='/home/user/ros2_ws/src',
        package_format='3',
        version='0.0.0',
        description='TODO: Package description',
        maintainer=['<name>', '<email>'],
        licenses='TODO: License declaration',
        build_type='ament_python',
        dependencies=[],
        node_name='my_node'
    )
