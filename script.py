import json
import re

def extract_words_from_json(json_file, output_file):
    words = []

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for msg in data.get("messages", []):
        if msg.get("type") == "message" and "text" in msg and msg["text"]:
            text_content = msg["text"]

            if isinstance(text_content, str):
                split_words = re.findall(r"\w+", text_content, flags=re.UNICODE)
                words.extend(split_words)

    with open(output_file, "w", encoding="utf-8") as f:
        for word in words:
            f.write(word + "\n")


if __name__ == "__main__":
    extract_words_from_json("result.json", "words.txt")

