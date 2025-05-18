#!/usr/bin/env python
"""
Script to fix FastAPI Annotated parameter issue
This modifies the API files to fix the issue where Annotated and default values conflict
"""
import os
import re
import glob

def fix_annotated_parameters(file_path):
    """
    Fix the FastAPI parameter issue by replacing problematic Annotated syntax
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Pattern that matches parameters with both Annotated and default Query
        # Example: var_date: Annotated[Optional[StrictStr], Field(description="...")] = Query(None, description="...", alias="date")
        pattern = r'(\w+): Annotated\[(Optional\[)?([^]]+)(\])?, Field\(([^)]*)\)\] = Query\(([^,]+)(,.*?)\)'
        
        # Replace with a version that only uses Query with combined parameters
        # Copy the description from Field to Query if it exists
        def replace_func(match):
            var_name = match.group(1)
            optional = match.group(2) or ""
            type_name = match.group(3)
            optional_close = match.group(4) or ""
            field_params = match.group(5)
            query_value = match.group(6)
            query_params = match.group(7) or ""
            
            # Extract description from Field if present
            field_desc = ""
            if "description=" in field_params:
                import re
                desc_match = re.search(r'description="([^"]*)"', field_params)
                if desc_match:
                    field_desc = desc_match.group(1)
            
            # If Query already has a description, don't add the one from Field
            if field_desc and "description=" not in query_params:
                query_params = query_params + f', description="{field_desc}"'
            
            return f'{var_name}: {optional}{type_name}{optional_close} = Query({query_value}{query_params})'
        
        modified_content = re.sub(pattern, replace_func, content)
        
        if modified_content != content:
            with open(file_path, 'w') as file:
                file.write(modified_content)
            print(f"Fixed annotated parameters in {file_path}")
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def main():
    # Look in both Docker path and local path
    api_paths = [
        '/usr/src/app/src/openapi_server/apis/**/*.py',  # Docker path
        './src/openapi_server/apis/**/*.py',            # Local path relative to script
        '../src/openapi_server/apis/**/*.py',           # Another possible local path
    ]
    
    fixed_count = 0
    for path_pattern in api_paths:
        api_files = glob.glob(path_pattern, recursive=True)
        for file_path in api_files:
            if os.path.exists(file_path) and fix_annotated_parameters(file_path):
                fixed_count += 1
    
    print(f"Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
