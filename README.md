# SRAC Malware Analysis Report

## Executive Summary

This repository contains analysis and documentation of a sophisticated information stealer malware dubbed "SRAC" (from the original filename "srac.py"). Unlike typical Discord token grabbers that utilize Discord webhooks for exfiltration, this variant employs a custom command and control (C2) server architecture, making it more difficult to detect and block.

The malware was discovered during security research and has been analyzed to understand its capabilities, infection methods, and potential mitigations.

## ⚠️ WARNING

**This repository contains information about malicious software for EDUCATIONAL PURPOSES ONLY.**

- Do not download, compile, or run any suspicious code
- The analysis is provided to help security professionals understand the threat
- The techniques described are actively harmful and illegal when deployed

## Malware Capabilities

SRAC is an advanced information stealer targeting:

### Browser Data Extraction
- **Credentials**: Harvests saved passwords from multiple browsers
- **Cookies**: Extracts browser cookies enabling session hijacking
- **Autofill Data**: Captures stored form data including personal information
- **Affected Browsers**: Chrome, Edge, Opera, Brave, Firefox, and derivatives

### Cryptocurrency Targeting
- **Wallet Access**: Targets multiple cryptocurrency wallets
  - Metamask, Exodus, Atomic, Electrum, and numerous others
- **Injection Mechanism**: Deploys malicious code into legitimate wallet applications
- **Extension Targeting**: Specifically hunts for browser extensions related to cryptocurrency

### Discord Account Compromise
- **Token Extraction**: Retrieves authentication tokens from:
  - Main Discord client
  - Discord PTB (Public Test Build)
  - Discord Canary
  - Multiple user profiles

### File System Reconnaissance
- **Sensitive Document Search**: Scans key directories (Desktop, Documents, Downloads)
- **Keyword Targeting**: Hunts for files containing terms like:
  - "password", "wallet", "crypto", "bank", "secret", "backup", "recovery"

## Technical Analysis

### Infection Process
1. Installation of required Python dependencies
2. Process termination of targeted browsers to unlock data files
3. Utilization of Windows cryptography APIs for credential decryption
4. Systematic extraction of targeted data
5. Compression of stolen information into archive files
6. Exfiltration to C2 server at "dieserbenni[.]ru"

### Novel Threat Aspects
Unlike conventional Discord malware that uses webhook-based exfiltration (which can be relatively easily blocked), SRAC implements:

- **Custom C2 Architecture**: Direct communication with attacker-controlled server
- **Weak Security Implementation**: No rate limiting or other protections on the server side
- **Vulnerability to Analysis**: The server infrastructure shows significant security flaws

## Detection & Mitigation

### Indicators of Compromise (IoCs)
- Script filename: `srac.py`
- C2 domain: `dieserbenni[.]ru`
- Temporary files created in user directories
- Unexpected Python library installations

### Recommended Security Measures
- Keep operating systems and browsers updated
- Use hardware security keys for critical accounts where possible
- Enable two-factor authentication for all important services
- Regularly audit installed applications and browser extensions
- Monitor for unexpected network connections
- Consider using dedicated devices for cryptocurrency management

## Research Methodology

This analysis was conducted in a controlled environment with proper isolation measures. The researcher identified the malware's attack vectors and C2 infrastructure without executing the malicious payload.

Upon discovering the poorly secured C2 server, the researcher conducted a legal and responsible stress test demonstrating the vulnerability of the infrastructure (see [video demonstration](https://streamable.com/zb56i4)).

## Contributing to Security Knowledge

If you have additional information about this threat or have discovered variants, please follow responsible disclosure practices:

1. Do not share or distribute malicious code
2. Document your findings with proper operational security
3. Report the malware to relevant security platforms and authorities
4. Consider informing affected service providers (Discord, browser vendors, etc.)

## Legal Disclaimer

This research is provided for educational and defensive purposes only. The techniques described should only be used in accordance with all applicable laws and regulations, including computer fraud and abuse legislation. The authors do not condone or support malicious use of the information provided.

---

*Last updated: April 24, 2025*
