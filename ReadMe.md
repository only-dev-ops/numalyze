# Numalyze

Numalyze is a web-based numerical analysis toolkit built with Python and Flask. It offers an interactive environment to explore classic numerical methods, from solving equations to performing complex integrations and linear algebra routines. By simply entering parameters into a web form, users can instantly view computed results and insights.

## Overview

This application centralizes a variety of numerical analysis techniques in one place, making them accessible and easy to experiment with. Whether you’re a student learning these concepts for the first time or a professional seeking to validate results, Numalyze provides quick, accurate calculations along with a minimal, user-friendly interface.

## Key Features

- **Root-Finding Algorithms**: Bisection Method, Fixed Point Iteration, Newton’s Method (standard and modified), Secant Method, and Müller’s Method.
- **Convergence Acceleration**: Aitken’s and Steffensen’s Methods for speeding up iterative processes.
- **Integration Techniques**: Composite Trapezoidal, Composite Simpson’s, and Romberg’s Integration.
- **Linear Algebra**: Compute the Reduced Row Echelon Form (RREF) of a matrix.
- **Interactive Interface**: Each algorithm is accessible via a dedicated route, where users can input functions, intervals, initial guesses, and tolerances.

## Technology Stack

- **Python** & **Flask**: Provide the core logic and web server functionality.
- **Jinja2 Templates**: Enable dynamic, server-side rendered HTML pages.
- **HTML/CSS/Bootstrap**: Power a clean and responsive front-end.
- **Docker**: Containerization via a slim Python 3.12 image.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/only-devops/numalyze.git
   cd numalyze
   ```
2. **Build the Docker Image**
   ```bash
   docker build -t numalyze .
   ```
3. **Run the Container**
   ```bash
   docker run -p 5000:5000 --name numalyze_container numalyze
   ```
   The app will be accessible at http://127.0.0.1:5000.

**Environment Variables**

- `PORT` (Optional): If you want to change the port the app is listening on within the container, pass `-e PORT=<your_port>` to Docker.

**Note:** The default command in the Dockerfile uses Gunicorn and binds the application to port `5000`.

## Usage

1. **Run the Flask App** (Without Docker)
   ```bash
   python run.py
   ```
2. **Open Your Browser** to http://127.0.0.1:5000 (or the displayed host/port).
3. **Navigate to Various Methods**
   - Root-Finding
   - Integration
   - Linear Algebra (RREF)
4. **Input Parameters** as prompted (function definition, intervals, initial guesses, or matrix entries) and click the button to compute results.

## Contributing

We welcome pull requests and issues! Feel free to:

- Suggest or implement new numerical methods.
- Improve existing algorithms.
- Enhance the UI/UX.
- Write documentation or tutorials.

When contributing, please:

- Follow the current code style.
