from locust import TaskSet

class Testbase(TaskSet):
    def post_image(self, image_file):
        self.post_image([image_file])