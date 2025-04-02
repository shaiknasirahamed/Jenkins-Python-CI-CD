pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/shaiknasirahamed/Jenkins-Python-CI-CD.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest discover -s tests'
            }
        }
        stage('Deploy Application') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}

