# Self-Driving Car using Udacity Car Simulator

## Overview
This project implements a self-driving car simulation using the Udacity Car Simulator. It leverages various machine learning and computer vision techniques to navigate and drive autonomously within the simulator environment.

## Features
- Real-time car control in the Udacity simulator
- Data collection and preprocessing tools
- Training scripts and evaluation metrics
- Autonomous Driving in the simulator

## Installation
To get started, follow these steps:

### Prerequisites
- Python 3.x
- Git
- Virtualenv or Anaconda (recommended for managing dependencies)

## Usage

To use the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abhinash-bhagat/self-driving-car.git
   cd self-driving-car

2. **Setup Virtual Environment**:
   ```bash
   conda create --name self-driving-car python=3.8
   conda activate self-driving-car


3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt


## Directory Structure

![dict-struct](https://github.com/abhinash-bhagat/self-driving-car/assets/96810040/294dda50-415a-456e-8c1e-317ad5d9bff1)


### Additional Setup

  * Download the Audacity Car Simulator from the udacity github page or below.
    - [Windows](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f3a4_simulator-windows-64/simulator-windows-64.zip)
    - [Linux](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f0f7_simulator-linux/simulator-linux.zip)
    - [Mac](https://d17h27t6h515a5.cloudfront.net/topher/2016/November/5831f290_simulator-macos/simulator-macos.zip)

  * Extract and place the simulator files in the simulator directory within the project.
  * Create a new folder in the root directory of the project called 'data'

### Collecting Training Data

To collect training data, run the Udacity car simulator file. This will allow you to manually drive the car in the simulator and collect images and steering angles. Click on `Training` mode and then start the record option on the top right and select 'data' folder as the path to store data and start driving. **OR YOU CAN USE THE DATA I PROVIDED.** 

### Training the Model
Run the cells in `train.ipyb` file and set the params like `epochs` according to your system's capabilities & time.

### Running the Autonomous Mode
After training the model, you can run the autonomous driving mode with `drive.py` remember to update the model's path with your model or you can use the model I have provided:
```bash
python drive.py
