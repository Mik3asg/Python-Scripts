'''
This script is intending to delete the following resources
  kubectl delete deploy --all
  kubectl delete svc --all
  kubectl delete ingress --all
'''
# Allows Python code to run external commands and interact with system processes
import subprocess   

def delete_all_resources():
    subprocess.run(
        ["kubectl", "delete", "deploy", "--all"],
        check=True,
    )
    subprocess.run(
        ["kubectl", "delete", "svc", "--all"],
        check=True,
    )
    subprocess.run(
        ["kubectl", "delete", "ingress", "--all"],
        check=True,
    )
    print("All deployments, services, and ingresses deleted.")

delete_all_resources()