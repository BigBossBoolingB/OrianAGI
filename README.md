# OrianAGI: The Ultimate Quantum Foundational Model

OrianAGI is a state-of-the-art AGI Quantum Computing AI Foundational Model designed for training on massive datasets and outperforming industry benchmarks.

## Competitive Edge

OrianAGI surpasses models like Google Gemini, Llama 3, DeepSeek, and GPT-4 through:
- **Quantum Entangled Attention:** Coherent long-form context.
- **Hamiltonian Reasoning Engine:** Superior logical synthesis via energy minimization.
- **Hamiltonian World Model:** Physically grounded predictive simulations.
- **Genetic Sequence Alignment:** SOTA performance in biological data analysis.
- **Natively Multi-Modal:** Integrated Audio, Video, and Text processing.
- **Autonomous Agent Teams:** Collaborative problem solving.

## System Configuration (QAATA-GENESIS-V1.2)

- **Architect:** Josephis K. Wade
- **Core State:** Variational State $|Ψ(θ)⟩$

## Documentation

- [Performance & Benchmarks](docs/performance_proof.md)
- [Competitive Benchmarks](docs/benchmarks.md)
- [Dashboard UI](docs/ui.md)

### Sample Synthesis
- [Poem: The Hamiltonian Sigh](docs/samples/poem.md)
- [Article: The Dawn of Quantum AGI](docs/samples/article.md)
- [Research Paper: QHS in Foundational AI](docs/samples/research_paper.md)
- [Book Blueprint: The Architecture of AGI](docs/samples/book_blueprint.md)

### Technical Guides
- [Multi-Modal Features](docs/multimodal.md)
- [World Model](docs/world_model.md)
- [AI Agent Teams](docs/agent_teams.md)
- [Advanced Prompting](docs/prompting.md)
- [Poetic Resonance](docs/poetics.md)
- [Ethical Safeguards](docs/ethics.md)
- [Psychological Intent](docs/psychological_intent.md)
- [Parental Controls](docs/parental_controls.md)
- [Biometric Security](docs/biometrics.md)
- [Quantum Logic](docs/quantum_logic.md)
- [Architecture Details](docs/architecture.md)

## Local Development

- Create env and install deps
  - python3 -m venv .venv && . .venv/bin/activate
  - pip install -r requirements.txt
- Run tests
  - python -m unittest discover -v
- Run the app (development)
  - python -c "from orianagi.app import app; app.run(host='0.0.0.0', port=8080)"

## Containerized Production (Cloud Run)

1. Build the image
   - gcloud builds submit --tag gcr.io/PROJECT_ID/orianagi
2. Deploy to Cloud Run
   - gcloud run deploy orianagi \
       --image gcr.io/PROJECT_ID/orianagi \
       --region REGION \
       --allow-unauthenticated \
       --port 8080
3. Verify service URL works

## Firebase Hosting Integration

Add a rewrite in firebase.json to route all app traffic to the Cloud Run service:

{
  "hosting": {
    "public": "public",
    "rewrites": [
      {
        "source": "**",
        "run": {
          "serviceId": "orianagi",
          "region": "REGION"
        }
      }
    ]
  }
}

Then deploy Hosting:
- firebase deploy --only hosting

Notes:
- The app now binds to the standard PORT environment variable used by Cloud Run (with ORIANAGI_PORT as an optional override).
- requirements.txt has been slimmed to Flask only to reduce cold starts. Re-add heavy packages in a dev extras file if needed.

## License

Distributed under the Apache License 2.0.
