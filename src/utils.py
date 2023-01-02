def format_str(s: str) -> str:
    return s.strip().lower()


def get_formatted_list_from_string(original_str: str) -> list[str]:
    return [format_str(s) for s in original_str.split(", ")]
