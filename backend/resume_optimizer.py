import re

MILITARY_TO_CORPORATE = {
    "sepoy": "Team Associate",
    "havildar": "Senior Team Member",
    "commanding officer": "Operations Manager",
    "unit": "Department",
    "mission": "Project",
    "operation": "Business Operation",
    "served": "Worked"
}

def optimize_resume(resume_text: str) -> str:
    optimized = resume_text.lower()

    for military, corporate in MILITARY_TO_CORPORATE.items():
        optimized = re.sub(
            rf"\b{military}\b",
            corporate,
            optimized,
            flags=re.IGNORECASE
        )

    optimized = optimized.replace(" i ", " I ")
    return optimized.strip()
