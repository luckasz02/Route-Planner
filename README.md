# Route Planner Application

## Overview

This Route Planner Application is a web-based tool designed to find the most efficient routes between nodes using various algorithms. It features a user-friendly interface where users can visually select nodes on a graph and choose between different algorithms for route calculation. The application supports the A\*, Bidirectional Dijkstra, and Bellman-Ford algorithms.

## Features

- Interactive graph to select start and end nodes for route planning.
- Route calculation using the A\* algorithm.
- Efficient path-finding with the Bidirectional Dijkstra algorithm.
- Implementation of the Bellman-Ford algorithm to handle routes with varying costs.
- Display of route details, including total distance, nodes visited, and computation time.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Modern web browser

### Installation Steps

1. **Clone or download the project**:

   - Download the ZIP file of the project and extract it, or clone the project repository.

2. **Set up a Python virtual environment (Optional but recommended)**:

   bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install required packages**:

   Navigate to the project directory and run:
   bash
   pip install -r requirements.txt

## Running the Application

1. **Start the Flask server**:

   bash
   python app.py

   This will start the Flask server on `http://localhost:5000`.

2. **Access the application**:

   - Open a web browser and navigate to `http://localhost:5000`.

3. **Using the application**:

   - Interactively select start and end nodes on the graph.
   - Choose the desired routing algorithm (A\*, Bidirectional Dijkstra, or Bellman-Ford).
   - Click "Find Route" to display the route details.

## Project Structure

- `app.py`: The main Flask application file.
- `algorithms.py`: Contains the implementations of A\*, Bidirectional Dijkstra, and Bellman-Ford algorithms.
- `/templates`: Contains HTML files for the front end, including the main interface.
- `/static`: Contains CSS for styling and JavaScript for interactive functionalities.

## Contributing

Contributions are welcome! Feel free to fork the project, make changes, and submit pull requests.

## License

This project is open-sourced under the [MIT License](LICENSE.md).

## Contact

For any queries, suggestions, or feedback regarding this project, please contact [lucadumitru02@gmail.com].
