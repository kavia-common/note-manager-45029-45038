# note-manager-45029-45038

Backend: Django + Django REST Framework

Quick start (in container):
- The app is already configured to run for preview. Do not modify preview commands.
- Apply migrations:
  - python manage.py migrate
- (Optional) Seed sample notes:
  - python manage.py seed_notes

Health:
- GET /api/health/ -> {"message": "Server is up!"}

Notes API (JSON):
- Base path: /api/notes/
- List (paginated): GET /api/notes/
- Create: POST /api/notes/ with body:
  {
    "title": "My Note",
    "content": "Optional content"
  }
- Retrieve: GET /api/notes/{id}/
- Update: PUT /api/notes/{id}/
- Partial update: PATCH /api/notes/{id}/
- Delete: DELETE /api/notes/{id}/

Notes model:
- id, title (required), content (optional), created_at (auto), updated_at (auto)

CORS:
- Enabled to allow all origins by default for preview convenience.

API Docs:
- Swagger UI: /docs
- ReDoc: /redoc
- OpenAPI JSON: /swagger.json