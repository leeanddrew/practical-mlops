from locust import HttpUser, task, between

class HelloUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def call_hello(self):
        self.client.post("/hello", json={"name": "Andrew"})