from testbase import Testbase
from locust import HttpLocust, task
import logging
import time

logger = logging.getLogger(__name__)


class PostImg(Testbase):

    @task(1)
    def post_225k_image(self):
        time_start = time.time()
        self.post_image('Zhang.jpg')
        response = self.client.get("/")
        time_end = time.time()
        logger.info("Response - URL: {url}. Status code: {status}. "
                    "Latency: {duration}".format(url=response.url,
                                                 status=response.status_code,
                                                 duration=round(time_end - time_start, 3)))

    @task(2)
    def post_15k_image(self):
        time_start = time.time()
        self.post_image('Eareyan.jpg')
        response = self.client.get("/")
        time_end = time.time()
        logger.info("Response - URL: {url}. Status code: {status}. "
                    "Latency: {duration}".format(url=response.url,
                                                 status=response.status_code,
                                                 duration=round(time_end - time_start, 3)))

class WebsiteUser(HttpLocust):
    task_set = [PostImg]