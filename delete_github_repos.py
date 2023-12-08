'''
Script Purpose:
Deletes specified GitHub repositories using PyGithub,
utilising GitHub username and personal access token from environment variables (GITHUB_USERNAME and GITHUB_TOKEN).

Pre-requisites:
To run the script successfully, you'll need to install the PyGithub library
and possibly the python-dotenv library if you plan to use environment variables for your credentials.

Note-1: Ensure environment variables GITHUB_USERNAME and GITHUB_TOKEN are set with your GitHub credentials.
Usage: python delete_github_repos.py -r REPO_NAME [REPO_NAME ...]
    -r, --repos      List of repository names to delete

Note-2: If the environment variables are not defined, specify the username and token using -u and -t options respectively.
    Usage: delete_github_repos.py [-h] [-u USERNAME] [-t TOKEN] -r REPOS [REPOS ...]
'''
import os
import argparse
from github import Github

def delete_repositories(username, access_token, repos_to_delete):
    g = Github(username, access_token)

    for repo_name in repos_to_delete:
        try:
            repo = g.get_user().get_repo(repo_name)
            if repo:
                repo.delete()
                print(f"Repository '{repo_name}' has been deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting '{repo_name}': {e}")

def main():
    parser = argparse.ArgumentParser(description='Delete GitHub repositories.')
    parser.add_argument('-u', '--username', default=os.getenv('GITHUB_USERNAME'), help='Your GitHub username')
    parser.add_argument('-t', '--token', default=os.getenv('GITHUB_TOKEN'), help='Your GitHub personal access token')
    parser.add_argument('-r', '--repos', nargs='+', required=True, help='List of repository names to delete')

    args = parser.parse_args()
    delete_repositories(args.username, args.token, args.repos)

if __name__ == "__main__":
    main()