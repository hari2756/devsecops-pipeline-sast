import json
import sys

def evaluate_sast(sast_file):
    with open(sast_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    results = data.get("results", [])
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    for finding in results:
        severity = finding.get("extra", {}).get("severity", "INFO").upper()
        if severity in counts:
            counts[severity] += 1
        else:
            counts["INFO"] += 1

    return counts

def evaluate_sca(sca_file):
    with open(sca_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    vuln_count = 0
    for dep in data.get("dependencies", []):
        vuln_count += len(dep.get("vulns", []))

    return vuln_count

if __name__ == "__main__":
    sast_counts = evaluate_sast("semgrep_report.json")
    sca_vulns = evaluate_sca("pip_audit_report.json")

    print("=== DevSecOps Quality Gate Summary ===")
    print(f"SAST Findings -> High/Error: {sast_counts['ERROR']}, Medium/Warning: {sast_counts['WARNING']}, Low/Info: {sast_counts['INFO']}")
    print(f"SCA Dependency CVEs -> {sca_vulns}")

    # Policy Thresholds:
    # 1. Fail if any High/ERROR SAST finding exists
    # 2. Fail if Medium/WARNING SAST findings exceed 2
    # 3. Fail if any third-party CVE is detected
    if sast_counts["ERROR"] > 0 or sast_counts["WARNING"] > 2 or sca_vulns > 0:
        print("\n[BLOCKED] Quality Gate Failed: Security thresholds exceeded.")
        sys.exit(1)

    print("\n[PASSED] Quality Gate Succeeded: Build meets security policy.")
    sys.exit(0)