pipeline {
    environment {
        registry = "moiseevdi/ip-simple-back"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Building image') {
            steps{
                script {
                dockerImage = docker.build registry + ":latest"
                }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $registry:latest"
            }
        }
    }
}
