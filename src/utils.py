import re
import requests
from typing import Optional, Tuple

import time

def get_repo_info(repo_link: str) -> Optional[Tuple[str, str]]:
    # Regular expression pattern to match GitHub repository link
    pattern = r"https://github\.com/([^/]+)/([^/]+)"

    match = re.match(pattern, repo_link)
    if match:
        owner = match.group(1)
        repo_name = match.group(2)

        # Making a request to the GitHub API to get repository information
        api_url = f"https://api.github.com/repos/{owner}/{repo_name}"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            # repo_info = response.json()
            # author = repo_info['owner']['login']
            return owner, repo_name

    raise Exception("Invalid github URL!")

def getCurrentTime() -> str:

    """
    A function that returns the local time in the form of HH-MM-SS.
    """

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time
