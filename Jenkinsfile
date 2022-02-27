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
                    step([$class: 'WsCleanup' ])
                    sh 'git clone https://github.com/Aishaml1/CryptoSocial.git'
                }
            }
            stage('Test') {
                steps {
                    sh 'python3 -m pytest CryptoNetwork/tests/test_p1 --verbose'
                }
            }
        }
    }