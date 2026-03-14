# OrianAGI Dashboard

OrianAGI features a modern, futuristic web interface for monitoring and interacting with the model.

## Launching the Dashboard

The dashboard is built using Flask. To start the server:

```bash
export FLASK_APP=orianagi.app
flask run --host=0.0.0.0 --port=5000
```

Once running, access the dashboard at `http://localhost:5000`.

## Features
- **Real-time Status:** Monitor the general health and active node count of OrianAGI.
- **Node Management:** View detailed status and load metrics for all active quantum anchors.
- **Poetic Interaction:** Generate resonant poetry directly from the UI.
- **Training Control:** Initiate large-scale foundational training sequences.

## UI Architecture
- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3 (Futuristic theme), Vanilla JavaScript
- **API:** RESTful endpoints for model interaction.
