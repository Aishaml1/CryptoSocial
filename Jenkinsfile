 pipeline {
        agent {
            docker { image 'python:3.9' }
        }
        stages {
            stage('Build') {
                steps {
                    //install all the packages 
                    sh 'pip install -r requirements.txt'
                }
            }

            stage('Test') {
                steps {
                    sh 'python CryptoNetwork/manage.py test ./CryptoNetwork'
                }
            }

            stage('Deploy') {
                steps {
                    sh 'none yet'
                }
            }
        }
    }