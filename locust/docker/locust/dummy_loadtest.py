# 还不知道怎么写
import uuid
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def post_metrics(self):
        self.client.post(
            "/", {"file": self.file})
#我真的在乱写 根本不知道数据是怎么传的

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet