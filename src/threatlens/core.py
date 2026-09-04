SEVERITIES = {"critical": 4, "high": 3, "medium": 2, "low": 1, "info": 0}


def severity_counts(findings):
    counts = {level: 0 for level in SEVERITIES}
    for finding in findings:
        level = str(finding.get("severity", "info")).lower()
        counts[level if level in counts else "info"] += 1
    return counts


def risk_score(findings):
    return sum(SEVERITIES.get(str(f.get("severity", "info")).lower(), 0) for f in findings)
