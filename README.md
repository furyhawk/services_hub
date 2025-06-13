# Services Hub

A unified API service hub that consolidates multiple weather data services into a single, consistent API interface.

## Overview

Services Hub is a FastAPI-based application that merges multiple OpenAPI specifications into a unified API service. The project currently focuses on weather-related data services, providing endpoints for:

- Air temperature readings across Singapore
- 2-hour weather forecasts
- 24-hour weather forecasts
- 4-day weather outlooks
- Wind direction data
- Lightning observations
- Wet Bulb Globe Temperature (WBGT) observations

The API is generated from OpenAPI specifications and provides a consistent interface for accessing various data services.

## Features

- **Unified API**: Single API interface for multiple data services
- **Auto-generated**: API implementation generated from OpenAPI specs
- **Consistent Interface**: Normalized endpoint design across services
- **Error Handling**: Standardized error responses across all endpoints
- **Pagination Support**: Consistent pagination for all endpoints

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (Python package installer)
- [Podman](https://podman.io/) or Docker (for containerized deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd services_hub
   ```

2. Install dependencies:
   ```bash
   uv pip install -e .
   ```

### Running the API Service

#### Local Development

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000

#### Using Podman

Build and run the service using Podman:

```bash
# Build the container image
podman build -t services-hub .

# Run the container
podman run -p 8000:8000 services-hub
```

#### Using Podman Compose

For multi-container setup with Podman Compose:

```bash
# Run the services defined in docker-compose.yaml
podman-compose up -d

# View logs
podman-compose logs -f

# Stop the services
podman-compose down
```

The API will be available at http://localhost:8000

### API Documentation

Once the server is running, you can access:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI Specification: http://127.0.0.1:8000/openapi.json

## Project Structure

```
services_hub/
│
├── app/                  # Main application code
│   ├── main.py           # FastAPI application entry point
│   ├── models.py         # Pydantic models for requests/responses
│   ├── dependencies.py   # FastAPI dependencies
│   └── routers/          # API endpoint routers
│
├── specs/                # OpenAPI specification files
│   ├── merged-api-spec.json  # Merged OpenAPI specification
│   ├── 24hourWeatherForecast.json
│   ├── 2hourWeatherForecast.json
│   └── ... (other specification files)
│
├── scripts/              # Utility scripts
│   ├── generate-fastapi.sh   # Generate FastAPI code from spec
│   ├── generate-client.sh    # Generate API client
│   └── merge-specs.sh        # Merge multiple API specs
│
├── Dockerfile            # Container definition for the service
├── docker-compose.yaml   # Multi-container setup configuration
├── pyproject.toml        # Project metadata and dependencies
└── README.md             # This file
```

## Development Workflow

### Adding a New Data Service

1. Add the OpenAPI specification file to the `specs/` directory
2. Run the merge script to update the merged specification:
   ```bash
   ./scripts/merge-specs.sh
   ```
3. Generate the FastAPI code:
   ```bash
   ./scripts/generate-fastapi.sh
   ```
4. Implement the endpoint logic in the corresponding router file

### Updating Existing Services

1. Update the corresponding specification file in the `specs/` directory
2. Follow steps 2-4 from "Adding a New Data Service"

## Containerization

The Services Hub supports containerized deployment using either Podman or Docker.

### Container Features

- Uses Python Alpine as the base image for a small footprint
- Leverages `uv` for faster dependency installation
- Includes health checks for container orchestration
- Configurable via environment variables
- Supports volume mounting for development

### Build Options

Both Dockerfile and docker-compose.yaml are provided with configurations that work with either Podman or Docker:

```bash
# Using Podman
podman build -t services-hub:latest .

# Using Docker
docker build -t services-hub:latest .
```

### Environment Variables

The following environment variables can be configured:

- `PYTHONPATH`: Set to `/app` by default
- `PYTHONUNBUFFERED`: Set to `1` for unbuffered output

## License

[Add license information here]

## Contact

[Add contact information here]