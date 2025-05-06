pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'kshah1025/student-survey:latest'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', git credentialsId: 'github-creds', url: 'https://github.com/Kush1025/Extra_Credit.git'
            }
        }

        

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Login & Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl rollout restart deployment student-survey'
            }
        }
    }
}
