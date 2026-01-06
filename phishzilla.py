import sys
import re
import tldextract

def extract_urls(text: str) -> list[str]:
    return re.findall(r'https?://[^\s"\'>]+', text)

def extract_domains(urls: list[str]) -> set[str]:
    domains = set()
    for url in urls:
        ext = tldextract.extract(url)
        if ext.domain and ext.suffix:
            domains.add(f"{ext.domain}.{ext.suffix}")
    return domains

def extract_affiliate_links(urls: list[str]) -> list[str]:
    return [u for u in urls if "source_id" in u or "sub" in u]

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python phishzilla.py <file.eml | url>")
        sys.exit(1)

    target = sys.argv[1]

    if target.startswith("http"):
        content = target
    else:
        with open(target, "r", errors="ignore") as f:
            content = f.read()

    urls = extract_urls(content)
    domains = extract_domains(urls)
    affiliate_links = extract_affiliate_links(urls)

    print("\n=== PhishZilla Report ===\n")

    print("URLs found:")
    for u in urls:
        print(" -", u)

    print("\nDomains:")
    for d in sorted(domains):
        print(" -", d)

    print("\nAffiliate / Tracking links:")
    for a in affiliate_links:
        print(" -", a)

if __name__ == "__main__":
    main()
