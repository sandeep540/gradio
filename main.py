import time
import gradio as gr
import requests

# The API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Data to be sent
data = {
    "userID": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

#Function to show the GCS File as HyperLink
def gcs_download(uri):
    return f"[Link to CSV File]({uri})"

# Call to external System
def call_data_wizard(text):
    response = requests.post(url, json=data)
    return gcs_download('https://storage.cloud.google.com/<bucket>/<file_name>.csv')

def slow_echo(message, history):
    time.sleep(0.05)
    yield call_data_wizard(message)

demo = gr.ChatInterface(slow_echo, type="messages", title="Data Wizard", chatbot=gr.Chatbot(height=350), textbox=gr.Textbox(placeholder="Provide me an instruction",
                                                                                                                            container=False, scale=7), submit_btn=True, show_progress="full", examples=["Get me list of top 20 Orders"])


if __name__ == "__main__":
    demo.launch()
    
    
    