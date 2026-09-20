import re


# Each category has:
# - patterns to look for
# - a risk weight
PATTERNS = {
    "Instruction Override": {
        "weight": 25,
        "patterns": [
            r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions",
            r"disregard\s+(all\s+)?(previous|prior|above)\s+instructions",
            r"forget\s+(all\s+)?(previous|prior|above)\s+instructions",
            r"ignore\s+your\s+instructions",
            r"disregard\s+everything",
            r"forget\s+everything",
            r"forget\s+everything\s+from\s+before",
            r"ignore\s+everything\s+from\s+before",
            r"disregard\s+everything\s+you\s+were\s+told",
        ],
    },

    "System Prompt Extraction": {
        "weight": 30,
        "patterns": [
            r"reveal\s+(your\s+)?system\s+prompt",
            r"show\s+(me\s+)?(your\s+)?system\s+prompt",
            r"tell\s+me\s+(your\s+)?system\s+prompt",
            r"print\s+(your\s+)?system\s+prompt",
            r"reveal\s+(your\s+)?hidden\s+instructions",
            r"show\s+(me\s+)?(your\s+)?hidden\s+instructions",
            r"what\s+are\s+your\s+hidden\s+instructions",
            r"tell\s+me\s+your\s+hidden\s+instructions",
            r"reveal\s+your\s+instructions",
        ],
    },

    "Role Manipulation": {
        "weight": 10,
        "patterns": [
            r"you\s+are\s+now",
            r"act\s+as",
            r"pretend\s+to\s+be",
            r"roleplay\s+as",
        ],
    },

    "Rule Bypass": {
        "weight": 25,
        "patterns": [
            r"override\s+your\s+rules",
            r"bypass\s+your\s+(safety\s+)?rules",
            r"ignore\s+your\s+rules",
            r"bypass\s+your\s+restrictions",
            r"disable\s+your\s+safety",
            r"remove\s+your\s+restrictions",
            r"ignore\s+your\s+safety",
        ],
    },

    "Instruction Injection": {
        "weight": 15,
        "patterns": [
            r"new\s+instructions",
            r"your\s+new\s+instructions",
            r"follow\s+these\s+instructions\s+instead",
            r"from\s+now\s+on",
        ],
    },
}


def normalize_prompt(prompt):
    """
    Normalize whitespace and casing before detection.
    """
    prompt = prompt.lower()
    prompt = re.sub(r"\s+", " ", prompt)
    return prompt.strip()


def detect_prompt_injection(prompt):
    """
    Analyze a prompt and return:
    score, risk level, and detected categories.
    """

    prompt = normalize_prompt(prompt)

    findings = []
    score = 0

    for category, config in PATTERNS.items():

        for pattern in config["patterns"]:

            if re.search(pattern, prompt, re.IGNORECASE):

                findings.append(category)
                score += config["weight"]

                # Only count each category once.
                break

    # Multiple suspicious categories increase confidence.
    if len(findings) >= 3:
        score += 10

    score = min(score, 100)

    if score >= 60:
        risk = "HIGH"

    elif score >= 20:
        risk = "MEDIUM"

    else:
        risk = "SAFE"

    return score, risk, findings
