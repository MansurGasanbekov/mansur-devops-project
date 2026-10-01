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
                sh 'docker build -t mansur-app:${BUILD_NUMBER} app'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to staging...'
            }
        }
    }
}
