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
