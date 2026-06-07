# Week 1 — Subfield Map, Candidate Projects & Recommendation

**How to read this report:** Section 1 maps the relevant subfields and how crowded each is. Section 2 gives three candidates; for each, I checked the prior art first, then state the gap, my contribution, feasibility for a remote 3–4 month build, and how it draws on both mentors' strengths. Section 3 recommends one. The screen applied throughout is the lesson from our first conversation: ML must earn its place by producing a capability a cheaper method cannot.

---

## 1. Subfield Map

* **Generative design & ML-assisted topology optimization:** *Heavily worked.* 2025 papers already pair reinforcement learning and physics-informed FEA with topology optimization to output print-ready STLs (one reports ~40% weight reduction), and a 2025–2026 ASME review surveys the whole space, including health/medical clusters. Generic ‘generative design for additive manufacturing’ is not a viable novelty target.
* **Surrogate models for expensive simulation:** *Mature as a general idea.* Defensible only when the underlying simulation is genuinely costly. The opening is not ‘build a surrogate’ but ‘apply one to a specific, expensive design loop nobody has accelerated yet’.
* **Patient-specific / clinical device design:** *Active but with concrete, repeatedly-stated open problems.* The prosthetics literature explicitly notes that an assessment system to predict socket fit before fabrication is still needed, and that digital socket design suffers from clinician-to-clinician inconsistency. These are real, named gaps rather than crowded ground.
* **ML for agriculture / water / remote sensing:** *Saturated.* Multiple 2025 reviews cover ML and digital twins for smart irrigation and arid-region water management, with case studies spanning Central Asia and the Middle East — hard to make novel. Data-efficiency methods are more open but too abstract to carry the tangible, local impact we want to foreground.

---

## 2. Candidate Projects

### Candidate A — Predicting prosthetic socket fit before fabrication (Recommended)

* **Problem & Local Relevance:** A prosthetic socket is the interface between a residual limb and the limb prosthesis; poor fit causes pain, pressure sores, and device abandonment. Designing a good socket digitally still depends heavily on individual clinician skill. Azerbaijan has a real and ongoing population of limb-loss patients from the conflict in and around Karabakh, including landmine injuries, where access to expert prosthetists is limited — so a tool that helps produce a good-fitting socket with less reliance on scarce expertise has direct, pointable impact.
* **Prior Art Found:** CAD/CAM and additive manufacturing of transtibial sockets is established; FEA has been used since the late 1980s to analyze stump–socket interface pressure; 2025 work continues FEA of AM sockets from CT/scan data. Critically, that same literature states plainly that a system to predict appropriate fit in advance of fabrication is still needed, and a 2024 clinical study documents inconsistency between clinicians in digital socket modification.
* **Gap:** FEA can analyze a socket once it exists, but it is slow and expert-driven, and it is run after a design is proposed. There is no fast, learned predictor that takes a residual-limb shape plus a candidate socket design and predicts the resulting interface-pressure map — turning a slow analysis into an instant design-time signal.
* **My Contribution:** Train a surrogate model that predicts stump–socket interface pressure distribution from limb geometry and socket parameters, using FEA-generated data as ground truth. Here the surrogate is justified precisely because FEA is expensive: the learned model converts hours of expert simulation into a real-time fit score a designer can iterate against. Deliver the model plus an open pipeline and validation against held-out FEA cases.
* **Feasibility:** *High.* Limb geometries can be sourced from public anatomical scan data or parametrically generated; FEA (Seymur’s domain) generates the training labels; modeling runs on free GPU. Mostly software.
* **Why this needs both mentors:** Seymur owns the biomechanics, FEA setup, and manufacturability; Elvin owns the surrogate modeling, data pipeline, and training rigor. Neither half is credible alone — which is exactly why it benefits from the pairing.
* **ML earns its place:** *Yes* — it replaces a genuinely expensive, expert-bound FEA loop with an instant predictor.

### Candidate B — Manufacturability-aware generative design for low-cost assistive parts

* **Problem & Local Relevance:** Assistive devices (e.g. hand/finger prostheses, orthotic brackets) are often 3D-printed locally on low-cost FDM printers. Designs optimized purely for strength frequently fail to print well on such hardware, wasting filament and time in exactly the resource-limited settings that most need them.
* **
