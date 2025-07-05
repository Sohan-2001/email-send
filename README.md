# Email Sending API

This project provides a simple FastAPI-based API for sending emails.

## Features
- Send emails with subject, body, and recipient
- Optional attachments support
- Configuration via environment variables

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your email server settings (see below).
3. Run the API:
   ```sh
   uvicorn main:app --reload
   ```

## Environment Variables
Create a `.env` file in the project root with the following:

```
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USER=your@email.com
EMAIL_PASSWORD=yourpassword
EMAIL_FROM=your@email.com
```

## API Usage
- POST `/send-email` with JSON body:
  ```json
  {
    "to": "recipient@email.com",
    "subject": "Test Email",
    "body": "Hello, this is a test email."
  }
  ```

## License
MIT
