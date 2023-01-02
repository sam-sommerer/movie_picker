def get_formatted_list_from_string(original_str: str) -> list[str]:
    return [s.strip().lower() for s in original_str.split(", ")]
