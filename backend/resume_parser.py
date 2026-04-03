def parse_resume(resume_text: str) -> dict:
    sections = {
        "summary": "",
        "skills": [],
        "experience": []
    }

    lines = resume_text.split("\n")

    for line in lines:
        lower = line.lower()

        if "skill" in lower:
            sections["skills"].append(line)

        elif any(word in lower for word in ["mission", "operation", "unit", "served"]):
            sections["experience"].append(line)

        else:
            sections["summary"] += line + " "

    return sections
