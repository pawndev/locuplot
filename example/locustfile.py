from locust import HttpUser, task, between


class Eta(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def get_home(self):
        self.client.get(url="/",
                        name="GetHome")

    @task(2)
    def get_known_issues(self):
        self.client.get(url="/known-issues/index.html",
                        name="GetKnownIssues")
