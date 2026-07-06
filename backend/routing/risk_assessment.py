"""
Risk Assessment Module

Detects maternal red-flag symptoms before routing.

Returns

high
medium
low
"""

HIGH_RISK_KEYWORDS = {

    "bleeding",
    "heavy bleeding",
    "blood",

    "difficulty breathing",
    "can't breathe",
    "cannot breathe",
    "shortness of breath",

    "severe headache",

    "vision changes",
    "blurred vision",

    "seizure",

    "chest pain",

    "fainted",
    "unconscious",

    "reduced fetal movement",

    "no fetal movement",

    "water broke",

    "labour",

    "labor",

    "severe abdominal pain",

    "high fever",

}


MEDIUM_RISK_KEYWORDS = {

    "vomiting",

    "back pain",

    "swelling",

    "fever",

    "pain",

    "cramps",

    "dizziness",

    "headache",

}


def assess_risk(
    query: str,
):
    """
    Assess maternal risk.

    Returns

    high
    medium
    low
    """

    q = query.lower()

    for word in HIGH_RISK_KEYWORDS:

        if word in q:

            return {
                "risk": "high",
                "reason": word,
            }

    for word in MEDIUM_RISK_KEYWORDS:

        if word in q:

            return {
                "risk": "medium",
                "reason": word,
            }

    return {
        "risk": "low",
        "reason": None,
    }