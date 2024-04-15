### WhatsApp Webhook Analytics

Handling and processing Incoming webhook request configured at Glific.

## Installation

### Prerequisite
1. pyenv
2. python 3.12

### Steps
1. Clone the repository
    ```sh
    git clone https://github.com/DostEducation/whatsapp-webhook-analytics.git
    ```
2. Switch to project folder and setup the vertual environment
    ```sh
    cd whatsapp-webhook-analytics
    python -m venv venv
    ```
3. Activate the virtual environment
    ```sh
    source ./venv/bin/activate
    ```
4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Set up your .env file by copying .env.example
    ```sh
    cp .env.example .env
    ```
6. Add/update variables in your `.env` file for your environment.
7. Run the following command to get started with pre-commit
    ```sh
    pre-commit install
    ```
8. Start the server by following command
    ```sh
    functions_framework --target=handle_payload --debug
    ```
