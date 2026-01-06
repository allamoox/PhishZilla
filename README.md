# PhishZilla

**PhishZilla** is an open-source phishing analysis & abuse-report generator built for security analysts.

It helps analysts quickly extract indicators of compromise (IOCs), identify affiliate abuse, and generate ready-to-use abuse report data from phishing emails or URLs.

---

## ✨ Features

- 📧 Analyze phishing `.eml` email files
- 🌐 Analyze suspicious URLs directly
- 🔗 Extract all embedded URLs
- 🏷️ Identify affiliate & tracking parameters (e.g. `source_id`, `sub*`)
- 🧠 Extract domains for IOC reporting
- 📝 Generate analyst-friendly output for abuse reporting

---

## 🚀 Usage

### Analyze a phishing email
python phishzilla.py sample.eml

**Analyze a URL**
python phishzilla.py https://example.com/phish

**📊 Example Output**


**=== PhishZilla Report ===**
URLs found:
 - https://proteingram.info/?source_id=20024&sub1=...

Domains:
 - proteingram.info
 - totaldrive.com

Affiliate / Tracking links:
 - https://www.upoert.com/cmp/223GDT1/...

**🛡️ Use Cases**

SOC phishing triage

Threat intelligence enrichment

Affiliate fraud investigation

Abuse reporting (Google Safe Browsing, Microsoft, Cloudflare, vendors)

**⚠️ Disclaimer**

PhishZilla is intended for defensive security and research purposes only.
Do not use it for unauthorized, deceptive, or malicious activity.

**📄 License**
MIT License
