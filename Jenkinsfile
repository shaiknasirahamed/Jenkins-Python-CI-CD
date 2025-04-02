pipeline {
    agent any
    environment {
        // Set environment variables, like the GitHub repo URL and credentials if needed
        GIT_URL = 'https://github.com/shaiknasirahamed/Jenkins-Python-CI-CD.git'
    }
    stages {
        stage('Checkout Repository') {
            steps {
                // Checkout the specific branch
                git url: GIT_URL, branch: 'main', credentialsId: 'github-credentials-id'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies from the requirements.txt file
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run Python unit tests
                sh 'python3 -m unittest discover -s tests'
            }
        }
        stage('Deploy Application') {
            steps {
                // Deploy the application using nohup
                sh 'nohup python3 app.py &'
            }
        }
    }
}

