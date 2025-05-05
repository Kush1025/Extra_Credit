pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // defined in Jenkins Credentials
    DOCKER_IMAGE = "kshah1025/student-survey:latest"
    KUBECONFIG = "$HOME/.kube/config"
  }

  stages {
    stage('Clone Repo') {
      steps {
        git branch: 'main', url: 'https://github.com/Kush1025/Extra_Credit.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Login to DockerHub') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }

    stage('Push Docker Image') {
      steps {
        sh 'docker push $DOCKER_IMAGE'
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        withEnv(["KUBECONFIG=$KUBECONFIG"]) {
          sh '''
            kubectl apply -f k8s/deployment.yaml
            kubectl apply -f k8s/service.yaml
            kubectl rollout restart deployment student-survey
          '''
        }
      }
    }
  }

  post {
    failure {
      echo "Pipeline failed. Check logs for details."
    }
    success {
      echo "Deployment successful!"
    }
  }
}
