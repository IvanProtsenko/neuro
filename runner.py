# Import the necessary modules
from os import path
import shutil

from ultralytics import YOLO
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

# Load the trained model
model = YOLO("best.pt")  # replace "yolov8m.pt" with the path to your trained model


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_POST(self):
        content_len = int(self.headers['content-length'])
        img_dir = self.rfile.read(content_len).decode('utf-8')
        img_dir = img_dir.split("\"")[1]
        print(img_dir)
        img_out_dir = img_dir[0:-len(img_dir.split(".")[-1]) - 1] + "_out.jpg"

        results = model.predict(source=img_dir, save=True, save_txt=True, project="./RESULT/", name="result", exist_ok=True)
        print(results[0].path)

        shutil.copyfile("./RESULT/result/" + img_dir.split("/")[-1], img_out_dir)

        if path.exists("./RESULT/result/labels/" + img_dir.split("/")[-1].split(".")[0] + ".txt"):
            img_out_dir_txt = img_dir[0:-len(img_dir.split(".")[-1]) - 1] + "_out_defects.txt"
            shutil.copyfile("./RESULT/result/labels/" + img_dir.split("/")[-1].split(".")[0] + ".txt", img_out_dir_txt)

        self.send_response(200)
        self.end_headers()
        return


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


run()