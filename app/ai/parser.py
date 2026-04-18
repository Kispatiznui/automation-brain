def parse_command(text: str):
    text = text.lower()

    if "descargas" in text:
        return {
            "action": "clean_downloads",
            "params": {
                "sort": "type",
                "remove_duplicates": True
            }
        }

    return {
        "action": "unknown",
        "params": {}
    }
