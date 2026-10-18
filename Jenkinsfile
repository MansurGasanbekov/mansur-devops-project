
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

        stage('Health Check') {
            steps {
                sh '''
                    for i in 1 2 3 4 5 6 7 8 9 10; do
                        if curl -fsS --max-time 5 http://127.0.0.1:5000/health; then
                            echo "Health Check passed!"
                            exit 0
                        fi

                        echo "Waiting for Flask... Attempt $i/10"
                        sleep 3
                    done

                    echo "Health Check failed!"
                    exit 1
                '''
            }
        }
    }
}
