import requests
import json
import threading
from queue import Queue
import csv

class GitHubUser:
    def __init__(self, username):
        self.username = username

    def get_user_info(self):
        API_URL = "https://api.github.com/users/{}".format(self.username)
        response = requests.get(API_URL)
        
        if response.status_code == 200:
            user_data = json.loads(response.text)
            return user_data
        else:
            return None

def producer(queue):
    usernames = ["Bishal", "ram", "shyam", "lilly", "geeta", "hari", "pawan", "jonh", "waden", "salman"]
    for username in usernames:
        user = GitHubUser(username)
        queue.put(user)

def consumer(queue, writer):
    while True:
        user = queue.get()
        user_info = user.get_user_info()
        if user_info:
            try:
                filtered_info = {key: user_info[key] for key in fieldnames if key in user_info}
                writer.writerow(filtered_info)
            except ValueError:
                print("Skipping user fields not in fieldnames:", user.username)
        else:
            print("Error retrieving user:", user.username)
        queue.task_done()

# Create a shared queue
queue = Queue()

producer_thread = threading.Thread(target=producer, args=(queue,))
producer_thread.start()

num_consumers = 10
consumer_threads = []
csv_file = open("user_info.csv", "w", newline="")
fieldnames = ["following", "name","id"]
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

for _ in range(num_consumers):
    t = threading.Thread(target=consumer, args=(queue, writer))
    t.start()
    consumer_threads.append(t)


queue.join()

# Wait for producer and consumer threads to complete
producer_thread.join()
for t in consumer_threads:
    t.join()

csv_file.close()
