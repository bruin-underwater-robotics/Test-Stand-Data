## *********************************************************
##
## File autogenerated for the pid package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'Kp_scale', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Kp scale', 'min': 0.1, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'scale_tenth', 'type': 'double', 'value': 0.1, 'srcline': 7, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 0.1', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_unity', 'type': 'double', 'value': 1.0, 'srcline': 8, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'No scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_ten', 'type': 'double', 'value': 10.0, 'srcline': 9, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 10', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_hundred', 'type': 'double', 'value': 100.0, 'srcline': 10, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 100', 'ctype': 'double', 'cconsttype': 'const double'}], 'enum_description': 'Scale factor for K setting'}", 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Kp', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Kp', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Ki_scale', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Ki scale', 'min': 0.1, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'scale_tenth', 'type': 'double', 'value': 0.1, 'srcline': 7, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 0.1', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_unity', 'type': 'double', 'value': 1.0, 'srcline': 8, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'No scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_ten', 'type': 'double', 'value': 10.0, 'srcline': 9, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 10', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_hundred', 'type': 'double', 'value': 100.0, 'srcline': 10, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 100', 'ctype': 'double', 'cconsttype': 'const double'}], 'enum_description': 'Scale factor for K setting'}", 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Ki', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Ki', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Kd_scale', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Kd scale', 'min': 0.1, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'scale_tenth', 'type': 'double', 'value': 0.1, 'srcline': 7, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 0.1', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_unity', 'type': 'double', 'value': 1.0, 'srcline': 8, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'No scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_ten', 'type': 'double', 'value': 10.0, 'srcline': 9, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 10', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scale_hundred', 'type': 'double', 'value': 100.0, 'srcline': 10, 'srcfile': '/home/goopbloop/BUR-2022-2023/catkin_ws/src/pid/cfg/Pid.cfg', 'description': 'Scale by 100', 'ctype': 'double', 'cconsttype': 'const double'}], 'enum_description': 'Scale factor for K setting'}", 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Kd', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Kd', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Pid_scale_tenth = 0.1
Pid_scale_unity = 1.0
Pid_scale_ten = 10.0
Pid_scale_hundred = 100.0
