<!------ PROJECT TITLE ------>
<p align="center">
    <img src="readme_data/project_title.png" alt="title" width="1500"/>
</p> <br> <br>

<!------ WHAT ------>
<p align="center">
    <img src="readme_data/what.png" alt="what" width="600"/>
</p>

<p align="center"><h1>🎀 Essence of the Project</h1></p>
<p align='justify'>
The Bicycle Kinematic Model block creates a bicycle vehicle model to simulate simplified car-like vehicle dynamics. It represents a vehicle with two axles separated by the wheelbase. The vehicle’s heading, theta, is defined at the center of the rear axle, where the front wheel can be steered using an angle, psi. This kinematic approach is fundamental in autonomous driving vehicles and autonomous mobile robotics, enabling accurate motion planning and control. It predicts vehicle trajectory and facilitates the implementation of advanced navigation algorithms, enhancing the efficiency and safety of autonomous systems.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=IAY0Meuh5nU&list=PL0phN1wjvpsafQdjjdUhWytGB8bZFhxXy&index=7">
    <img src="https://img.shields.io/badge/My Project Video-Kinematic Bicycle Model Analysis-blue" alt="Video" width="470" height="35"/>
  </a>
</p> <hr> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="why" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
The project utilizes the Kinematic Bicycle Model to improve movement planning and execution in autonomous driving and robotics. This model enhances control over vehicle dynamics, meeting the complex requirements of modern autonomous systems. The Kinematic Bicycle Model ensures precise movement planning and simplifies trajectory predictions, making steering commands more actionable and efficient. It is crucial for smooth path planning and maintaining strict route adherence, thereby increasing safety, optimizing energy efficiency, and reducing risks in dynamic driving environments.
</p> <hr> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="how" width="600"/>
</p>

<p align="center"><h1>🪓Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
The project is developed using the Robot Operating System (ROS), facilitating complex simulations and trajectory analysis. The mathematical foundation and kinematic behavior of the bicycle model are visualized through Matplotlib, with Python scripting at the core of the development. RViz provides real-time visualization of the robot model and trajectory, enhancing the analysis and debugging process.
</p>

<p>
<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=python&logoColor=white" alt="Python" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Matplotlib-FFD43B.svg?&style=flat-square&logo=python&logoColor=blue" alt="Matplotlib" style="height: 30px;"/> &nbsp;
</p> <br>

<!------ Technical Terms ------>
<p align="center"><h2>💠 Project Technical Terms & Concepts </h2></p>
<p align="center"><h3>▸ Differential Drive in Robotics</h3></p>
<p style="text-align: justify;">
Differential drive in robotics refers to a method of movement where a robot is controlled by two separately driven wheels placed on either side of the robot's body. The varying speeds and directions of these wheels allow the robot to move forward, backward, turn, and pivot on the spot, providing high maneuverability in tight spaces.
</p> <br>

<p align="center"><h3>▸ Can the Kinematic Bicycle Model be implemented only in autonomous vehicles or mobile robots?</h3></p>
<p style="text-align: justify;">
The Kinematic Bicycle Model can be implemented in both autonomous vehicles and mobile robots, as it provides a realistic and computationally efficient way to model the motion of any vehicle with a two-wheel base, including bicycles and motorcycles, expanding its applications beyond just four-wheeled vehicles.
</p> <br>

<p align="center"><h3>▸ What is Mobile Robot Maneuverability? </h3></p>
<p style="text-align: justify;">
Mobile robot maneuverability refers to the ability of a robot to change its position and orientation effectively within its environment. This includes the robot's capability to navigate around obstacles, make tight turns, and adjust its path according to the operational needs and environmental constraints.
</p> <br>

<p align="center"><h3>▸ What is Degree of Mobility in Robotics? </h3></p>
<p style="text-align: justify;">
The degree of mobility in robotics quantifies the ability of a robot to move freely and efficiently in its environment. It typically measures the number of independent ways in which a robot can move or change its position, often determined by the design of its drive system and chassis.
</p> <br>

