pipeline {
        agent any
        stages {
            stage('Build') {
                steps {
                    git branch: 'main', credentialsId: 'Github1', url: 'https://github.com/Aishaml1/CryptoSocial'
                }
            }
            stage('Test') {
                steps {
                    sh 'python3 CryptoNetwork/manage.py test ./CryptoNetwork'
                }
            }
        }
    }