# PostPilot AI — Django AI Post Generator

A Django-based AI post generation app. The user enters a topic, tone, platform, and image style. Backend AI agents generate a caption, hashtags, image prompt, and optional AI image. After generation, the frontend opens a right-side preview panel similar to an adjacent artifact/preview tab.

## Current MVP Features

- Django-only full-stack project
- User input form for topic, tone, platform, and image style
- AJAX generation flow without page reload
- Backend multi-agent service layer
- Caption Agent
- Hashtag Agent
- Image Agent
- Formatter/Orchestrator Agent
- Gemini support for content/image generation
- GitHub Models support through the OpenAI Python library
- SQLite database for saved generated posts
- Django admin support
- Responsive preview UI

## Tech Stack

- Python
- Django
- SQLite for MVP
- HTML, CSS, JavaScript
- Gemini API
- GitHub Models
- OpenAI Python SDK for OpenAI-compatible agent calls

## Project Structure

```text
automationproject/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── generator/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── services/
│       ├── __init__.py
│       ├── orchestrator.py
│       ├── caption_agent.py
│       ├── hashtag_agent.py
│       ├── image_agent.py
│       ├── formatter_agent.py
│       ├── github_models_client.py
│       └── gemini_client.py
├── templates/
│   ├── base.html
│   └── generator/
│       └── home.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── generator.js
└── media/
    └── generated_images/
```

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/Tirthanand17/automationproject.git
cd automationproject
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

Copy `.env.example` to `.env` and add your keys.

```bash
cp .env.example .env
```

On Windows, you can manually copy the file and rename it to `.env`.

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create admin user

```bash
python manage.py createsuperuser
```

### 7. Run server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Environment Variables

```env
DJANGO_SECRET_KEY=change-this-secret-key
DJANGO_DEBUG=True

AI_PROVIDER=github

GITHUB_TOKEN=your_github_token_here
GITHUB_MODEL_NAME=openai/gpt-4.1
GITHUB_MODELS_BASE_URL=https://models.github.ai/inference

GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_TEXT_MODEL=gemini-2.5-flash
GEMINI_IMAGE_MODEL=gemini-2.5-flash-image-preview
```

## AI Provider Options

Use GitHub Models:

```env
AI_PROVIDER=github
```

Use Gemini:

```env
AI_PROVIDER=gemini
```

If no valid API key is found, the app returns a safe demo response so the frontend flow still works.

## Important Notes

- Do not upload your real `.env` file to GitHub.
- API keys must stay local only.
- For MVP, generated images may fall back to an image prompt/placeholder if the selected model does not return image bytes.
- Real social media posting APIs are intentionally not included in this version.

## Future Improvements

- Real generated image download button
- User login and post history
- Saved favorite posts
- Platform-specific templates
- PostgreSQL production database
- Celery/Redis background task queue
- Docker deployment
- Vercel/Render/Railway deployment guide
