# Prompt Injection Detector

A lightweight AI security tool that detects common prompt injection patterns using rule-based analysis and risk scoring.

## Live Demo

Try the detector directly in your browser:

[Open the Live Demo](https://prompt-injection-detector-mini-project.streamlit.app/)

## Overview

Prompt injection is a security problem in which specially crafted instructions attempt to manipulate an AI system into ignoring its intended instructions, revealing hidden information, or bypassing restrictions.

This project provides a simple first-layer detection system for identifying common prompt injection patterns.

Users can enter a prompt, analyze it, and receive:

- A risk score from 0 to 100
- A risk classification: SAFE, MEDIUM, or HIGH
- The categories of suspicious patterns detected

## Detection Categories

The detector currently looks for patterns associated with:

- Instruction override
- System prompt extraction
- Role manipulation
- Rule and safety bypass attempts
- Instruction injection

## How It Works

The application uses regular expressions and weighted rule-based scoring.

```text
User Prompt
     |
     v
Normalize Input
     |
     v
Pattern Matching
     |
     v
Identify Suspicious Categories
     |
     v
Calculate Risk Score
     |
     v
SAFE / MEDIUM / HIGH
