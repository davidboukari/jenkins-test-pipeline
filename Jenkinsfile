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
        script
        {
          def scmVars = checkout scm
          //println scmVars.toString() 
          SERVER_FILE_MAIL = 'server_mail.csv'
          if( MAIL_MESSAGE != "No subject" )
          {
            map_all_server = [:]
            if (fileExists(SERVER_FILE_MAIL))
            {
              echo SERVER_FILE_MAIL + ' found OK'
              error_lines = ''
              readFile(SERVER_FILE_MAIL).split('\n').eachWithIndex
              {
                line, count -> def fields = line.split(';')
                try
                {
                  map_all_server[fields[0]] = fields
                }
                catch( Exception e )
                {
                  println e
                  error_lines += "line:" + count + " - content:" + line + "\n"
                } 
              }
              if( error_lines != '' )
              {
                println "Send mail for:\n" + error_lines
                try
                {
                  body_message = "File: ${scmVars.GIT_URL}/blob/${scmVars.GIT_BRANCH}/${SERVER_FILE_MAIL}\nJob: ${BUILD_URL}\n\n${error_lines}"
                  emailext  to: MAIL_TO, subject: "Error in file ${SERVER_FILE_MAIL}", body: body_message
                }
                catch(Exception e)
                {
                  println e
                }
              }
              map_all_server.each
              {
                key, value -> println key.toString() + '-' + value.toString()
              }
            }
            else
            {
              error('Aborting: Machines.csv Not found. Failing.')
            }
            String param_server_list="srv,Code,Timestamp\nmyserver5,CODEA2,2021-05-11T12:37:42,(60%)\nmysever4,CODEA2,2021-05-11T12:39:47,(60%)\nmyserver3,CODEA2,2021-05-11T12:33:48,(60%)\nmyserver10,CODEA2,2021-05-11T12:31:46,(60%)\nmysever8,CODEA2,2021-05-11T12:39:43,(60%)\n"
            mail_to = "unknown@localhost.localdomain"
            mail_subject = "Metric CPU errors"

            String[] list_server_on_error = param_server_list.tokenize('\n')
            line = 0
            for( String my_server_info:  list_server_on_error)
            {
              if( line > 0 )
              {
                println my_server_info;
                my_server = my_server_info.tokenize(',')[0]
                println "--->" + my_server
                try
                {
                  // Find mail
                  csv_info = map_all_server[my_server]
                  email_addr = csv_info[4]
                  // Add the Team to the subject 
                  email_subject = mail_subject + ' - (' +  csv_info[3]  + ')'
                  println "------------>" + email_addr
                }
                catch( Exception e)
                {
                  println "Server not found in the CSV file"
                  email_addr = mail_to
                  email_subject = mail_subject
                }
                email_message = my_server_info
                println "emailext body: " + email_message + ", subject: " + email_subject + ", to: " + email_addr
                try
                {
                  emailext body: "${email_message}", subject: "${email_subject}", to: "${email_addr}"
                }
                catch(Exception e)
                {
                  println e
                }  
              }
              line++
             }
           }
           else
           {
             println "There is no message to send"
           }
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
    always 
    {
      try
      {
        emailext body: "Success From jenkins msg...", subject: "From jenkins Success job ...", to: 'root@localhost'
      }
      catch(Exception e)
      {
        println e
      }
    }
  }

}

