pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'echo "Testing application..."'
                sh 'python3 -m py_compile app/app.py'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Checking Docker..."'
                sh 'docker --version'
                sh 'docker ps'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to staging...'
            }
        }
    }
}
