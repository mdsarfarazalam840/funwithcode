from locust import HttpUser, between, task

class MyUser(HttpUser):
    #Setting a wait time of between 2 numbers
    wait_time = between(5,15)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_users(self):
        self.client.get("/users")

    #Create a task to create a new post on the API
    @task
    def create_post(self):
        #Defining the data to be posted
        data={
            "title":"NEW POST",
            "body":"This is new post",
            "userId": 1
        }
        headers = {"Content-type","application/json"}
        self.client.post("/posts", json=data, headers=headers)