pipeline {
    agent any
    environment {
        GIT_URL = 'https://github.com/shaiknasirahamed/Jenkins-Python-CI-CD.git'
    }
    stages {
        stage('Checkout Repository') {
            steps {
                git url: GIT_URL, branch: 'main', credentialsId: 'github-credentials-id'
            }
        }
        stage('Install pipx and Dependencies') {
            steps {
                // Install pipx if not already installed
                sh 'python3 -m pip install --user pipx'
                // Install dependencies with pipx
                sh 'pipx install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests with pipx environment
                sh 'pipx run python3 -m unittest discover -s tests'
            }
        }
        stage('Deploy Application') {
            steps {
                // Deploy the application with pipx environment
                sh 'pipx run python3 app.py &'
            }
        }
    }
}

