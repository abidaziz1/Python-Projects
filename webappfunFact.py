import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def setup_ui():
    # Function to setup the UI with heading and button.
    put_html("""
    <p align="center">
        <h2>
            <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%">
            Fun Fact Generator
        </h2>
    </p>
    """)
    put_buttons(
        [dict(label="Click me", value="outline-success", color="outline-success")],
        onclick=get_fun_fact
    )

def get_fun_fact(_):
    """Function to fetch and display a fun fact."""
    clear() # clear everything from the get request page
    setup_ui()

    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        # Use GET request
        response = requests.get(url, timeout=5)

        # Check if the response was successful
        response.raise_for_status()

        # Load the request in json file
        data = response.json()

        # Extracts the fact text from the response.
        useless_fact = data.get("text", "Failed to fetch fact!")

        # Put the facts in the green color
        style(put_text(useless_fact), 'color:blue; font-size: 30px')

    except requests.RequestException as e:
        put_text("Error fetching fact:", e, color="red")

if __name__ == '__main__':
    setup_ui()
    hold()  # keeps the session active to allow continuous interaction.