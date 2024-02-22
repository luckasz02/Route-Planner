document.getElementById('routeForm').addEventListener('submit', function(e) {
    e.preventDefault();

    var startNode = document.getElementById('start').value;
    var endNode = document.getElementById('end').value;
    var algorithm = document.getElementById('algorithm').value;

    fetch('/route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ start: startNode, end: endNode, algorithm: algorithm }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = JSON.stringify(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function drawGraph() {
    const canvas = document.getElementById('graphCanvas');
    const ctx = canvas.getContext('2d');
    canvas.removeEventListener('click', onCanvasClick); // Remove existing listener

    const nodes = {'A': {x: 50, y: 100}, 'B': {x: 200, y: 50}, 'C': {x: 350, y: 100}, 'D': {x: 200, y: 200}};
    const edges = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['B', 'D']];

    // Clear canvas before redrawing
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const offsetX = (canvas.width - Math.max(...Object.values(nodes).map(n => n.x))) / 2;
    const offsetY = (canvas.height - Math.max(...Object.values(nodes).map(n => n.y))) / 2;

    // Draw nodes
    for (const [node, {x, y}] of Object.entries(nodes)) {
        ctx.beginPath();
        ctx.arc(x + offsetX, y + offsetY, 10, 0, 2 * Math.PI);
        ctx.fillStyle = 'blue';
        ctx.fill();
        ctx.stroke();
        ctx.fillText(node, x - 5 + offsetX, y - 15 + offsetY);
        ctx.closePath();
    }

    // Draw edges
    edges.forEach(edge => {
        const [start, end] = edge;
        ctx.beginPath();
        ctx.moveTo(nodes[start].x + offsetX, nodes[start].y + offsetY);
        ctx.lineTo(nodes[end].x + offsetX, nodes[end].y + offsetY);
        ctx.stroke();
    });

    function onCanvasClick(event) {
        for (const [node, {x, y}] of Object.entries(nodes)) {
            if (Math.sqrt((event.offsetX - (x + offsetX)) ** 2 + (event.offsetY - (y + offsetY)) ** 2) < 10) {
                if (!document.getElementById('start').value) {
                    document.getElementById('start').value = node;
                    console.log(`Start node selected: ${node}`);
                } else if (!document.getElementById('end').value) {
                    document.getElementById('end').value = node;
                    console.log(`End node selected: ${node}`);
                }
                break;
            }
        }
    }

    canvas.addEventListener('click', onCanvasClick);
}

drawGraph();