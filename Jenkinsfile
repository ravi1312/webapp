@Library('github.com/releaseworks/jenkinslib') _

node {
  stage("List S3 buckets") {
    withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 's3backupuser', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
        AWS("s3 ls")
     sh 'chmod 700 ./backup.sh ./githubrepolist.sh'
     sh './githubrepolist.sh >output.txt'
     sh 'cat ./ouput.txt'
      sh '''
          pwd
          ls -ltr
          '''
      
    }
  }
}
