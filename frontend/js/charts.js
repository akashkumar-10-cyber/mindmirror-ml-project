/**
 * MindMirror AI - Chart.js Visualizations Manager with Full Interactive Click Handlers
 */

class DashboardChartsManager {
  constructor() {
    this.chartEmotionDist = null;
    this.chartIntensityBar = null;
    this.chartTimelineLine = null;
    this.chartContextRadar = null;
  }

  destroyAll() {
    if (this.chartEmotionDist) { this.chartEmotionDist.destroy(); this.chartEmotionDist = null; }
    if (this.chartIntensityBar) { this.chartIntensityBar.destroy(); this.chartIntensityBar = null; }
    if (this.chartTimelineLine) { this.chartTimelineLine.destroy(); this.chartTimelineLine = null; }
    if (this.chartContextRadar) { this.chartContextRadar.destroy(); this.chartContextRadar = null; }
  }

  renderAll(metrics) {
    this.destroyAll();

    this.renderEmotionDist(metrics.emotion_distribution);
    this.renderIntensityBar(metrics.timeline_data);
    this.renderTimelineLine(metrics.timeline_data);
    this.renderContextRadar(metrics.context_distribution);
  }

  // 1. Emotion Category Distribution (Doughnut - Clickable Slices)
  renderEmotionDist(dist) {
    const canvas = document.getElementById('chart-emotion-dist');
    if (!canvas) return;

    const labels = Object.keys(dist);
    const data = Object.values(dist);

    if (labels.length === 0) {
      labels.push('No data yet');
      data.push(1);
    }

    const colorMap = {
      'ANXIETY': '#f59e0b',
      'FEAR': '#f59e0b',
      'SADNESS': '#3b82f6',
      'ANGER': '#ef4444',
      'FRUSTRATION': '#d946ef',
      'JOY': '#10b981',
      'SURPRISE': '#8b5cf6',
      'NEUTRAL': '#94a3b8',
      'No data yet': '#334155'
    };

    const backgroundColors = labels.map(l => colorMap[l.toUpperCase()] || '#14b8a6');

    this.chartEmotionDist = new Chart(canvas, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          data: data,
          backgroundColor: backgroundColors,
          borderColor: '#0f172a',
          borderWidth: 2,
          hoverOffset: 10
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        onClick: (event, elements) => {
          if (elements && elements.length > 0) {
            const index = elements[0].index;
            const clickedEmotion = labels[index];
            if (clickedEmotion && clickedEmotion !== 'No data yet' && window.app) {
              window.app.filterHistoryByEmotion(clickedEmotion);
            }
          }
        },
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#94a3b8', boxWidth: 12, font: { family: 'Inter', size: 11 } }
          },
          tooltip: {
            callbacks: {
              afterLabel: () => '👉 Click to view history records'
            }
          }
        },
        cutout: '65%'
      }
    });
  }

  // 2. Emotion Intensity Over Time (Bar - Clickable Bars to View Full Analysis)
  renderIntensityBar(timeline) {
    const canvas = document.getElementById('chart-intensity-bar');
    if (!canvas) return;

    const labels = timeline.map(t => t.timestamp);
    const data = timeline.map(t => t.intensity_score);
    const ids = timeline.map(t => t.id);
    const emotions = timeline.map(t => t.emotion);

    const bgColors = timeline.map(t => {
      if (t.intensity === 'High') return '#f43f5e';
      if (t.intensity === 'Medium') return '#f59e0b';
      return '#14b8a6';
    });

    this.chartIntensityBar = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: labels.length ? labels : ['Sample'],
        datasets: [{
          label: 'Intensity (0.0 to 1.0)',
          data: data.length ? data : [0.5],
          backgroundColor: bgColors.length ? bgColors : ['#14b8a6'],
          borderRadius: 6,
          hoverBackgroundColor: '#38bdf8'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        onClick: (event, elements) => {
          if (elements && elements.length > 0 && ids.length > 0) {
            const index = elements[0].index;
            const recordId = ids[index];
            if (recordId && window.app) {
              window.app.viewHistoryDetails(recordId);
            }
          }
        },
        scales: {
          y: {
            min: 0,
            max: 1.0,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { color: '#64748b', font: { family: 'Inter', size: 10 } }
          },
          x: {
            grid: { display: false },
            ticks: { color: '#64748b', font: { family: 'Inter', size: 10 }, maxRotation: 45 }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: (ctx) => {
                const em = emotions[ctx.dataIndex];
                return `Emotion: ${em || 'N/A'}\n👉 Click bar to inspect full analysis`;
              }
            }
          }
        }
      }
    });
  }

  // 3. Emotion Trajectory Timeline (Smooth Line - Clickable Data Points)
  renderTimelineLine(timeline) {
    const canvas = document.getElementById('chart-timeline-line');
    if (!canvas) return;

    const labels = timeline.map(t => t.timestamp);
    const confData = timeline.map(t => t.confidence);
    const intensityData = timeline.map(t => t.intensity_score);
    const ids = timeline.map(t => t.id);

    this.chartTimelineLine = new Chart(canvas, {
      type: 'line',
      data: {
        labels: labels.length ? labels : ['Sample'],
        datasets: [
          {
            label: 'Emotion Intensity',
            data: intensityData.length ? intensityData : [0.5],
            borderColor: '#f59e0b',
            backgroundColor: 'rgba(245, 158, 11, 0.1)',
            fill: true,
            tension: 0.35,
            pointRadius: 5,
            pointHoverRadius: 8,
            pointBackgroundColor: '#f59e0b'
          },
          {
            label: 'ML Model Confidence',
            data: confData.length ? confData : [0.8],
            borderColor: '#14b8a6',
            backgroundColor: 'rgba(20, 184, 166, 0.05)',
            borderDash: [4, 4],
            fill: false,
            tension: 0.35,
            pointRadius: 4,
            pointHoverRadius: 7,
            pointBackgroundColor: '#14b8a6'
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        onClick: (event, elements) => {
          if (elements && elements.length > 0 && ids.length > 0) {
            const index = elements[0].index;
            const recordId = ids[index];
            if (recordId && window.app) {
              window.app.viewHistoryDetails(recordId);
            }
          }
        },
        scales: {
          y: {
            min: 0,
            max: 1.0,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { color: '#64748b', font: { family: 'Inter', size: 10 } }
          },
          x: {
            grid: { display: false },
            ticks: { color: '#64748b', font: { family: 'Inter', size: 10 } }
          }
        },
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#94a3b8', boxWidth: 10, font: { family: 'Inter', size: 11 } }
          },
          tooltip: {
            callbacks: {
              afterLabel: () => '👉 Click point to inspect full analysis'
            }
          }
        }
      }
    });
  }

  // 4. Domain Context Breakdown (Polar Area - Clickable Slices)
  renderContextRadar(dist) {
    const canvas = document.getElementById('chart-context-radar');
    if (!canvas) return;

    const labels = Object.keys(dist);
    const data = Object.values(dist);

    if (labels.length === 0) {
      labels.push('General');
      data.push(1);
    }

    this.chartContextRadar = new Chart(canvas, {
      type: 'polarArea',
      data: {
        labels: labels,
        datasets: [{
          data: data,
          backgroundColor: [
            'rgba(20, 184, 166, 0.7)',
            'rgba(99, 102, 241, 0.7)',
            'rgba(245, 158, 11, 0.7)',
            'rgba(244, 63, 94, 0.7)',
            'rgba(139, 92, 246, 0.7)',
            'rgba(16, 185, 129, 0.7)'
          ],
          borderColor: '#0f172a',
          borderWidth: 2,
          hoverOffset: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        onClick: (event, elements) => {
          if (elements && elements.length > 0) {
            const index = elements[0].index;
            const clickedContext = labels[index];
            if (clickedContext && clickedContext !== 'General' && window.app) {
              window.app.filterHistoryByContext(clickedContext);
            }
          }
        },
        scales: {
          r: {
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { display: false, backdropColor: 'transparent' }
          }
        },
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#94a3b8', boxWidth: 10, font: { family: 'Inter', size: 11 } }
          },
          tooltip: {
            callbacks: {
              afterLabel: () => '👉 Click to view history in this domain'
            }
          }
        }
      }
    });
  }
}

window.dashboardCharts = new DashboardChartsManager();
