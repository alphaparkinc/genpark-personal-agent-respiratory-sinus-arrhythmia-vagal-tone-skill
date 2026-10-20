# -*- coding: utf-8 -*-
"""MCP Server for Respiratory Sinus Arrhythmia RSA & Vagal Tone Copilot Skill."""
import sys
import json
import logging
from typing import Dict, Any

from .core import RespiratorySinusArrhythmiaVagalToneCopilot

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TOOLS_SCHEMA = [
    {
        "name": "evaluate_vagal_tone_index",
        "description": "Compute parasympathetic vagal tone and stress recovery balance from high-frequency HRV (RMSSD and HF-power) telemetry.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "rmssd_ms": {
                    "type": "number",
                    "description": "Root mean square of successive differences in ms"
                },
                "resting_hr_bpm": {
                    "type": "integer"
                },
                "sdnn_ms": {
                    "type": "number"
                },
                "subjective_stress_score_1_to_10": {
                    "type": "integer"
                }
            },
            "required": [
                "rmssd_ms",
                "resting_hr_bpm"
            ]
        }
    },
    {
        "name": "generate_paced_resonance_breathing_session",
        "description": "Synthesize a 5.5 breaths-per-minute heart-rate coherence resonant breathing protocol to stimulate the vagus nerve.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "session_duration_minutes": {
                    "type": "integer"
                },
                "target_vagal_boost_pct": {
                    "type": "number"
                }
            },
            "required": [
                "session_duration_minutes"
            ]
        }
    }
]

def handle_rpc(line: str) -> str:
    try:
        req = json.loads(line)
        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-respiratory-sinus-arrhythmia-vagal-tone-skill", "version": "1.0.0"}
            }
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": res})

        elif method == "tools/list":
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS_SCHEMA}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            target_func = getattr(RespiratorySinusArrhythmiaVagalToneCopilot, tool_name, None)
            if not target_func:
                return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {tool_name}"}})

            result = target_func(**args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result, indent=2)}]
                }
            })

        else:
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {method}"}})

    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": req.get("id") if "req" in locals() else None, "error": {"code": -32000, "message": str(e)}})

def run_test():
    print("[TEST] Running internal RPC self-test for genpark-personal-agent-respiratory-sinus-arrhythmia-vagal-tone-skill...")
    init_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    init_res = json.loads(handle_rpc(init_req))
    assert init_res.get("result", {}).get("serverInfo", {}).get("name") == "genpark-personal-agent-respiratory-sinus-arrhythmia-vagal-tone-skill"

    list_req = json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    list_res = json.loads(handle_rpc(list_req))
    assert len(list_res.get("result", {}).get("tools", [])) == 2
    print(f"[TEST] SUCCESS: {len(list_res['result']['tools'])} tools verified.")
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        if run_test():
            sys.exit(0)
        sys.exit(1)

    for line in sys.stdin:
        if not line.strip():
            continue
        out = handle_rpc(line)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()
