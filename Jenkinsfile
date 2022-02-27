pipeline {
        agent any
        stages {
            stage('SCM checkout') {
                steps {
                    git branch: 'main', credentialsId: 'Github1', url: 'https://github.com/Aishaml1/CryptoSocial'
                }
            }
            stage('Build') {
                steps {
                    //cleans up work space
                    step([$class: 'WsCleanup' ])
                    sh 'git clone https://github.com/Aishaml1/CryptoSocial.git'
                    //package python application and copy to remote server

                }
            }
            stage('Test') {
                steps {
                    echo 'the job has been tested'
                }
            }
        }
    }