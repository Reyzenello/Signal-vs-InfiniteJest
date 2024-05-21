import requests
import json
import os
from datetime import datetime

# Configuration
GITHUB_API_URL = "https://api.github.com/search/repositories"
QUERY = "artificial intelligence open source"
OUTPUT_FILE = "ai_open_source_repos.json"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_repositories(query):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }
    response = requests.get(GITHUB_API_URL, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["items"]

def extract_repo_details(repositories):
    repo_details = []
    for repo in repositories:
        repo_details.append({
            "name": repo["name"],
            "full_name": repo["full_name"],
            "html_url": repo["html_url"],
            "description": repo["description"]
        })
    return repo_details

def save_repos_to_file(repo_details):
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(repo_details, f, indent=4)

def main():
    repositories = fetch_repositories(QUERY)
    repo_details = extract_repo_details(repositories)
    save_repos_to_file(repo_details)
    print(f"Fetched and saved {len(repo_details)} open-source AI repositories")
    print(f"Data saved to {OUTPUT_FILE}")

    # Print the contents of the file to check if it has data
    with open(OUTPUT_FILE, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()
