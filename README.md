# Translation API

This project provides a REST API for translating text using the Google Translate service. It allows users to translate words, phrases, and paragraphs between different languages.

## Setup Instructions

To set up the project, follow the instructions below:

### Prerequisites

- Python 3.7 or higher installed on your machine
- Pip package manager

### Installation

1. Clone the repository to your local machine:

```shell
git clone https://github.com/ParthGupta-HL/Assignment.git
```

2. Activate the virtual environment:

```shell
source django_env/bin/activate
```

3. Install the project dependencies using pip:

```shell
pip install -r requirements.txt
```

4. Navigate to the project directory:

```shell
cd translation-api
```

5. Configure the settings:

   - Open the `translation/settings.py` file and update the database settings if necessary.
   - You can also modify other settings such as cache settings, logging, etc., if needed.

6. Apply database migrations:

```shell
python manage.py migrate
```

7. Run the development server:

```shell
python manage.py runserver
```

The server should now be running locally at `http://127.0.0.1:8000/`.

## Usage

To use the Translation API, you can make requests to the `/translate/` endpoint with the required parameters:

- `source_language`: The source language code (e.g., "en" for English)
- `target_language`: The target language code (e.g., "hi" for Hindi)
- `text`: The text to be translated

Example request:

```shell
GET /translate/?source_language=en&target_language=hi&text=Hello
```

Example response:

```json
{
  "translation": "नमस्ते"
}
```

## Testing

To run the test cases for the Translation API, make sure you are in the project root directory and run the following command:

```shell
python manage.py test translator.tests
```

This will execute the test cases and display the results in the terminal.

## Bonus

This app stores the responses in Django cache memory. If a user requests already translated data, it is served from cache.
