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

                    //a plug in that cleans up our workspace
                    step($class:wsCleanup)
                    //clone repository 
                    sh 'git clone https://github.com/Aishaml1/CryptoSocial.git'
                    // install all packages
                    sh 'pip install -r requirements.txt'
                }
            }
            stage('Test') {
                steps {
                    //verbose displays or gets extended information.
                    sh 'python3 -m  pytest CryptoSocial/tests/test_p1.py --verbose '
                }
            }
        }
    }