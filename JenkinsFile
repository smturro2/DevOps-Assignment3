pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                checkout scm
                sh 'sudo apt update'
                sh "sudo apt install -y python3-venv"
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
