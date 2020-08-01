from locust import TaskSet
import io

class Testbase(TaskSet):
    def post_image(self, image_file):
        self.post_images([image_file])

    def post_images(self, image_files):
        for item in image_files:
            file_bytes = self.load_file(item)
            br = io.BufferedReader(io.BytesIO(file_bytes))
            self.client.post("" ,files = {'image_file':br})

