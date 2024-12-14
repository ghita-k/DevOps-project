from locust import HttpUser, task

class VideoServiceUser(HttpUser):
    @task
    def upload_video(self):
        self.client.post("/upload", files={"file": open("video.mp4", "rb")})
