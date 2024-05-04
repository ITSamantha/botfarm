#!/bin/bash

alembic revision --autogenerate

alembic upgrade head

PYTHONPATH=/app python src/database/seeders/database_seeder.py

# PYTHONPATH=/app pytest tests/tests.py

uvicorn src.main:app --host 0.0.0.0 --port 800 0