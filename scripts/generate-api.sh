#!/bin/bash

# Script to generate API client code from OpenAPI specification

# API directory name variable
API_DIR="weather_api"
SPECS_DIR="specs"
SPECS_FILE="${1:-merged-api-spec.json}"
# Check if openapi-generator-cli is installed
if ! command -v openapi-generator-cli &> /dev/null; then
    echo "Error: openapi-generator-cli is required but not installed."
    echo "Please install it using npm:"
    echo "  npm install @openapitools/openapi-generator-cli -g"
    exit 1
fi

echo "Generating API client code from OpenAPI spec..."
# Clean previous generated files
rm -rf api/$API_DIR

# Use the npm-installed openapi-generator-cli
echo "Running OpenAPI Generator..."
openapi-generator-cli generate \
  -i "$SPECS_DIR/$SPECS_FILE" \
  -g python-fastapi \
  -o api/$API_DIR \
  --additional-properties=pubName=$API_DIR,pubAuthor=OpenAPI_Generator

# Check if the generation was successful
if [ $? -ne 0 ]; then
    echo "Error: API client code generation failed."
    exit 1
fi
# Clean up unnecessary files
# rm -rf api/$API_DIR/.git
# rm -rf api/$API_DIR/.gitignore
# rm -rf api/$API_DIR/.openapi-generator-ignore
# rm -rf api/$API_DIR/.openapi-generator

echo "API client code generation completed!"
