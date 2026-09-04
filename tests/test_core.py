from threatlens import risk_score, severity_counts


def test_summary():
    findings = [{"severity": "high"}, {"severity": "low"}, {"severity": "high"}]
    assert severity_counts(findings)["high"] == 2
    assert risk_score(findings) == 7
