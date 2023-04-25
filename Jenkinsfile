pipeline {
    environment {
        registry = "moiseevdi/simple-back"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    tools {nodejs "node" }
    stages {
        stage('SonarQube analysis') {
            steps {
                script {
                    withSonarQubeEnv('sonarasus') {
                        sh "sonar-scanner"
                    }
                    timeout(time: 1, unit: "HOURS") {
                        def qualitygate = waitForQualityGate()
                        if (qualitygate.status != "OK") {
                            waitForQualityGate abortPipeline: true
                        }
                    }
                }
            }
        }
        stage('Building image') {
            steps{
                script {
                dockerImage = docker.build registry + ":$BUILD_NUMBER"
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
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
