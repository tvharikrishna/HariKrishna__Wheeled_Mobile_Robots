<!------ PROJECT TITLE ------>
<p align="center">
    <img src="readme_data/project_title.png" alt="title" width="1111"/>
</p> <br> <br>

<!------ WHAT ------>
<p align="center">
    <img src="readme_data/what.png" alt="what" width="600"/>
</p>

<p align="center"><h1>🎀 Essence of the Project</h1></p>
<p align='justify'>
The SLAM Gmapping project employs Simultaneous Localization and Mapping (SLAM) using Gmapping to enable real-time navigation and environment mapping. By processing LiDAR data, it creates detailed maps while tracking the robot's position. This project is key for autonomous robots, providing them with spatial awareness, adaptive navigation, and precise path planning in unfamiliar surroundings.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=lD5XJAQXX8Y&list=PL0phN1wjvpsafQdjjdUhWytGB8bZFhxXy&index=3">
    <img src="https://img.shields.io/badge/My Project Video-SLAM Gmapping-blue" alt="Video" width="320" height="35"/>
  </a>
</p> <hr> <br> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="why" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
The vision for the SLAM Gmapping project is to revolutionize how autonomous systems perceive and interact with their environment. It aims to create sophisticated, self-updating maps while navigating in real-time, allowing for seamless movement and obstacle avoidance in complex, dynamic environments. Ultimately, this project aspires to set a new standard for adaptability and reliability in autonomous exploration.
</p> <hr> <br> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="how" width="600"/>
</p>

<p align="center"><h1>🪓Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
The project is developed using a robust and versatile tech stack, comprising Ubuntu and Linux for the operating systems, Python as the primary programming language, and utilizing essential tools like SSH, PuTTY, and VNC Viewer for secure remote connections. Development and simulation are enhanced with the ROS ecosystem, including RViz for visualization.
</p>

<p>
<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=python&logoColor=white" alt="Python" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/SSH-4D4D4D.svg?&style=flat-square&logo=windows-terminal&logoColor=white" alt="SSH" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/PuTTY-007ACC.svg?&style=flat-square&logo=windows-terminal&logoColor=white" alt="PuTTY" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/VNC%20Viewer-ED1C24.svg?&style=flat-square&logo=CodeSandbox&logoColor=white" alt="VNC Viewer" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/RVIZ-000000.svg?&style=flat-square&logo=ros&logoColor=white" alt="RViz" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Numpy-013243.svg?&style=flat-square&logo=numpy&logoColor=white" alt="Numpy" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 25px;"/> &nbsp;
</p> <br>

<!------ Technical Terms ------>
<p align="center"><h2>💠 Project Technical Terms & Concept </h2></p>
<p align="center"><h3>▸ What is SLAM?</h3></p>
<p style="text-align: justify;">
SLAM (Simultaneous Localization and Mapping) is a technology that allows a robot or a vehicle to create a map of its surroundings while simultaneously determining its location within that map. This is crucial for navigation in environments where GPS is unavailable or unreliable.
</p> <br>

<p align="center"><h3>▸ What are types of SLAM?</h3></p>
<p style="text-align: justify;">
There are several types of SLAM, each suited to different applications. The main types include Visual SLAM (V-SLAM), which uses cameras, Lidar SLAM, which uses laser scanners, and Sensor Fusion SLAM, which combines multiple sensors. Each type has its advantages, depending on the specific requirements of the environment and the task.
</p> <br>

<p align="center"><h3>▸ What is Gmapping?</h3></p>
<p style="text-align: justify;">
GMapping is a specific implementation of SLAM that uses a particle filter to produce a 2D map from Lidar data. It is widely used in robotics for its efficiency and accuracy in mapping indoor environments. GMapping helps robots navigate and understand their environment by providing a detailed spatial layout.
</p> <br>

<!------ Deployment and Testing ------>
<p align="center"><h2>💠 Deployment and Testing</h2></p>
<p style="text-align: justify;">
    
<p align="center">
  <img src="readme_data/project_obs2.png" alt="Project Observation 2" width="1111"/>
</p>

<p align="center">
  <img src="readme_data/project_obs3.png" alt="Project Observation 3" width="1111"/>
</p>

<p align="center">
  <img src="readme_data/project_obs4.png" alt="Project Observation 4" width="1111"/>
</p> <br>

<!------ Result and Analysis ------>
<p align="center"><h2>💠 Results & Analysis </h2></p>
<p align='justify'>
▸ The SLAM Gmapping project's results demonstrate a marked improvement in map accuracy through the use of morphological operations. The original map (`my_map.pgm`) contains noise and gaps that hinder accurate environment mapping. Applying operations like erosion and dilation with different kernel sizes enhances boundary detection and closes gaps effectively. The refined map, visible at the bottom right of the image, shows a clear and precise representation of the space.

▸ The initial morphological operations (kernel size 1) reduce noise and delineate boundaries better than the raw map. Further refinement (kernel size 2) creates a high-quality map with smooth edges, filled gaps, and accurate obstacle representation.

▸ This map refinement technique improves the quality and usability of the generated maps significantly, ensuring accurate navigation and planning. By leveraging computer vision methods, this approach provides robust solutions for noise reduction and enhances the overall quality of SLAM-based maps.
</p>

<p align="center">
  <img src="readme_data/project_obs5.png" alt="Project Observation 5" width="1111"/>
</p>

<hr> <br> <br> 

<!------ End Image ------>
<p align="center">
    <img src="readme_data/HKbot_endquote.png" alt="Alt text for your image" width="1500"/>
</p>
