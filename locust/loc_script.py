from locust import HttpLocust, TaskSet, task
import json

class UserBehavior(TaskSet):
    
    @task(2)
    def get_user(self):
        headers_ = {"content-type": "application/json"}
        self.client.get("api/v1/user", headers=headers_)

    @task(1)
    def post_user(self):
        headers_ = {"content-type": "application/json"}
        self.client.post("api/v1/user", data=json.dumps({}),  headers=headers_)

class ReportBehavior(TaskSet):
    
    @task(1)
    def post_report(self):
        headers_ = {"content-type": "application/json"}
        self.client.post("api/v1/report", data=json.dumps({}),  headers=headers_)

class StatusBehaviour(TaskSet):
    
    @task(2)
    def check_liveness(self):
        headers_ = {"content-type": "application/json"}
        self.client.get("api/v1/liveness",  headers=headers_)

    @task(1)
    def check_readiness(self):
        headers_ = {"content-type": "application/json"}
        self.client.get("api/v1/readiness",  headers=headers_)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

class WebsiteReport(HttpLocust):
    task_set = ReportBehavior
    min_wait = 5000
    max_wait = 9000

class WebsiteStatus(HttpLocust):
    task_set = StatusBehaviour
    min_wait = 5000
    max_wait = 9000