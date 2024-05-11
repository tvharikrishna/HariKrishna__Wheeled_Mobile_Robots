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
Implementation of the RANSAC algorithm to refine LiDAR data for autonomous vehicles and robots. This technique filters out noise-induced outliers, ensuring that the most reliable inliers remain for accurate model estimation. The aim is to create a robust system for safe and efficient navigation, improving terrain mapping and obstacle avoidance.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=zXO-8BgycEM&list=PL0phN1wjvpsafQdjjdUhWytGB8bZFhxXy&index=6">
    <img src="https://img.shields.io/badge/My Project Video-RANSAC Lidar Optimization-blue" alt="Video" width="480" height="40"/>
  </a>
</p> <hr> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="why" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
The project aims to leverage the RANSAC algorithm to optimize LiDAR data analysis for autonomous systems, enhancing the reliability of navigational pathways and ensuring that vehicles and robotics operate with increased accuracy and safety. The implementation brings critical advantages to autonomous navigation, including advanced outlier detection by using RANSAC on LiDAR data to identify and remove outliers, thereby maintaining only the most reliable data for model estimation. It also enhances navigation safety by improving the precision of terrain mapping and obstacle avoidance methodologies, and builds a robust system within the ROS framework, utilizing rospy for scripting and employing the F1Tenth Simulator alongside RViz for comprehensive simulation and visualization.
</p> <hr> <br> <br> 

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="What the project accomplishes" width="600"/>
</p>

<p align="center"><h1>🪓Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
The project's execution is centered on the strategic application of the RANSAC algorithm within the ROS framework, optimizing the extraction and utilization of LiDAR data for autonomous navigation. With meticulous integration of advanced computational tools and simulation environments, I established a robust methodology for enhancing the Lidar data processing pipeline. This includes scripting in rospy to facilitate real-time data analysis from the lidar and employing simulation platforms for testing and refining our models. The outcome is a sophisticated system poised to significantly advance the field of mobile robotics and autonomous vehicle navigation. </p>

<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=python&logoColor=white" alt="Python" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/F1%20Tenth%20Simulator-007ACC.svg?&style=flat-square&logo=chevrolet&logoColor=white" alt="F1 Tenth Simulator" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/RVIZ-000000.svg?&style=flat-square&logo=ros&logoColor=white" alt="Gazebo" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Numpy-013243.svg?&style=flat-square&logo=numpy&logoColor=white" alt="Numpy" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 30px;"/> &nbsp;
<br>

<!------ Technical Terms ------>
<p align="center"><h2>💠 Project Technical Terms & Concepts</h2></p>
<p align="center"><h3>▸ What is RANSAC?</h3></p>
<p style="text-align: justify;">
RANSAC (Random Sample Consensus) is an iterative method used in data analysis to estimate parameters of a mathematical model from a set of observed data that contains outliers. It is a robust algorithm designed to produce reliable estimates by repeatedly selecting random subsets of the data, fitting a model, and then determining how many of the remaining data points fit this model within a predefined tolerance.
</p> <br>

<p align="center">
    <img src="readme_data/ransac_gif_1.gif" alt="Project Technical Terms & Concepts Images" width="651"/>
</p> <br>

<p align="center"><h3>▸ What are Outliers in Lidar Data</h3></p>
<p style="text-align: justify;">
Outliers in LiDAR data are data points that do not fit the expected pattern or model, often caused by noise, errors in measurement, or objects that are not relevant to the analysis, such as birds, rain, or dust. These points can significantly skew the results of data analysis if not properly managed.
</p> <br>

<p align="center"><h3>▸ What are Inliers in Lidar Data</h3></p>
<p style="text-align: justify;">
Inliers in LiDAR data are the points that align well with the general model being used to represent the environment. These are the data points that reflect the actual physical surfaces in the environment, such as the ground, buildings, and other structures, and are crucial for accurate mapping and navigation.
</p> <br>

<p align="center"><h3>▸ What is the whole purpose of using RANSAC on Lidar Data</h3></p>
<p style="text-align: justify;">
The primary purpose of using RANSAC on LiDAR data is to effectively distinguish between inliers and outliers, allowing for the construction of an accurate model of the environment with minimal influence from noise and erroneous measurements. This enhances the reliability and precision of applications such as autonomous navigation, terrain mapping, and obstacle detection.
</p> <br>

<p align="center"><h3>▸ Apart from RANSAC, are there any other methods?</h3></p>
<p style="text-align: justify;">
Yes, apart from RANSAC, there are several other robust estimation methods used to handle outliers in data analysis, including methods like the Least Median of Squares (LMedS), Maximum Likelihood Estimation (MLE), and other iterative techniques that aim to optimize the fit of a model to the data by minimizing the effect of outliers.
</p> <br>

<!------ Deployment and Testing ------>
<p align="center"><h2>💠 Deployment and Testing </h2></p>

<p align="center">
    <img src="readme_data/project_obs_1.png" alt="Deployment and Testing Images" width="1500"/>
</p>

<p align="center">
    <img src="readme_data/project_obs_2.png" alt="Deployment and Testing Images" width="1500"/>
</p>

<p align="center">
    <img src="readme_data/project_obs_3.png" alt="Deployment and Testing Images" width="1500"/>
</p>

<!------ Result and Analysis ------>
<p align="center"><h2>💠 Results & Analysis </h2></p>
<p align='justify'>
The implementation of the RANSAC algorithm on the LiDAR data has been successful in removing outliers. The refined data now presents a more accurate representation of the environment, allowing for improved navigational decisions and path planning in autonomous systems.
</p> <hr> <br>

<!------ End Image ------>
<p align="center">
    <img src="readme_data/hk_quote.png" alt="endquote" width="1500"/>
</p>
