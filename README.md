# 🚑 CIVIC-RESCUE: Urban Crisis Triage & AI Dispatch

[![Hugging Face Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)](YOUR_SPACE_URL_HERE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**CIVIC-RESCUE** is a high-fidelity environment designed to evaluate Agentic AI in high-stakes, resource-constrained environments. Unlike static benchmarks, CIVIC-RESCUE simulates **dynamic risk escalation**, where unaddressed emergencies compound in severity over time, testing an agent's ability to prioritize long-term stability over short-term gains.

---

## 🚀 Key Features

* **Dynamic Severity Engine**: Incidents evolve. A "Small Fire" left unmanaged for 3 steps escalates into a "Structural Conflagration," doubling the risk score.
* **Spatial Awareness**: Agents must manage a 10x10 urban grid, optimizing travel time and resource distribution.
* **Pydantic V2 Architecture**: Full type-safety for observation and action spaces, ensuring seamless integration with LLMs (GPT-4o, Claude 3.5, Llama 3).
* **Real-Time Command Center**: A production-grade Streamlit dashboard featuring live heatmaps and decision-logic logs.

---

## 🧠 Technical Framework

### Observation Space
The environment provides a structured `EmergencyObservation` object:
* `incidents`: A list of active `Incident` objects (ID, Type, Location, Severity).
* `resources`: Current availability of Fire, Medical, and Police units.

### Reward Function
The agent's performance is measured by the **Risk Mitigation Efficiency (RME)**:
$$R_t = \sum_{i \in I} (S_{i,t-1} - S_{i,t}) - \beta \cdot U_t$$

Where:
* $S$: Severity of incident $i$.
* $U_t$: Penalty for unauthorized or redundant resource dispatch.
* $\beta$: Scaling factor for resource conservation.

---

## 🛠️ Installation & Local Development

1. **Clone the repository:**
   ```zsh
   git clone [https://huggingface.co/spaces/YOUR_USER/YOUR_SPACE](https://huggingface.co/spaces/YOUR_USER/YOUR_SPACE)
   cd openenv-aics







