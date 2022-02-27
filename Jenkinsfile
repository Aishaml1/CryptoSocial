pipeline {
        agent any
        stages {
            stage('Build') {
                steps {
                    //cleans up work space
                    step([$class: 'WsCleanup' ])
                    //clone repo
                    sh 'git clone https://github.com/Aishaml1/CryptoSocial.git'
                    //package python application and copy to remote server
                }
            }
            stage('Test') {
                steps {
                    //verbose displays or gets extended information.
                    sh 'python3 -m pytest CryptoNetwork/tests/test_p1.py --verbose'
                }
            }
        }
    }