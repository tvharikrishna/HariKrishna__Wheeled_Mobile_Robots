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
The aim of this project is to create an occupancy grid for a mobile robot, essential for autonomous navigation. By forming a precise map, the robot can accurately interpret its environment, which is crucial for any advanced navigation strategy. I've integrated morphological techniques to enhance the map's utility and accuracy, refining the grid by smoothing and removing noise. This not only improves the robot's operational efficiency in complex environments but also optimizes its interaction with surroundings, facilitating effective path planning and obstacle avoidance.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=hPO0Oewo9eA&list=PL0phN1wjvpsafQdjjdUhWytGB8bZFhxXy&index=5">
    <img src="https://img.shields.io/badge/My Project Video-Occupancy Grid Mapping-blue" alt="Video" width="440" height="35"/>
  </a>
</p> <hr> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="why" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
Project Vision is centered on developing a comprehensive occupancy grid mapping system for mobile robots, which is essential for autonomous navigation. The project aims to generate a detailed map that forms the foundation for sophisticated navigational strategies, ensuring accurate environmental interpretation and interaction. Key benefits of this advanced mapping approach include foundational mapping, which is critical for autonomous navigation, enabling precise environmental interpretation. Advanced morphological operations enhance mapping accuracy by smoothing out noise and refining the grid, thus improving navigational decisions. This approach optimizes the robot's path planning capabilities and enables effective obstacle avoidance, enhancing safety and reliability in autonomous operations.
</p> <hr> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="how" width="600"/>
</p>

<p align="center"><h1>🪓Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
The Occupancy Grid Mapping project utilizes the Robot Operating System (ROS) within Ubuntu and Linux environments for robust, real-time map generation. Python scripts facilitate the creation and refinement of occupancy grids, employing Gazebo for simulations to evaluate mapping algorithms across diverse environments. RViz, enhanced with advanced visualization techniques including morphological filtering with OpenCV, improves visual insights and map building accuracy. This project integrates VS Code as the development environment.
    
<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=python&logoColor=white" alt="Python" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Gazebo-000000.svg?&style=flat-square&logo=ros&logoColor=white" alt="Gazebo" style="height: 25px;"/>
<img src="https://img.shields.io/badge/RVIZ-000000.svg?&style=flat-square&logo=ros&logoColor=white" alt="Gazebo" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Pillow-FFD43B.svg?&style=flat-square&logo=python&logoColor=blue" alt="Pillow" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/OpenCV-5C3EE8.svg?&style=flat-square&logo=opencv&logoColor=white" alt="OpenCV" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Numpy-013243.svg?&style=flat-square&logo=numpy&logoColor=white" alt="Numpy" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 25px;"/> &nbsp;
</p> <br>

<!------ Technical Terms ------>
<p align="center"><h2>💠 Project Technical Terms & Concepts </h2></p>
<p align="center"><h3>▸ Erosion</h3></p>
<p style="text-align: justify;">
Erosion is a morphological process that shrinks the boundaries of the foreground object, effectively reducing noise and small details from an image. This technique is pivotal in eliminating irrelevant or extraneous structures that could impede the clarity of navigational pathways.
</p> <br>

<p align="center"><h3>▸ What is Occupancy Grid Mapping</h3></p>
<p style="text-align: justify;">
Occupancy Grid Mapping is a spatial representation technique used in robotics to model the environment as a grid of cells. Each cell in the grid represents a specific area of space and is assigned a probability that indicates whether the area is occupied by an obstacle, free, or unknown. This method provides a detailed and flexible way of mapping complex environments for navigation and planning in autonomous robots.
</p> <br>

<p align="center"><h3>▸ What is the difference between Occupancy Grid Mapping and SLAM?</h3></p>
<p style="text-align: justify;">
Occupancy Grid Mapping and SLAM (Simultaneous Localization and Mapping) are both crucial in autonomous navigation but serve different purposes. Occupancy Grid Mapping focuses on creating a map of the environment using sensor data to determine occupied and free spaces. In contrast, SLAM simultaneously creates a map of the environment while also tracking the robot's location within it, integrating localization with mapping to maintain accuracy in dynamic environments.
</p> <br>

<p align="center"><h3>▸ Dilation</h3></p>
<p style="text-align: justify;">
Dilation is the complementary process to erosion, expanding the boundaries of the foreground object in an image. It is often used to fill in small holes and connect disjointed elements, enhancing the map's structural integrity and ensuring essential navigational features are pronounced and easily interpretable.
</p> <br>

<p align="center"><h3>▸ Are Erosion and Dilation on the generated map really useful?</h3></p>
<p style="text-align: justify;">
Yes, applying erosion and dilation to the generated maps is highly beneficial in occupancy grid mapping. Erosion helps remove noise and unnecessary details that could clutter the map, while dilation ensures that important features and pathways are visible and connected. Together, these processes refine the map's quality, aiding robots in better navigation and obstacle avoidance, ultimately leading to more efficient and reliable autonomous operations.
</p> <br>

<!------ Deployment and Testing ------>
<p align="center"><h2>💠 Deployment and Testing </h2></p>
<p align='justify'>
The below images represents a visual representation of Occupancy Grid Mapping and Morphological Map Refinement within a robotic simulation environment. On the left, we see an initial occupancy grid map generated by a robot using LiDAR and odometry data, with various obstacles and free spaces indicated. The map on the right shows the outcome of applying morphological refinement techniques to the initial map, resulting in a cleaner, more navigable map. </p>

<p align="center">
  <img src="readme_data/project_obs_1.png" alt="Deployment and Testing Images" width="1000"/>
</p>

<p align="center">
  <img src="readme_data/project_obs_2.png" alt="Deployment and Testing Images" width="1000"/>
</p>

<p align="center">
  <img src="readme_data/project_obs_3.png" alt="Deployment and Testing Images" width="1000"/>
</p>

<p align="center">
  <img src="readme_data/project_obs_4.png" alt="Deployment and Testing Images" width="1000"/>
</p>

<!------ Result and Analysis ------>
<p align="center"><h2>💠 Results & Analysis </h2></p>

<p align="left">▸ Original Map Generated without Map Refinement:</p>
<p align="center">
  <img src="readme_data/refinment_map_orginal.jpg" alt="Original Map" width="350"/>
</p>

<p align="left">▸ Map after Refinement using Erosion and Dilation:</p>
<p align="center">
  <img src="readme_data/refinment_map_1.jpg" alt="Refinement Map 1" width="200"/>
  <img src="readme_data/refinment_map_2.jpg" alt="Refinement Map 2" width="200"/>
  <img src="readme_data/refinment_map_3.jpg" alt="Refinement Map 3" width="200"/>
  <img src="readme_data/refinment_map_4.jpg" alt="Refinement Map 4" width="200"/>
</p> <hr> <br> <br>

<!------ End Image ------>
<p align="center">
    <img src="readme_data/hk_quote.png" alt="End Quote" width="1500"/>
</p>
