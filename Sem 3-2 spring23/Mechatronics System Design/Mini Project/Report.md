# Mechatronics Mini Project Report

### Introduction

This project involves the design and fabrication of an animatronic eye model that utilizes a combination of Fusion 360, Robotics Operating System (ROS), and Arduino. The animatronic eye model consists of three motors that control the blinking motion, left-right movement, and up-down movement of the eye. The individual parts of the eye model, including the eyelids, eyeball, and brackets, were designed using Fusion 360. The 3D printing process was then used to fabricate the individual parts, which were assembled to form the animatronic eye model. 

The integration of ROS with Arduino enables communication between the software and hardware components of the animatronic eye model. 

### Contribution 

<Later>

### Design and Fabrication 

The design process involved creating each part of the eye model separately using Fusion 360. There are three motors controlling all motion in the eye – One for blinking, one for Left-Right motion and one for Up-Down motion. The first step was to design the eyelids that would be responsible for the blinking motion. This was done using the upper and lower eyelids (eye_lid_up and eye_lid_down) connected to a common sliding mechanism (eye_blink_slider) to move the eyelids simultaneously. This system is controlled by the first motor (servo_blink). Next, the eyeball was designed with a hollow center that would allow for the movement of the motors responsible for the left-right motion. The motor responsible for this moment is placed in the center of the hollow eyeball (servo_left_right). The third motor placed on the servo_fixed part along with the blink motor is responsible for the up-down motion. This is connected to the eyeball using the eye_up_down links.  

Once the design was finalized, the individual parts were fabricated using a 3D printer. The eyelids, eyeball, and brackets were printed separately and then assembled. The provided motors and horns were connected to the Arduino using an Arduino and were programmed using ROS to control their movement. 

### System Integration 

System integration for the three motors is done using ROS Melodic and Arduino that enables the development of complex robotic systems. ROS provides a framework for building and integrating software modules for various components of a robotic system, while Arduino provides an easy-to-use hardware platform for controlling actuators and sensors. 

The integration of these platforms allows for the development of customizable and versatile robotic systems that can perform a wide range of tasks. Communication between ROS and Arduino is achieved through a serial interface, where ROS sends commands and receives data from the board. This enables control of the movement of motors, collection of sensor data, and provision of feedback to the ROS system. Thus, system integration with ROS and Arduino is a powerful solution for creating advanced robotic systems that can accomplish complex tasks. 


### References 
<Later>

### Conclusion
In conclusion, the design and fabrication of the animatronic eye model, utilizing a combination of Fusion 360, ROS, and Arduino, has demonstrated the potential of integrating different technologies to create advanced robotic systems. The use of Fusion 360, a cloud-based CAD tool, allowed for the creation of precise designs for the individual parts of the eye model, which were then fabricated using 3D printing. The integration of ROS with Arduino facilitated communication between the software and hardware components of the animatronic eye model, allowing for the control of the three motors responsible for the movements of the eye. The animatronic eye model showcases the potential of integrating CAD software, a powerful hardware platform, and a versatile software framework to create complex robotic systems. This technology has potential applications in various fields, including healthcare, industrial automation, and education, among others. Overall, the design and fabrication of the animatronic eye model demonstrates the effectiveness of integrating different technologies to create advanced robotic systems, highlighting the possibilities that exist for the future of robotics. 