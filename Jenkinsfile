pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                checkout scm
                // sh 'apt update'
                sh "python3.12"
                sh "apt install python3.12-venv"
                sh "python3 -m venv venv"
                sh "source venv/bin/activate && pip install -r requirements.txt"
            }
        }

        stage('Code Checks') {
            steps {
                sh "source venv/bin/activate && flake8 ."
                sh "source venv/bin/activate && black --check ."
            }
        }

        stage('Tests') {
            steps {
                sh "source venv/bin/activate && pytest --cov=. --cov-report=html tests.py"
            }
        }
    }
}
