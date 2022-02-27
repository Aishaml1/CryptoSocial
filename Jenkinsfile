pipeline {
        agent any
        stages {
            stage('SCM checkout') {
                steps {
                    git branch: 'main', credentialsId: '36f5cbfb-972e-4a45-8024-a5bb059e929a', url: 'https://github.com/JQstrategio/CryptoSocial'
                }
            }
            stage('Build') {
                steps {
                    //cleans up work space
                    step([$class: 'WsCleanup' ])

                    //clone repo
                    sh 'git clone https://github.com/JQstrategio/CryptoSocial'

                    //package python application and copy to remote server

                }
            }
            stage('Test') {
                steps {
                    sh 'python3 -m pytest CryptoSocial/tests/test_p1.py --verbose'
                }
            }
        }
    }