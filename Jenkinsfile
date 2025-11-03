pipeline {
    agent any

    environment {
        // Docker Hub credentials ID in Jenkins
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
        // Docker Hub username
        DOCKER_USERNAME = 'divyanshu123'
        // Docker image name
        IMAGE_NAME = 'mlops-case-study'
        // GitHub credentials ID in Jenkins
        GIT_CREDENTIALS_ID = 'github-creds'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                git(
                    url: 'https://github.com/Divyanshu592/ai_final.git',
                    branch: 'master',
                    credentialsId: "${GIT_CREDENTIALS_ID}"
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    bat "docker build -t ${DOCKER_USERNAME}/${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Run Docker Image (Test)') {
            steps {
                script {
                    // Run container for testing
                    bat "docker run --rm ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        bat "docker login -u %USER% -p %PASS%"
                        // Push image
                        bat "docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:latest"
                        bat "docker logout"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs."
        }
    }
}
