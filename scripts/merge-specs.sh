#!/bin/bash
# This script merges multiple OpenAPI specification files into a single file

set -e

# Directory settings
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPECS_DIR="$(realpath "${SCRIPT_DIR}/../specs")"
OUTPUT_DIR="$(realpath "${SCRIPT_DIR}/../specs")"
OUTPUT_FILE="${OUTPUT_DIR}/merged-api-spec.json"

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed."
    echo "Please install jq using your package manager, e.g.:"
    echo "  apt-get install jq or brew install jq"
    exit 1
fi

echo "Merging OpenAPI specs from ${SPECS_DIR}..."

# Initialize merged spec with first file
FIRST_FILE=$(ls "${SPECS_DIR}"/*.json | head -n 1)
cp "${FIRST_FILE}" "${OUTPUT_FILE}"

# Get base paths, info, and servers from first file
BASE_PATHS=$(jq '.paths' "${OUTPUT_FILE}")
BASE_INFO=$(jq '.info' "${OUTPUT_FILE}")
BASE_SERVERS=$(jq '.servers' "${OUTPUT_FILE}")
BASE_COMPONENTS=$(jq '.components // {}' "${OUTPUT_FILE}")

# Process each remaining spec file
for spec_file in "${SPECS_DIR}"/*.json; do
    # Skip the output file if it already exists and the first file
    if [[ "${spec_file}" == "${OUTPUT_FILE}" ]] || [[ "${spec_file}" == "${FIRST_FILE}" ]]; then
        continue
    fi
    
    echo "Processing ${spec_file}..."
    
    # Extract paths from the current spec file
    CURRENT_PATHS=$(jq '.paths' "${spec_file}")
    
    # Extract components from the current spec file
    CURRENT_COMPONENTS=$(jq '.components // {}' "${spec_file}")
    
    # Merge paths (taking the file name as a tag prefix for operations)
    BASE_PATHS=$(jq -s '.[0] * .[1]' <(echo "${BASE_PATHS}") <(echo "${CURRENT_PATHS}"))
    
    # Merge components (schemas, parameters, responses, etc.)
    BASE_COMPONENTS=$(jq -s '.[0] * .[1]' <(echo "${BASE_COMPONENTS}") <(echo "${CURRENT_COMPONENTS}"))
done

# Update the merged spec file with the combined paths and components
jq --argjson paths "${BASE_PATHS}" --argjson components "${BASE_COMPONENTS}" \
   '.paths = $paths | .components = $components' "${OUTPUT_FILE}" > "${OUTPUT_FILE}.tmp"
mv "${OUTPUT_FILE}.tmp" "${OUTPUT_FILE}"

# Update title and description in the merged spec
MERGED_TITLE="Merged API Services"
MERGED_DESCRIPTION="This is a merged OpenAPI specification containing multiple API services"
MERGED_VERSION=$(date +"%Y.%m.%d")

jq --arg title "${MERGED_TITLE}" --arg desc "${MERGED_DESCRIPTION}" --arg ver "${MERGED_VERSION}" \
   '.info.title = $title | .info.description = $desc | .info.version = $ver' "${OUTPUT_FILE}" > "${OUTPUT_FILE}.tmp"
mv "${OUTPUT_FILE}.tmp" "${OUTPUT_FILE}"

echo "OpenAPI specs successfully merged into ${OUTPUT_FILE}"
echo "Merged spec contains $(jq '.paths | keys | length' "${OUTPUT_FILE}") endpoints"
echo "Merged spec contains $(jq '.components.schemas | keys | length // 0' "${OUTPUT_FILE}") schema definitions"