from flask import Flask
import threading
import time

manager = Manager()
manager.start()
manager_thread = threading.Thread(target=manager.run)

app = Flask(__name__)

def process_item(item):
    print(f"Processing item: {item}")
    time.sleep(2)
    print(f"Finished processing item: {item}")

@app.route('/')
def add_item():
    # Recebi item da requisiçao e vou passar como param na linha abaixo
    manager.add_item()
    
    return "Item added!"

if __name__ == '__main__':
    app.run(threaded=True)  # Enable multi-threading (development mode)
 