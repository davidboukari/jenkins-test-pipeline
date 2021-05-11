pipeline
{
  agent any
  stages
  {
    stage('Sonarqube')
    {
      environment
      {
        scannerHome = tool 'SonarQubeScanner'
      }
      steps
      {
        withSonarQubeEnv('sonarqube-jenkins-test-pipeline')
        {
          sh "${scannerHome}/bin/sonar-scanner"
        }
        timeout(time: 10, unit: 'MINUTES')
        {
          waitForQualityGate abortPipeline: true
        }
      }
    }  
   
    stage('Notification Email')
    {
       steps
       { 
         echo "Send Notification"
         echo "Title: ${env.MAIL_SUBJECT}"
         echo "To: ${env.MAIL_TO}"
         echo "Message: ${env.MAIL_MESSAGE}"
         sh "printenv"

         if( ${env.MAIL_MESSAGE} != "No message")
         {
           // Send an email
           emailext body: "${env.MAIL_MESSAGE}", subject: "${env.MAIL_SUBJECT}", to: "${env.MAIL_TO}"
         }
         else
         {
           echo "The body of the message is empty => Nothing to send"
         }

       } 
    }
/*
    stage('Notification Mattermost')
    {
       steps
       { 
         // Send to Mattermost webhook
          mattermostSend (
            color: "#2A42EA",
            channel: 'devops',
            endpoint: 'http://192.168.0.133:8065/hooks/uwfu8ohdojyi9gbf1gtykkyzeo', 
            message: "Hello from jenkins pipeline --"
          ) 
       } 
    }
*/
/*    
    stage('GIT')
    {
       steps
       { 
         echo 'Get the git source ...'
         sleep(2)         
       } 
    }
  
    stage('Unit Tests')
    {
      steps
      {
        echo 'Unit Tests...'
        //sh 'pip install --upgrade --user tox'
        sh 'tox -r'
      }
    }
  
    stage('Security Tests')
    {
      steps
      {
        echo 'Security Tests...'
        sleep(2)
        //sh 'tox -r -e envsecurity'
      }
    }
  
    stage('Sonarqube')
    {
      environment
      {
        scannerHome = tool 'SonarQubeScanner'
      }    
      steps
      {
        withSonarQubeEnv('sonarqube')
        {
          sh "${scannerHome}/bin/sonar-scanner"
        } 
        timeout(time: 10, unit: 'MINUTES')
        {
          waitForQualityGate abortPipeline: true
        }
      }
    }
  
    stage('Deployment')
    {
      steps
      {  
        echo 'Deployment...'
        sleep(2)
        // DEV
  
        // UAT
  
        // PRD
      }
    }
*/  

  }

  post {
    always {
        emailext body: "Success From jenkins msg...", subject: "From jenkins Success job ...", to: 'root@localhost' 
    }
  }

}

