#! /usr/bin/env bash

set -e
set -x

spec_file="${1:-specs/merged-api-spec.json}"

echo "Processing $spec_file..."
fastapi-codegen --input $spec_file --output app --output-model-type pydantic_v2.BaseModel
