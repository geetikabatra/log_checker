# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Geetika Batra <geetika791@gmail.com>
#

"""Class for locust server."""

from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):
    """Contains locust test for endpoint user."""

    @task(2)
    def get_user(self):
        """Get method for /user."""
        headers_ = {"content-type": "application/json"}
        self.client.get("api/v1/user", headers=headers_)

    @task(1)
    def post_user(self):
        """Post method for /user."""
        headers_ = {"content-type": "application/json"}
        self.client.post("api/v1/user", data=json.dumps({}), headers=headers_)


class ReportBehavior(TaskSet):
    """Contains locust test for endpoint /report."""

    @task(1)
    def post_report(self):
        """Post method for /report."""
        headers_ = {"content-type": "application/json"}
        self.client.post(
            "api/v1/report",
            data=json.dumps(
                {}),
            headers=headers_)


class StatusBehaviour(TaskSet):
    """Contains locust test for endpoint /liveness and /readiness."""

    @task(2)
    def check_liveness(self):
        """Get method for /liveness."""
        headers_ = {"content-type": "application/json"}
        self.client.get("api/v1/liveness", headers=headers_)

    @task(1)
    def check_readiness(self):
        """Get method for /readiness."""
        headers_ = {"content-type": "application/json"}
        self.client.get("api/v1/readiness", headers=headers_)


class WebsiteUser(HttpLocust):
    """Initiates Locust test for User."""

    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000


class WebsiteReport(HttpLocust):
    """Initiates Locust test for Report."""

    task_set = ReportBehavior
    min_wait = 5000
    max_wait = 9000


class WebsiteStatus(HttpLocust):
    """Initiates Locust test for Status."""

    task_set = StatusBehaviour
    min_wait = 5000
    max_wait = 9000
