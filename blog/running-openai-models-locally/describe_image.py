# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "ollama",
# ]
# ///

import sys
import ollama

model_name = "rlim-agent"

prompt = """
You are an AI model that describes images in JSON format.
"""

json_schema = {
    "type": "object",
    "properties": {
        "who": {
            "type": "string",
            "description": "Description of the person(s) in the image.",
        },
        "where": {
            "type": "string",
            "description": "Description of the location or setting of the image.",
        },
    },
    "required": ["who", "where"],
}


def describe(image_path):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image_path],
            }
        ],
        format=json_schema,
        stream=False,
    )
    return response["message"]["content"]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python describe_image.py <path_to_image>")
        sys.exit(1)

    image_file = sys.argv[1]
    description_json = describe(image_file)
    print(description_json)
