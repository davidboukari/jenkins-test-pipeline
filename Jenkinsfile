pipeline
{
  agent any
  stages
  {
    
    stage('Notification Email')
    {
       steps
       { 
         // Send an email
         emailext body: "From jenkins msg...", subject: "From jenkins start job ...", to: "${mail_to}"
       } 
    }

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

