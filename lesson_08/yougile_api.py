import os

import requests


class YouGileApi:
    BASE_URL = "https://yougile.com/api-v2"

    def __init__(self):
        token = os.getenv("YOUGILE_API_TOKEN")

        if not token:
            raise RuntimeError(
                "Не задана переменная окружения YOUGILE_API_TOKEN"
            )

        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def create_project(self, title):
        return requests.post(
            f"{self.BASE_URL}/projects",
            headers=self.headers,
            json={"title": title},
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
            json={"title": title},
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
        )

    def delete_project(self, project_id):
        return requests.delete(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
        )
