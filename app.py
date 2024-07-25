# lambda-code

#deploying using AWS CLI..

'''
#workinf code for COdeQL
import json
import boto3
from botocore.exceptions import ClientError

# Initialize ECS client
ecs_client = boto3.client('ecs')

def lambda_handler(event, context):
    # Parse the GitHub webhook payload
    job = "Other Job"
    
    try:
        payload = json.loads(event['body'])
        
        # Check if 'workflow_job' key exists in the payload
        if 'workflow_job' in payload:
            workflow_job = payload['workflow_job']
            workflow_job_name = workflow_job['name']
            workflow_job_status = workflow_job['status']
            
            if "Lambda" in workflow_job_name and workflow_job_status == "queued":
                print("CodeQL job found and status is queued")
                job = "CodeQL"
                
                # Run ECS Fargate task
                response = run_fargate_task()
                print(f"Fargate task response: {response}")
            else:
                print("Job is not a CodeQL job or status is not queued")
        else:
            print("'workflow_job' key not found in the payload")

    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps("Invalid JSON format")
        }
    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing key: {e}")
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal server error: {e}")
        }

    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps(job)
    }

def run_fargate_task():
    try:
        response = ecs_client.run_task(
            cluster='github-ephemeral-test',  # ECS cluster name
            taskDefinition='github-runner',  # Task definition
            launchType='FARGATE',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-0d2eb50770ac514ad'],  # Subnet ID
                    'securityGroups': ['sg-01bccd59b38827c5e'],  # Security group ID
                    'assignPublicIp': 'ENABLED'  # or 'DISABLED'
                }
            }
        )
        return response
    except ClientError as e:
        print(f"ClientError: {e}")
        return f"Error running Fargate task: {e}" '''
#-------------------------------------------------------------------------------------------------

#check the dependency review Functionality.
import json
import boto3
from botocore.exceptions import ClientError

# Initialize ECS client
ecs_client = boto3.client('ecs')

def lambda_handler(event, context):
    # Parse the GitHub webhook payload
    job = "Other Job"
    
    try:
        payload = json.loads(event['body'])
        
        # Check if 'workflow_job' key exists in the payload
        if 'workflow_job' in payload:
            workflow_job = payload['workflow_job']
            workflow_job_name = workflow_job['name']
            workflow_job_status = workflow_job['status']
            
            if "Analyze" in workflow_job_name and workflow_job_status == "queued":
                print("CodeQL job found and status is queued")
                job = "CodeQL"
                
                # Run ECS Fargate task for CodeQL
                response = run_fargate_task('github-runner')
                print(f"Fargate task response: {response}")
            elif workflow_job_name == "dependency-review" and workflow_job_status == "queued":
                print("Dependency review job found and status is queued")
                job = "Dependency Review"
                
                # Run ECS Fargate task for Dependency Review
                #response = run_fargate_task('dependency-review-runner')
                #print(f"Fargate task response: {response}")
            else:
                print("Job is not a CodeQL or Dependency Review job, or status is not queued")
        else:
            print("'workflow_job' key not found in the payload")

    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps("Invalid JSON format")
        }
    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing key: {e}")
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal server error: {e}")
        }

    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps(job)
    }

def run_fargate_task(task_definition):
    try:
        response = ecs_client.run_task(
            cluster='github-ephemeral-test',  # ECS cluster name
            taskDefinition=task_definition,  # Task definition
            launchType='FARGATE',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-0d2eb50770ac514ad'],  # Subnet ID
                    'securityGroups': ['sg-01bccd59b38827c5e'],  # Security group ID
                    'assignPublicIp': 'ENABLED'  # or 'DISABLED'
                }
            }
        )
        return response
    except ClientError as e:
        print(f"ClientError: {e}")
        return f"Error running Fargate task: {e}"





#-------------------------------------------------------------
'''import json
import boto3
from botocore.exceptions import ClientError

# Initialize ECS client
ecs_client = boto3.client('ecs')

def lambda_handler(event, context):
    # Parse the GitHub webhook payload
    job = "Other Job"
    
    try:
        payload = json.loads(event['body'])
        
        # Check if 'workflow_job' key exists in the payload
        if 'workflow_job' in payload:
            workflow_job_name = payload['workflow_job']['name']
            
            if "Analyze" in workflow_job_name:
                print("codeql job found")
                job = "CodeQL"
                
                # Run ECS Fargate task
                response = run_fargate_task()
                print(f"Fargate task response: {response}")
            else:
                print("not a codeql job")
        else:
            print("'workflow_job' key not found in the payload")

    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps("Invalid JSON format")
        }
    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing key: {e}")
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal server error: {e}")
        }

    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps(job)
    }

def run_fargate_task():
    try:
        response = ecs_client.run_task(
            cluster='github-ephemeral-test',  # ECS cluster name
            taskDefinition='github-runner',  # Task definition
            launchType='FARGATE',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-0d2eb50770ac514ad'],  # Subnet ID
                    'securityGroups': ['sg-01bccd59b38827c5e'],  # Security group ID
                    'assignPublicIp': 'ENABLED'  # or 'DISABLED'
                }
            }
        )
        return response
    except ClientError as e:
        print(f"ClientError: {e}")
        return f"Error running Fargate task: {e}"  '''






#-----------------------------------------------------------------






'''import json

def lambda_handler(event, context):
    # Parse the GitHub webhook payload
    job = "Other Job"
    
    try:
        payload = json.loads(event['body'])
        
        # Check if 'workflow_job' key exists in the payload
        if 'workflow_job' in payload:
            workflow_job_name = payload['workflow_job']['name']
            
            if "Analyze" in workflow_job_name:
                print("codeql job found")
                job = "CodeQL"
            else:
                print("not a codeql job")
        else:
            print("'workflow_job' key not found in the payload")

    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps("Invalid JSON format")
        }
    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Missing key: {e}")
        }
    except Exception as e:
        print(f"Exception: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal server error: {e}")
        }

    # Return a success response
    return {
        'statusCode': 200,
        'body': json.dumps(job)
    }'''












'''import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }'''
