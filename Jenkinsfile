pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-creds' // Jenkins credentials ID
        IMAGE_NAME = 'yourdockerhubusername/mlops-case-study'
        IMAGE_TAG = "${env.BUILD_ID}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }
        stage('Run Docker Image (Test)') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout || true'
        }
    }
}
