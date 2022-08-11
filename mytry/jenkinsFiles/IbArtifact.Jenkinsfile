//for this pipline will be relevant - when reading the file from resources in jenkins-lib
library identifier: 'jenkins-libs@master', retriever: modernSCM(
  [$class: 'GitSCMSource',
   remote: 'https://github.com/taimax13/jenkins.git',
   credentialsId: 'talex-token'])

pipeline {
    agent {
        kubernetes {
            defaultContainer 'node-js'
            yamlFile 'k8s/jenkins-slave.yaml'
        }
    }
    environment {
       //WD for the artifact re-naming 
        ARTIFACT_WORKDIR = "Generated/SourceCodeArtifacts/JavaScript/GeneratedVocab/" 
    }
    stages {
        stage("Get TEMP"){
            steps{
                echo "====++++getting temperature++++===="
                script{
                    container("python3") {
                        sh """
                            TMP=$(python tmp_reqiest.py) 
                            echo "$TMP"
                        """
                    }
                }
            }
        }
        stage('Buil_Rename') {
            steps {
                println("Build and re-name artifact")
                dir("${ARTIFACT_WORKDIR}"){
                sh """
                    npm -g install @inrupt/artifact-generator         
                   """
            }}
        }
        stage('Upload to S3') {
            steps {
                withAWS(roleAccount: "${ACCOUNT_NUMBER}", role: 'JenkinsCrossAccountRole') {
                    dir("${ARTIFACT_WORKDIR}") {
                        sh """
                            aws codeartifact login --tool npm --domain my_domain --domain-owner test --repository test_repo
                            npm install ib_rock
                            npm publish
                        """
                    }
                }
            }
        } 
}