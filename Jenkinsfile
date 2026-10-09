
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
                sh 'docker build -t mansur-app:${BUILD_NUMBER} -t mansur-app:latest app'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose --project-directory /home/mansur/devops_project -f /home/mansur/devops_project/compose.yaml up -d --no-deps --force-recreate app'
            }
        }
    }
}


