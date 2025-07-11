# Task / Repo Overview
This assignment is to create a simple web app and implement a CI pipeline. A reflection is also written below

# Reflection
I initally tried to setup my CI pipeline with jenkins but it ended being a hassel to install python in the container. 
I went with github actions it's easier to use other peoples code (eetting up and install python, uploading artifacts, etc)
One improvement i would make is configuring the .flake8. There are some things in which I do not care for. I would also
add checking for typehints. CI will improve my ability to write consistent code and ensure good type hints. Often times I make changes and forget to 
update the type hints

# Commands

### Setup
1. Setup venv and install packages
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run
```
streamlit frontend.py
```

### Run Tests
```
pytest tests.py
```

### Python Setup on Ubuntu
```
apt install python3.12-venv
apt install python3.12
```


Set up a CI pipeline using Jenkins (or another CI platform of your choice such as GitHub Actions, GitLab CI, etc.) that:

    Triggers appropriately
        Configure pipeline to run on push to main/master branch
        Configure pipeline to run on pull requests targeting main/master
        Ensure triggers are specific to avoid unnecessary runs

    Environment setup
        Check out the source code from the repository
        Install and configure the correct runtime environment (Node.js, Python, Java, etc.)
        Install project dependencies using appropriate package managers
        Set up any required environment variables or configuration files

    Code quality checks
        Configure and run linting tools appropriate for your language (ESLint, flake8, Checkstyle, etc.)
        Implement at least one code formatting check tool (Prettier, Black, etc.)
        Configure quality gates that fail the pipeline if standards aren't met
        Provide clear error messages and suggestions for fixing issues

    Testing
        Execute all unit tests using appropriate testing framework
        Generate comprehensive test coverage reports (HTML, XML, or JSON format)
        Set minimum coverage thresholds (e.g., 80%) that must be met
        Ensure pipeline fails if any tests fail or coverage is below threshold
        Include test result artifacts for later analysis

    Build process
        Compile/build the application using appropriate build tools
        Verify that all build artifacts are generated successfully

Deliverables

Submit the following components:

    CI Pipeline Configuration
        Complete pipeline configuration file (Jenkinsfile, .github/workflows/ci.yml, etc.)
        Pipeline must implement all 5 required tasks above

    Application Source Code
        Working application with minimum 3 endpoints/features
        Unit tests with minimum 5 test cases
        README file with project setup instructions
        All necessary configuration files

    Pipeline Evidence
        Screenshots or links showing successful pipeline runs
        Evidence that all 5 pipeline tasks execute successfully
        Screenshots showing pipeline failures (e.g., failed tests, code quality issues)


