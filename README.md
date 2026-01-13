# Task Automation System

Task automation system built with Python and Docker.  
It processes task data from text files, generates automated reports, and logs executions.

## Tech Stack
- Python
- Docker
- Linux

## How to Run
```bash
docker build -t task-automation .
docker run -v $(pwd)/output:/app/output task-automation
