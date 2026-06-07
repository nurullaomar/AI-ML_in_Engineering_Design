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
* **Prior Art Found:** Generative design and topology optimization that output print-ready parts are well covered, including RL- and FEA-guided 2025 frameworks and ASME reviews. Manufacturability is usually treated via generic constraints (overhang angle, minimum feature size) rather than the real behavior of a specific low-cost printer.
* **Gap:** Optimizing assistive-part geometry against an empirically-learned model of a specific low-cost FDM printer’s failure modes — not idealized rules — is underexplored.
* **My Contribution:** Learn a printability model from print outcomes on an accessible FDM machine, then fold it into a design loop so generated parts are both structurally sound and reliably printable on low-cost hardware. Validate by print-success rate vs. a strength-only baseline.
* **Feasibility:** *Medium.* Needs some real printing for printability data (modest hardware), plus simulation and ML — heavier logistics than A.
* **Mentor Fit & ML Justification:** Seymur (DFM, additive manufacturing); Elvin (the learned printability model). ML is justified because a printer’s real failure behavior is not closed-form and must be learned.

### Candidate C — Surrogate-accelerated design of compliant assistive mechanisms

* **Problem & Local Relevance:** Compliant mechanisms (single-piece flexible structures) make cheap, robust assistive devices — prosthetic fingers, adaptive grippers — because they have no assembled joints to fail. Designing them requires repeated nonlinear FEA, which is slow and expert-bound.
* **Prior Art Found:** Compliant mechanism design and topology optimization are established; ML surrogates for FEA exist generally. Most compliant-mechanism work targets idealized benchmarks rather than manufacturable assistive parts, and few couple a surrogate to an assistive-device design loop.
* **Gap:** A surrogate that predicts compliant-mechanism behavior (deflection, stress, grip force) fast enough to search assistive-device designs interactively, validated on a real printable part.
* **My Contribution:** Build the surrogate from FEA data and use it to explore compliant assistive-gripper designs orders of magnitude faster than direct FEA, then validate the chosen design physically.
* **Feasibility:** *Medium.* Strong simulation + ML core; optional light hardware for validation.
* **Mentor Fit & ML Justification:** Seymur (compliant mechanisms, FEA — close to his Harvard gripper advising); Elvin (surrogate modeling). Nonlinear compliant-mechanism FEA is expensive, so the surrogate enables otherwise-impractical search.

---

## 3. Recommendation

I recommend **Candidate A — predicting prosthetic socket fit before fabrication**. It is the strongest on every axis.

1. **Tangible Local Impact:** Better-fitting sockets with less dependence on scarce expert prosthetists, directly relevant to limb-loss patients in Azerbaijan including post-conflict and landmine cases.
2. **Verified Academic Gap:** The prior-art check shows a real, explicitly-stated gap — the literature itself asks for a system that predicts fit before fabrication — rather than crowded ground.
3. **Justified Machine Learning:** ML is unambiguously justified because it replaces a slow, expert-bound FEA loop with an instant design-time predictor, directly answering our architectural core constraints.
4. **Timeline Feasibility:** Highly feasible remotely in 3–4 months on mostly public or simulable data with free compute.
5. **Dual-Mentor Multiplier:** It is the candidate that most needs both advisors. Seymur anchors the biomechanics, FEA ground truth, and manufacturability; Elvin anchors the surrogate model, data pipeline, and training rigor. The project is not credible from either side alone, which makes the mentorship pairing a genuine multiplier.

Candidates B and C are good fallbacks — B if we want a stronger manufacturing/hardware flavor, C if we want to stay closest to Seymur’s compliant-mechanism work — but A has the absolute best combination of tangible impact, a verified gap, justified ML, and dual-mentor fit.

---

## 4. Questions for Our Call

1. Do you agree Candidate A is the strongest, or would you weight B or C higher given hardware access and your time?
2. For the training data: does it make sense to generate FEA (Finite Element Analysis) cases from public or parametric limb shapes? And what FEA setup would you trust for the interface-pressure labels?
3. **Elvin** — what model type and testing approach would you want from the start so the results hold up?
4. What would each of you want to see by the end of Week 2 to feel sure we picked the right project?
