import requests

def send_post_request(entity_id):
    urlPost = 'https://********.live.dynatrace.com/api/v2/settings/objects'
    headersPost = {
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Api-Token **********************'
    }

    payload = [{
        "schemaId": "builtin:host.monitoring",
        "schemaVersion": "1.4",
        "scope": f"{entity_id}",
        "value": {"enabled": False}
    }]

    responsePost = requests.post(urlPost, headers=headersPost, json=payload)

    if responsePost.status_code == 200:
        print(f"Scope updated for entity ID: {entity_id}")
    else:
        print(f"Failed to update scope for entity ID: {entity_id}. Status code: {responsePost.status_code}")

urlGet = 'https://************.live.dynatrace.com/api/v2/entities?pageSize=150&entitySelector=type%28%22HOST%22%29%2ChealthState%28%22HEALTHY%22%29'
headers1 = {
    'accept': 'application/json; charset=utf-8',
    'Authorization': 'Api-Token ******************************'
}

responseGet = requests.get(urlGet, headers=headers1)
if responseGet.status_code == 200:
    data = responseGet.json()
    entities = data.get('entities', [])
    counter = 0

    entity_ids = []
    for entity in entities:
        entity_id = entity.get('entityId')
        if entity_id:
            entity_ids.append(entity_id)

    for entity_id in entity_ids:
        send_post_request(entity_id)
        counter += 1
    print(f"Number of hosts Disabled: {counter}")
else:
    print(f"Failed to retrieve data. Status code: {responseGet.status_code}")


