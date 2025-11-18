pipeline {
    agent any

    stages {

        stage('Pull') {
            steps { git 'https://github.com/yourrepo/classroom-generator.git' }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Extract Text') {
            steps {
                sh 'python backend/api.py --extract-only'
            }
        }

        stage('Generate Materials') {
            steps {
                sh 'python backend/api.py --generate-only'
            }
        }

        stage('Create PDFs') {
            steps {
                sh 'python backend/api.py --pdf-only'
            }
        }

        stage('Publish Output') {
            steps {
                archiveArtifacts artifacts: 'output/*.pdf'
            }
        }
    }
}