<p align="center"><h3>▸ What is Degree of Steerability in Robotics? </h3></p>
<p style="text-align: justify;">
The degree of steerability in robotics refers to the extent to which a robot can change its direction of travel through steering mechanisms. It is a crucial factor in navigating through complex environments and is typically influenced by the robot's wheel configuration and control algorithms.
</p> <br>

<p align="center"><h3>▸ What is Degree of Maneuverability in Robotics? </h3></p>
<p style="text-align: justify;">
The degree of maneuverability in robotics describes how well a robot can control its motion within its operational environment. This includes its ability to execute precise movements, such as starting, stopping, and turning, which are critical for tasks requiring high precision and agility.
</p> <br>

<p align="center"><h3>▸ What are wheeled kinematic constraints? </h3></p>
<p style="text-align: justify;">
Wheeled kinematic constraints refer to the limitations in movement patterns and paths that a wheeled robot can follow, based on its specific wheel configuration. These constraints impact how the robot can move and are determined by factors like the number of wheels, their placement, and whether they are fixed or steering.
</p> <br>

<!------ Deployment and Testing ------>
<p align="center"><h2>💠 Deployment and Testing </h2></p>
<p align='justify'>
▸ The deployment of the Bicycle Kinematic Model was conducted within a simulated environment using ROS, ensuring a controlled testing. I deployed the model on a standard Ubuntu system, with simulations facilitated by Matplotlib for trajectory visualization. The process included continuous integration practices to check for code integrity and automated tests to validate kinematic equations against predetermined inputs.
</p>

<p align='justify'>
▸ Testing consisted of a series of controlled simulations designed to challenge the model's capabilities in trajectory planning and response. Scenarios included navigating circular paths, sharp turns, and S-shaped trajectories, each requiring precise control of steering angles and velocity. The model's performance was gauged by its ability to maintain the intended path with minimal deviation and its response time to dynamic commands.
</p> <br>

<p align="center">
    <img src="readme_data/project_obs_1.png" alt="Deployment and Testing Images" width="1500"/>
</p> <br>

<p align="center">
    <img src="readme_data/project_obs_2.png" alt="Deployment and Testing Images" width="1500"/>
</p> <br>

<p align="center">
    <img src="readme_data/project_obs_3.png" alt="Deployment and Testing Images" width="1500"/>
</p> <br>

<!------ Result and Analysis ------>
<p align="center"><h2>💠 Results & Analysis </h2></p>

<p align='justify'>
▸ The Bicycle Kinematic Model's testing confirmed theoretical predictions with real-world behavior. Control sequences manipulated velocity and turning rate, with resulting positions and distances traveled quantifying model accuracy.
</p>

<p align='justify'>
▸ A test with <code>control sequence [1, 0.1, 5]</code> showed the model navigating from the origin to <code>(-2.5586, 5.1742)</code>, covering <code>5.77 units</code>. This aligns with predictions from kinematic equations, illustrating the model's precision.
</p>

<p align='justify'>
▸ Complex maneuvers like sharp turns and direction reversals were executed with high fidelity, as seen with sequences like <code>[1, 0.7, 7]</code> and <code>[-0.1, 0.8]</code>, validating the model's responsiveness to input variations.
</p>

<p align='justify'>
▸ The practical validation of the kinematic equations has established their high accuracy and reliability. Each computational step, from velocity computation to positional adjustments, adhered to theoretical expectations with precision. This thorough analysis has not only fortified the Bicycle Kinematic Model's theoretical foundations but has also illuminated its practical efficacy.
</p> <br>

<p align="center">
    <img src="readme_data/project_obs_4.png" alt="Result and Analysis Images" width="1500"/>
<hr> <br> <br>

<!------ Smile More ------>
<p align="center">
    <img src="readme_data/hk_quote.png" alt="endquote" width="1500"/>
</p>
