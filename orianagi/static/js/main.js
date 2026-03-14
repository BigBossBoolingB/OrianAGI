async function fetchStatus() {
    const response = await fetch('/api/status');
    const data = await response.json();
    document.getElementById('status-display').innerText = `Status: ${data.status} | Active Nodes: ${data.nodes_active}`;
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

// Initial fetch
fetchStatus();
fetchNodes();
// Refresh status and nodes every 10 seconds
setInterval(fetchStatus, 10000);
setInterval(fetchNodes, 10000);
