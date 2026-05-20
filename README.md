# DevOps1 Calculator Project

## Introduction

This project is a simple calculator application developed in Python for the DevOps 1 assignment.

The purpose of the project is to demonstrate a basic DevOps workflow using:

- Git and GitHub
- Branching and Pull Requests
- Automated testing with pytest
- Docker containers
- Continuous Integration with GitHub Actions

The calculator supports basic mathematical operations:

- Addition
- Subtraction
- Multiplication
- Division

The project also includes automated tests and Docker support so the application can run consistently on different machines.

---

# Technologies Used

- Python 3.12
- pytest
- Git
- GitHub
- Docker
- GitHub Actions

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/devops1-calculator.git
```

Go into project folder:

```bash
cd devops1-calculator
```

---

# Create Virtual Environment (Optional)

Create virtual environment:

```bash
python3 -m venv venv
```

Activate environment on macOS/Linux:

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip3 install -r requirements.txt
```

This installs pytest for automated testing.

---

# Run Application

Run calculator:

```bash
python3 calculator.py
```

Example output:

```txt
Simple Calculator
2 + 3 = 5
5 - 2 = 3
4 * 3 = 12
10 / 2 = 5.0
```

---

# Run Automated Tests

The project uses pytest for automated testing.

Run tests:

```bash
pytest -v
```

Expected result:

```txt
5 passed
```

---

# Pytest Fixture

The tests use a pytest fixture:

```python
@pytest.fixture
def calculator():
    return Calculator()
```

The fixture creates a reusable Calculator object for the tests.

This avoids repeating the same setup code in every test function.

---

# Docker Support

Docker is included so the project can run in the same environment on different computers.

This helps avoid compatibility problems.

---

# Build Docker Image

```bash
docker build -t devops1-calculator .
```

---

# Run Docker Container

```bash
docker run --rm --name devops1-calculator devops1-calculator
```

The container automatically runs pytest inside the Docker environment.

---

# Git Workflow

This project uses a simple Git workflow.

## Main Branch

The `main` branch contains stable code.

## Feature Branch

Changes are developed in separate feature branches.

Example:

```bash
git checkout -b feature/improve-readme
```

---

# Useful Git Commands

## Check Git Status

```bash
git status
```

## Add Files

```bash
git add .
```

## Commit Changes

```bash
git commit -m "Commit message"
```

## Push Changes

```bash
git push
```

---

# Continuous Integration (CI)

This project uses GitHub Actions for Continuous Integration.

The CI pipeline automatically:

1. Checks out repository code
2. Installs dependencies
3. Runs automated tests
4. Builds Docker image

The pipeline runs automatically when code is pushed to GitHub.

---

# Why CI is Important

Continuous Integration helps developers detect problems early.

Instead of testing manually, tests run automatically whenever code changes are pushed.

This improves:

- Code quality
- Reliability
- Team collaboration
- Faster delivery

---

# Author

Nadeem Ahmad