async function fetchStatus() {
    const response = await fetch('/api/status');
    const data = await response.json();
    const statusDisplay = document.getElementById('status-display');
    if (statusDisplay) {
        const { collective_state, market_sentinel } = data;
        statusDisplay.innerHTML = `
            <strong>Status:</strong> ${collective_state.status} | 
            <strong>Tier:</strong> ${collective_state.operating_tier} | 
            <strong>Threat Level:</strong> <span style="color: #ff4d4d;">${market_sentinel.cyber_threat_level}</span>
        `;
    }
    const ethicalScore = document.getElementById('ethical-score');
    if (ethicalScore) {
        const intel_status = data.intelligence_recruitment.status;
        ethicalScore.innerText = intel_status;
        if (intel_status.includes("Verified")) {
            ethicalScore.style.color = "#00f2ff";
        } else {
            ethicalScore.style.color = "#ff4d4d";
        }
    }
    const alignmentDisplay = document.getElementById('alignment-display');
    if (alignmentDisplay) {
        const { strategic_alignment } = data;
        alignmentDisplay.innerHTML = `
            <strong>Golden Path:</strong> ${strategic_alignment.golden_path} <br>
            <strong>Current Move:</strong> ${strategic_alignment.current_move}
        `;
    }
}

async function fetchNodes() {
    const response = await fetch('/api/nodes');
    const data = await response.json();
    const list = document.getElementById('nodes-list');
    list.innerHTML = '';
    data.forEach(node => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${node.name} (${node.id})</span> <span class="node-status">${node.status} [${node.load}]</span>`;
        list.appendChild(li);
    });
}

async function generatePoem() {
    const theme = document.getElementById('poetic-theme').value || 'Quantum';
    const output = document.getElementById('poem-output');
    output.innerText = 'Synthesizing...';

    const response = await fetch('/api/poetic', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ theme })
    });
    const data = await response.json();
    output.innerText = data.poem;
}

async function startTraining() {
    const status = document.getElementById('train-status');
    status.innerText = 'Initiating training sequence...';

    const response = await fetch('/api/train', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dataset: 'large_data_foundational' })
    });
    const data = await response.json();
    status.innerText = data.status;
}

async function startReasoning() {
    const query = document.getElementById('reasoning-query').value || 'Logic';
    const output = document.getElementById('reasoning-output');
    output.innerText = 'Synthesizing reasoning trace...';

    const response = await fetch('/api/reason', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
    });
    const data = await response.json();
    output.innerText = `Trace: ${data.trace.join(' → ')}\nConfidence: ${data.confidence}`;
}

async function showRouting() {
    const status = document.getElementById('qmoe-status');
    status.innerText = 'Monitoring expert routing...';

    const response = await fetch('/api/qmoe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    const data = await response.json();
    status.innerText = `Active Experts: ${data.active_experts.join(', ')}\nGain: ${data.efficiency_gain}`;
}

async function checkIntent() {
    const input = document.getElementById('intent-input').value;
    const resultDiv = document.getElementById('intent-result');
    resultDiv.innerText = 'Scanning...';

    const response = await fetch('/api/scan_intent', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input })
    });
    const data = await response.json();
    resultDiv.innerText = `Result: ${data.status.toUpperCase()}${data.reason ? ' - ' + data.reason : ''}`;
    resultDiv.style.color = data.status === 'blocked' ? '#ff4d4d' : '#00f2ff';
}

// Initial fetch
fetchStatus();
fetchNodes();
// Refresh status and nodes every 10 seconds
setInterval(fetchStatus, 10000);
setInterval(fetchNodes, 10000);
