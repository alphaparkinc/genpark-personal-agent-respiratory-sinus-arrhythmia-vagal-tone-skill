# Respiratory Sinus Arrhythmia RSA & Vagal Tone Copilot Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Continuous heart rate variability (HRV) RMSSD to Respiratory Sinus Arrhythmia (RSA) coupling analyzer, autonomic nervous system stress sentinel, and paced biofeedback breathing pacer. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `evaluate_vagal_tone_index`: Compute parasympathetic vagal tone and stress recovery balance from high-frequency HRV (RMSSD and HF-power) telemetry.
- `generate_paced_resonance_breathing_session`: Synthesize a 5.5 breaths-per-minute heart-rate coherence resonant breathing protocol to stimulate the vagus nerve.

## 🚀 Installation & Usage
Run directly with pure Python standard library:
```bash
python -m genpark_personal_agent_respiratory_sinus_arrhythmia_vagal_tone_skill.server --test
```
