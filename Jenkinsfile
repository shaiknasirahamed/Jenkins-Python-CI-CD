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
        stage('Setup Virtual Environment') {
            steps {
                // Set up virtual environment
                sh 'python3 -m venv venv'
                // Activate the virtual environment
                sh '. venv/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies in the virtual environment
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests within the virtual environment
                sh '. venv/bin/activate && python3 -m unittest discover -s tests'
            }
        }
        stage('Deploy Application') {
            steps {
                // Deploy the application in the background
                sh '. venv/bin/activate && nohup python3 app.py &'
            }
        }
    }
}

