from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Fetch details about the environment
    pod_name = os.getenv('HOSTNAME', socket.gethostname())
    
    # HTML styling for a nice demo look
    html_content = f"""
    <div style="font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h1 style="color: #2c3e50;">🚀 Ephemeral Environment is Live! test2</h1>
        <p>This is a dynamic preview generated automatically this is updated to test.but there is a problem summa</p>
        <br>
        <div style="background: #ecf0f1; display: inline-block; padding: 20px; border-radius: 10px;">
            <p><strong>Container ID / Pod:</strong> {pod_name}</p>
            <p><strong>Status:</strong> <span style="color: green;">Running</span></p>
        </div>
    </div>
    """
    return html_content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)