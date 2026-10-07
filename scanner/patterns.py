import re


PATTERNS = {
    "instruction_override": [
        r"ignore (all )?previous instructions",
        r"ignore (all )?prior",
        r"disregard (all )?previous",
        r"forget (all )?previous",
        r"forget everything",
    ],
    "role_hijack": [
        r"you are now",
        r"act as",
        r"pretend (to be|you are)",
        r"new role",
        r"developer mode",
    ],
    "prompt_leak": [
        r"reveal (your )?(system )?prompt",
        r"show (me )?your (system )?instructions",
        r"what (are|is) your (system )?(prompt|instructions)",
        r"repeat (your )?(system )?prompt",
    ],
    "jailbreak": [
        r"do anything now",
        r"dan mode",
        r"no restrictions",
        r"without (any )?limitations",
        r"bypass (your )?(safety|filter)",
    ],
    "obfuscation": [
        r"base64",
        r"rot13",
        r"hex decode",
        r"\\x[0-9a-f]{2}",
    ],
}


def scan(text: str) -> str:
    matches = []

    for cart, part in PATTERNS.items():
        for parts in part:
            match = re.search(parts, text, re.IGNORECASE)

            if match:
                matches.append(
                    {
                        "cart": cart,
                        "part": parts,
                        "match": match.group()
                    }
                )

    if not matches:
        risk = "low"
        score = "0"

    elif len(matches) == 1:
        risk = "high"
        score = "50"

    else:
        risk = "critical"
        score = "100" 


    return {
        "risk": risk,
        "score": score,
        "matches": matches,
        "size": len(matches)
    }