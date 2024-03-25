import re

# Compiled pattern for reuse, improves performance
STATIC_PATH_PATTERN = re.compile(r'\.\./static/([a-zA-Z0-9_\-./]+)')


def transform_path_to_django_static(original_path):
    """Transforms a relative static path to Django's static tag format.

    Parameters:
        original_path (str): The original path to be transformed.

    Returns:
        str: The transformed path wrapped in Django's static tag format.
    """
    print(f"Transforming path: {original_path}")  # Log the original path
    trimmed_path = original_path.replace('../static/', '')
    transformed_path = f"{{% static '{trimmed_path}' %}}"
    print(f"Transformed path: {transformed_path}")  # Log the transformed path
    return transformed_path


def add_static_tag_at_start(content):
    """Ensures the '{% load static %}' tag is at the beginning of the content.

    Parameters:
        content (str): The original content of the file.

    Returns:
        str: The modified content with the static tag at the beginning, if it was missing.
    """
    static_tag = "{% load static %}"
    if static_tag not in content:
        content = f"{static_tag}{content}"
        print("Static tag added at the beginning.")  # Log addition of static tag
    else:
        print("Static tag already present at the beginning.")  # Log presence of static tag
    return content


def process_html_content(content):
    """Processes HTML content, adding necessary Django static tags and transforming paths.

    Parameters:
        content (str): The original HTML content.

    Returns:
        str: The processed HTML content with transformed paths.
    """
    print("Processing HTML content...")  # Log the beginning of content processing
    content = add_static_tag_at_start(content)
    content = STATIC_PATH_PATTERN.sub(lambda match: transform_path_to_django_static(f'../static/{match.group(1)}'),
                                      content)
    print("HTML content processed.")  # Log the completion of content processing
    return content


def process_html_file(file_path):
    """Reads, processes, and writes back an HTML file for Django static file handling.

    Parameters:
        file_path (str): Path to the HTML file to process.
    """
    print(f"Processing file: {file_path}")  # Log the file being processed
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        content = process_html_content(content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File processed and saved: {file_path}")  # Log the successful processing and saving
    except FileNotFoundError:
        print(f"File not found: {file_path}")  # Log file not found error
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")  # Log other errors


# Example usage
file_path = 'river_admin/templates/index.html'
process_html_file(file_path)
