# ROS-Arduino-Ultrasonic_Sensor
An Arduino application that receives data from ultrasonic sensor and send data to ROS node. Then the ROS node can send robot state to its client.

The client side is Windows (because RobotStudio only support Windows) -> RobotStudio -> ABB robotic arm
- When an object is close to the ultrasonic sensor, the movement of the robotic arm will be slowed down.
- When an object is away from the ultrasonic sensor, the movement of the robotic arm will be back to normal speed.

## Client Side (RobotStudio):
![robotstudio](https://user-images.githubusercontent.com/21185752/42662984-87301b5c-85e8-11e8-9d44-1017db8a9654.PNG)
