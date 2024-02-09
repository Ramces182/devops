import requests
import json

DT_TENANT = "******.dynatrace.com"
DT_API_TOKEN = "******************************"


def get_latest_oneagent_metainfo():
    url = f"https://{DT_TENANT}/api/v1/deployment/installer/agent/unix/default/latest/metainfo?flavor=default&arch=all&bitness=all"
    headers = {
        "Authorization": f"Api-Token {DT_API_TOKEN}",
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            response = response.json()
            print(response)
            version = response['latestAgentVersion']
            print(version)
            return version
        except:
            print("Failed to parse JSON response:", e)
    else:
        print("Request failed with status code:", response.status_code)


def download_oneagent_installer(version):
    url = f"https://{DT_TENANT}/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default"
    headers = {"Authorization": f"Api-Token {DT_API_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f"Dynatrace-OneAgent-Linux-{version}.sh", "wb") as f:
            f.write(response.content)
        print(f"OneAgent installer saved as Dynatrace-OneAgent-Linux-{version}.sh")
    else:
        print(f"Failed to download OneAgent installer. Status code: {response.status_code}")


if __name__ == "__main__":
    try:
        version = get_latest_oneagent_metainfo()
        download_oneagent_installer(version)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
