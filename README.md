GoogleCollab:main file
https://drive.google.com/drive/folders/1cNQomkh2X_zkhJhYbzZ2NIzqDRlDyIHB?usp=drive_link


# FlowSync - TrafficLight Optimization
Revolution-Bytes



FlowSync is an intelligent traffic light optimization system that is designed to improve traffic flow, using  dynamic timing algorithms and computer vision. In response to the current traffic density, the system dynamically modifies the timing of traffic lights after detecting and counting the number of detected vehicles.The project aims to reduce waiting times, improve traffic flow, and provide a data-driven approach for optimizing signal timings.
 
Recently lots of traffic lights has been installed in kathmandu valley which uses the constant timer but the traffic density varies on different lane that's why in many intersection like in satdobato, they started manual system using the traffic police .To address this challenge, the project has been initiated to effectively manage the issue.

We have used computer vision technology to implement real time detection and tracking of the vehicles at intersections.
Implementing different types of algorithems to count the number of detected vehicles efficintly. After the detection and counting our project calculate the real time traffic density and change the traffic light dynamically. Lanes with low traffic density are programed to be green lighed for shorter time and lanes with high traffic density are programed to be green lighed for longer time. So for the red light respectively.(max green time allocation=120 sec)

We have designed simulation for the traffic light system with the help of Pygame for the proper visualization and simulation allowing the users to observe the difference in traffic flow before and after the implementation of our project.


We have high expection that the current state of traffic problems can be solved in a certain amount with the help of our project. With the help of dynamic traffic light we are positive that it can save alot of time during our day to day hectic life.

For the project we have used YOLOv8 model for the object detection and counting. We collected current data and labeled it with the help of labelimg, bytetracking and supervision for the detection and counting. 
![image](https://github.com/kunwaratit/Revolution-Bytes/assets/89177301/2edf26dd-2d3b-4bed-9208-cad9adc93478)

