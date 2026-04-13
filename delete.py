import requests
import time

USERNAME = "your-username"
TOKEN = "your-token"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repositories():
    repos = []
    page = 1

    while True:
        response = requests.get(
            f"https://api.github.com/user/repos?affiliation=owner&page={page}&per_page=100",
            headers=HEADERS
        ).json()

        if not response:
            break

        repos.extend(response)
        page += 1

    return repos


def delete_repository(repo_name):
    while True:
        try:
            print(f"Deleting: {repo_name}")

            response = requests.delete(
                f"https://api.github.com/repos/{USERNAME}/{repo_name}",
                headers=HEADERS
            )

            print(f"Status: {response.status_code}")

            if response.status_code == 204:
                print("Deleted ✅")
                break
            else:
                print(f"Error: {response.text}")
                time.sleep(5)

        except Exception as e:
            print(f"Network error: {e}")
            time.sleep(5)


def main():
    repos = get_repositories()
    print(f"Found {len(repos)} repositories")

    for repo in repos:
        delete_repository(repo["name"])
        time.sleep(2)

    print("DONE 💣")


if __name__ == "__main__":
    main()
