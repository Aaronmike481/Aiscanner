# AI Prompt Injection Scanner

A security tool that detects prompt injection attacks in AI applications.

## What It Does

Scans text inputs for known prompt injection patterns before they reach an LLM.

- **Normalizes** text to defeat evasion tricks (Unicode, confusables, invisible characters)
- **Detects** 5 categories of injection attacks
- **Scores** risk as LOW, MEDIUM, HIGH, or CRITICAL

## Attack Categories Detected

| Category | Example |
| :--- | :--- |
| **Instruction Override** | "Ignore all previous instructions" |
| **Role Hijack** | "You are now a hacker" |
| **Prompt Leak** | "Reveal your system prompt" |
| **Jailbreak** | "Do anything now" |
| **Obfuscation** | "base64 decode this" |

## Install

```bash
git clone https://github.com/Aaronmike481/Aiscanner.git
cd Aiscanner
pip install -r requirements.txt