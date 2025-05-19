# 3D Object Manipulation with Hand Gestures

A computer vision application that allows users to manipulate 3D objects in real-time using hand gestures captured by a webcam.

![Demo](assets/demo.gif)

## Features

- **Real-time 3D object manipulation** using hand gestures
- **Multiple object types**: Switch between cube and sphere
- **Gesture controls**:
  - Move objects by pointing
  - Scale objects with pinch gestures
  - Rotate objects in 3D space
  - Change rotation axis
  - Adjust rotation speed
- **Visual depth cues** with color gradient rendering
- **MediaPipe integration** for accurate hand tracking and gesture recognition

## Requirements

- Python 3.8+
- OpenCV
- MediaPipe
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/3d-gesture-control.git
cd 3d-gesture-control
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the MediaPipe gesture recognizer model:
   - You'll need to obtain the `gesture_recognizer.task` file and place it in the project directory
   - See [MediaPipe documentation](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer) for more details

## Usage

Run the main application:
```bash
python main.py
```

### Controls

| Gesture | Action |
|---------|--------|
| Open Palm | Reset rotations |
| Closed Fist | Toggle rotation on/off |
| Victory Sign | Switch between cube and sphere |
| Pointing Up | Cycle between X, Y, Z rotation axes |
| Thumb Up | Increase rotation speed |
| Thumb Down | Decrease rotation speed |
| Right Hand Movement | Move the object |
| Thumb-Index Pinch | Scale the object |
| Press ESC | Exit application |

## Project Structure

- `main.py`: Main application entry point
- `create_object.py`: Contains functions for creating 3D objects
- `projection.py`: Handles 3D to 2D projection and rotation
- `requirements.txt`: List of required packages
- `docs/`: Documentation and usage guides

## How It Works

The application uses MediaPipe to track hand landmarks and recognize gestures in real-time. The right hand controls the object's position, while the left hand controls scaling through pinch gestures. Various predefined gestures trigger different actions like changing objects, toggling rotation, or changing rotation axes.

The 3D objects are created with parametric equations, transformed in 3D space, and then projected onto the 2D screen with proper depth cues using color gradients.

## Extending the Project

To add new object types, modify the `create_object.py` file with your new object's parametric equations or mesh data. The main application can be extended to support additional gestures by modifying the gesture recognition handling in `main.py`.

## License

[MIT License](LICENSE)

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand tracking and gesture recognition
- [OpenCV](https://opencv.org/) for image processing
- [NumPy](https://numpy.org/) for numerical operations
- [Matplotlib](https://matplotlib.org/) for visualization
