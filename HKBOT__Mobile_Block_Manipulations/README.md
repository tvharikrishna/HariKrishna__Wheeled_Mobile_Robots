<!------ Copyrights ------>
<p align="right">© 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻 𝗯𝘆 𝘁𝘃𝗵𝗮𝗿𝗶𝗸𝗿𝗶𝘀𝗵𝗻𝗮</p>
<p align="right">5 𝘮𝘪𝘯𝘶𝘵𝘦 𝘳𝘦𝘢𝘥 📚 </p> <br>

<!------ PROJECT TITLE ------>
<p align="center">
    <img src="readme_data/project_title.png" alt="project title" width="1111"/>
</p> <br> <br>

<!------ WHAT ------>
<p align="center">
    <img src="readme_data/what.png" alt="what section" width="600"/>
</p>

<p align="center"><h1>🎀 Essence of the Project</h1></p>
<p align='justify'>
▸ I have developed a specialized algorithm for a custom-built mobile robot that utilizes an NVIDIA Jetson Nano and a 6-DOF robotic arm for block manipulation tasks. The robot is designed with mecanum wheels, which enable omnidirectional movement, allowing the robot to maneuver with precision in any direction. Safety protocols and measures have been rigorously integrated to ensure the robot operates within the guidelines for mobile robots and autonomous guided vehicles. </p>

<p align='justify'>
▸ The algorithm efficiently manages the 'pick and place' operations, placing blocks onto the robot's chassis, adapting dynamically to the payload configuration, and optimizing the spatial arrangement to accommodate additional blocks.</p>

<p align="center">
  <a href="https://www.linkedin.com/feed/update/urn:li:activity:7130040549587243008?utm_source=share&utm_medium=member_desktop">
    <img src="https://img.shields.io/badge/My Project Video-Robot Block Manipulation-blue" alt="Video" width="337" height="30"/>
  </a>
</p> <br> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="What the project accomplishes" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
The project is dedicated to revolutionizing block manipulation tasks through the development of a specialized algorithm and the integration of advanced technology, including an NVIDIA Jetson Nano and a 6-DOF robotic arm. Here are the key benefits of this innovative project in the realm of autonomous mobile robotics:
</p>
<p style="text-align: justify;">
▸ <code>Enhanced Operational Efficiency:</code> Utilizing a sophisticated algorithm to optimize 'pick and place' operations, significantly reducing execution time and resource use.
</p>
<p style="text-align: justify;">
▸ <code>Innovative Robotic Mobility:</code> The use of mecanum wheels facilitates omnidirectional movement, allowing for precise and versatile maneuvering, enhancing automation in logistics and beyond.
</p>
<p style="text-align: justify;">
▸ <code>Safety Protocol Integration:</code> Rigorous safety measures ensure the robot's operation adheres to the highest standards for mobile robots and autonomous guided vehicles, promoting a secure working environment.
</p>
<p style="text-align: justify;">
▸ <code>Dynamic Adaptation:</code> The robot's ability to adjust dynamically to various payload configurations and optimize spatial arrangements for block placement demonstrates advanced adaptability in automated tasks.
</p> <br> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="How the project was implemented" width="600"/>
</p>

<p align="center"><h1>🪓 Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
My project's implementation is centered around a highly efficient and adaptable software architecture, utilizing cutting-edge technology and innovative design principles:

▸ <strong>Specialized Algorithm:</strong> Leveraging the NVIDIA Jetson Nano, I crafted a tailored algorithm designed for precise and efficient 'pick and place' operations. This algorithm optimizes block manipulation with an emphasis on speed and accuracy.

▸ <strong>Machine Learning Models:</strong> I employed advanced object recognition and spatial awareness models to facilitate real-time decision-making. This enables the robot to dynamically adapt to new payloads and ensures optimal placement of blocks.

▸ <strong>Hardware Integration:</strong> I ensured seamless control over the robot's 6-DOF arm and mecanum wheels through the use of custom PCBs and high-quality components. This integration achieves precise maneuverability and task execution.

▸ <strong>Safety First:</strong> I embedded rigorous safety protocols into the project to guarantee operation within the guidelines for autonomous vehicles. This prioritizes the safety of both the robot and its surrounding environment.
</p>

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

<!------ Deployment and Testing ------>
<p align="center"><h2>💠 Deployment and Testing</h2></p>
<p style="text-align: justify;">
    
<p align="center"><h2>▸ Manipulation Sequence Planning</h2></p>
▸ I have designed the algorithm for the robotic arm in a way that is referred to as 'manipulation sequence' or 'manipulation planning' in robotics. When the robot's chassis already holds one or two blocks, it needs space to place an additional block. My developed algorithm directs the arm to push the existing blocks slightly backward, creating room for the new one. This process can repeat for any number of blocks, as demonstrated in the video.

<p align="center"><h2>▸ Implemented Safety Measures for Operating AMRs/AGVs</h2></p>
As we all know, robots can pose a hazard if we enter their operational zone. To address safety concerns on sites and factories that use mobile robots and Autonomous Guided Vehicles (AGVs), I have programmed an algorithm to enhance safety communications. When the robot is performing a manipulation task, it emits a flashing red light. Conversely, when the robot is merely moving around, it emits a green light, signaling to humans that it is safe to approach. However, it is unsafe to approach when the robot flashes a red light. </p>

<p align="center"><h2>Red: Danger</h2></p>
<p align="center">
  <img src="readme_data/project_observation_1.png" alt="Project Observation 1" width="1111"/>
</p>

<p align="center"><h2>Green: Safe</h2></p>
<p align="center">
  <img src="readme_data/project_observation_2.png" alt="Project Observation 2" width="1111"/>
</p> <hr>

<!------ End Image ------>
<p align="center">
    <img src="readme_data/HKbot_endquote.png" alt="Alt text for your image" width="1500"/>
</p>
