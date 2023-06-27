from flask import Flask, render_template
import requests

app = Flask(__name__)

urls = [
    "https://www.tiktok.com/@lyvoi5/video/7235777025716407579",
    "https://www.tiktok.com/@twenty4tim/video/7244946821133438235",
    "https://www.tiktok.com/@mujib.m.t/video/7216688120241196314"
]

@app.route('/')
def index():
    videos = []
    for url in urls:
        completed_link = f"https://hello-world-dawn-sunset-aa71.devdesk.workers.dev/?url={url}"
        response = requests.get(completed_link)
        video_src = response.text.strip()
        videos.append({'url': url, 'src': video_src})
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(timeout=600)  # Set a higher timeout value, such as 600 seconds (10 minutes)
