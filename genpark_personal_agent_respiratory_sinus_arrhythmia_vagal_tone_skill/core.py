# -*- coding: utf-8 -*-
"""Respiratory Sinus Arrhythmia RSA & Vagal Tone Copilot for GenPark Personal Agent."""
import json
import math
from typing import Dict, Any

class RespiratorySinusArrhythmiaVagalToneCopilot:
    """Parasympathetic vagal nerve tone, HRV RMSSD, and resonance breathing engine."""

    @staticmethod
    def evaluate_vagal_tone_index(rmssd_ms: float, resting_hr_bpm: int, sdnn_ms: float = 50.0, subjective_stress_score_1_to_10: int = 5) -> Dict[str, Any]:
        """Assess autonomic nervous system balance: Sympathetic Overdrive vs. Parasympathetic Coherence."""
        # Log-transformed RMSSD (lnRMSSD) is clinical standard for vagal tone
        ln_rmssd = round(math.log(max(1.0, rmssd_ms)), 2)
        
        if rmssd_ms < 20.0:
            status = "ACUTE_SYMPATHETIC_EXHAUSTION"
            vagal_index = "CRITICALLY_LOW"
        elif rmssd_ms <= 45.0:
            status = "MODERATE_STRESS_STATE"
            vagal_index = "SUB_OPTIMAL"
        elif rmssd_ms <= 80.0:
            status = "BALANCED_PARASYMPATHETIC_HOMEOSTASIS"
            vagal_index = "HEALTHY"
        else:
            status = "HIGH_VAGAL_RECOVERY_EXCELLENT"
            vagal_index = "SUPERIOR"

        return {
            "rmssd_ms": rmssd_ms,
            "ln_rmssd": ln_rmssd,
            "autonomic_state": status,
            "vagal_tone_tier": vagal_index,
            "cardiac_sympathovagal_balance": "PARASYMPATHETIC_DOMINANT" if rmssd_ms >= 45.0 else "SYMPATHETIC_STRESSED",
            "recovery_recommendation": "Engage 10-minute 5.5 bpm resonant breathing pacer to upregulate baroreflex sensitivity." if rmssd_ms < 45.0 else "Maintain current restorative physical state."
        }

    @staticmethod
    def generate_paced_resonance_breathing_session(session_duration_minutes: int, target_vagal_boost_pct: float = 25.0) -> Dict[str, Any]:
        """Synthesize 0.1 Hz resonant frequency breathing protocol (4.5s Inhale / 5.5s Exhale)."""
        cycles_per_minute = 6.0
        total_breaths = int(session_duration_minutes * cycles_per_minute)

        return {
            "protocol_name": "0.1 Hz Resonant Baroreflex Coherence Protocol",
            "session_duration_minutes": session_duration_minutes,
            "breath_timing": {
                "inhale_seconds": 4.5,
                "hold_at_top_seconds": 0.0,
                "exhale_seconds": 5.5,
                "hold_at_bottom_seconds": 0.0
            },
            "total_breathing_cycles": total_breaths,
            "physiological_impact": [
                "Maximal heart rate oscillations synchronize with respiratory frequency.",
                "Blood pressure Mayer waves lock in phase with vagus nerve efferent activity.",
                "Downregulates amygdala arousal and lowers systemic salivary cortisol."
            ]
        }
