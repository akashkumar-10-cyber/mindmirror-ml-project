/**
 * MindMirror AI - Main Frontend Application Controller & Router
 * Enhanced with pop-up modal for history analysis details
 */

class MindMirrorApp {
  constructor() {
    this.container = document.getElementById('app-container');
    this.demoPresets = {
      1: "I have an exam tomorrow and I haven't studied anything. I feel like I'm going to fail.",
      2: "I have a presentation tomorrow and I am nervous about speaking in front of everyone.",
      3: "I have so many assignments that I don't know where to begin.",
      4: "My project keeps failing and I am getting frustrated."
    };
  }

  async init() {
    // Check ML backend health
    this.checkHealthStatus();

    // Setup hash-based routing
    window.addEventListener('hashchange', () => this.handleRoute());
    
    // Setup ESC key listener for modal closing
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.closeHistoryModal();
      }
    });

    // Initial route load
    this.handleRoute();
  }

  async checkHealthStatus() {
    const health = await apiClient.checkHealth();
    const badgeText = document.getElementById('model-badge-text');
    if (badgeText) {
      if (health.status === 'healthy') {
        const shortName = health.is_transformer_active ? 'DistilRoBERTa ML' : 'Neural Lexicon ML';
        badgeText.textContent = shortName;
        badgeText.parentElement.title = `Model: ${health.model_loaded}`;
      } else {
        badgeText.textContent = 'ML Offline';
        badgeText.parentElement.classList.replace('border-slate-800', 'border-rose-800');
      }
    }
  }

  handleRoute() {
    const rawHash = window.location.hash.replace('#', '') || 'home';
    const validViews = ['home', 'analyze', 'dashboard', 'history', 'how-it-works', 'safety-privacy'];
    const activeView = validViews.includes(rawHash) ? rawHash : 'home';

    appState.currentView = activeView;

    // Update active nav links
    document.querySelectorAll('.nav-link').forEach(link => {
      if (link.getAttribute('data-view') === activeView) {
        link.classList.add('bg-slate-800', 'text-teal-400');
        link.classList.remove('text-slate-300');
      } else {
        link.classList.remove('bg-slate-800', 'text-teal-400');
        link.classList.add('text-slate-300');
      }
    });

    // Render corresponding view
    this.renderActiveView(activeView);

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async renderActiveView(view) {
    if (!this.container) return;

    if (view === 'home') {
      this.container.innerHTML = components.renderHome();
    } else if (view === 'analyze') {
      this.container.innerHTML = components.renderAnalyze();
      if (appState.latestResult) {
        const input = document.getElementById('reflection-input');
        if (input && appState.latestResult.text) {
          input.value = appState.latestResult.text;
          this.updateCharCount(appState.latestResult.text);
        }
        this.displayAnalysisResult(appState.latestResult);
      }
    } else if (view === 'dashboard') {
      this.container.innerHTML = components.renderDashboard({
        total_analyses: 0,
        most_common_emotion: 'Loading...',
        avg_intensity_score: 0.0,
        most_common_context: 'Loading...',
        recent_trend: '...',
        active_patterns: ['Loading real-time metrics...'],
        emotion_distribution: {},
        context_distribution: {},
        intensity_distribution: {},
        timeline_data: []
      });
      await this.loadDashboardData();
    } else if (view === 'history') {
      this.container.innerHTML = `<div class="text-center py-12 text-slate-400"><div class="w-8 h-8 rounded-full border-2 border-teal-500 border-t-transparent animate-spin mx-auto mb-2"></div>Loading analysis history...</div>`;
      await this.loadHistoryData();
    } else if (view === 'how-it-works') {
      this.container.innerHTML = components.renderHowItWorks();
    } else if (view === 'safety-privacy') {
      this.container.innerHTML = components.renderSafetyPrivacy();
    }

    // Reinitialize Lucide icons
    if (window.lucide) {
      lucide.createIcons();
    }
  }

  // ==================== HOME QUICK ANALYZE ====================

  loadHomePreset(presetId) {
    const text = this.demoPresets[presetId];
    const input = document.getElementById('home-reflection-input');
    if (input && text) {
      input.value = text;
      input.focus();
    }
  }

  async handleHomeQuickAnalyze(e) {
    e.preventDefault();
    const input = document.getElementById('home-reflection-input');
    if (!input || !input.value.trim()) return;

    const text = input.value.trim();
    window.location.hash = '#analyze';
    setTimeout(async () => {
      const analyzeInput = document.getElementById('reflection-input');
      if (analyzeInput) {
        analyzeInput.value = text;
        this.updateCharCount(text);
      }
      const form = document.getElementById('analyze-form');
      if (form) {
        form.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
      }
    }, 80);
  }

  // ==================== ANALYZE ACTIONS ====================

  updateCharCount(val) {
    const counter = document.getElementById('char-counter');
    if (counter) {
      counter.textContent = `${val.length} / 2500 characters`;
    }
  }

  loadDemoPreset(presetId) {
    window.location.hash = '#analyze';
    setTimeout(() => {
      this.fillDemoText(presetId);
    }, 50);
  }

  fillDemoText(presetId) {
    const text = this.demoPresets[presetId];
    const input = document.getElementById('reflection-input');
    if (input && text) {
      input.value = text;
      this.updateCharCount(text);
      input.focus();
    }
  }

  async handleAnalyzeSubmit(e) {
    e.preventDefault();
    const input = document.getElementById('reflection-input');
    if (!input || !input.value.trim()) return;

    const text = input.value.trim();
    const btn = document.getElementById('analyze-btn');
    const loader = document.getElementById('loading-indicator');
    const resultBox = document.getElementById('result-container');

    if (btn) btn.disabled = true;
    if (loader) loader.classList.remove('hidden');
    if (resultBox) resultBox.classList.add('hidden');

    try {
      const response = await apiClient.analyzeText(text, appState.sessionId);
      appState.latestResult = response;

      if (response.is_crisis_alert) {
        const modal = document.getElementById('crisis-modal');
        const modalText = document.getElementById('crisis-modal-text');
        if (modal && modalText) {
          modalText.textContent = response.crisis_guidance;
          modal.classList.remove('hidden');
        }
      }

      this.displayAnalysisResult(response);
    } catch (err) {
      alert(`Analysis error: ${err.message}`);
    } finally {
      if (btn) btn.disabled = false;
      if (loader) loader.classList.add('hidden');
    }
  }

  displayAnalysisResult(result) {
    const resultBox = document.getElementById('result-container');
    if (resultBox) {
      resultBox.innerHTML = components.renderResultCard(result);
      resultBox.classList.remove('hidden');
      if (window.lucide) lucide.createIcons();
      resultBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  resetForNewAnalysis() {
    appState.latestResult = null;
    const input = document.getElementById('reflection-input');
    const resultBox = document.getElementById('result-container');
    if (input) {
      input.value = '';
      this.updateCharCount('');
      input.focus();
    }
    if (resultBox) {
      resultBox.classList.add('hidden');
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // ==================== DASHBOARD ACTIONS ====================

  async loadDashboardData() {
    try {
      const data = await apiClient.fetchDashboard(appState.sessionId);
      appState.dashboardData = data;
      this.container.innerHTML = components.renderDashboard(data);
      if (window.lucide) lucide.createIcons();

      // Render interactive Chart.js charts
      dashboardCharts.renderAll(data);
    } catch (err) {
      this.container.innerHTML = `<div class="p-6 text-center text-rose-400">Failed to load dashboard: ${err.message}</div>`;
    }
  }

  async refreshDashboard() {
    await this.loadDashboardData();
  }

  navigateToHistory() {
    window.location.hash = '#history';
  }

  scrollToChart(chartCanvasId) {
    const canvas = document.getElementById(chartCanvasId);
    if (canvas) {
      const parentCard = canvas.closest('.glass-panel');
      if (parentCard) {
        parentCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        parentCard.classList.add('ring-2', 'ring-teal-400');
        setTimeout(() => parentCard.classList.remove('ring-2', 'ring-teal-400'), 1500);
      }
    }
  }

  async filterHistoryByEmotion(emotion) {
    window.location.hash = '#history';
    setTimeout(async () => {
      await this.loadHistoryData((item) => item.emotion.toUpperCase() === emotion.toUpperCase(), `Emotion: ${emotion}`);
    }, 60);
  }

  async filterHistoryByContext(context) {
    window.location.hash = '#history';
    setTimeout(async () => {
      await this.loadHistoryData((item) => item.context.toLowerCase().includes(context.toLowerCase()) || context.toLowerCase().includes(item.context.toLowerCase()), `Domain: ${context}`);
    }, 60);
  }

  // ==================== HISTORY & POP-UP MODAL ACTIONS ====================

  async loadHistoryData(filterFn = null, filterLabel = '') {
    try {
      const items = await apiClient.fetchHistory(appState.sessionId, 100);
      appState.historyList = items;
      
      const displayItems = filterFn ? items.filter(filterFn) : items;

      this.container.innerHTML = components.renderHistory(displayItems, filterLabel);
      if (window.lucide) lucide.createIcons();
    } catch (err) {
      this.container.innerHTML = `<div class="p-6 text-center text-rose-400">Failed to load history: ${err.message}</div>`;
    }
  }

  viewHistoryDetails(itemId) {
    const findAndShowModal = (items) => {
      const item = items.find(h => h.id === itemId);
      if (!item) return;

      const modal = document.getElementById('history-detail-modal');
      const content = document.getElementById('history-modal-content');
      if (modal && content) {
        content.innerHTML = components.renderHistoryModal(item);
        modal.classList.remove('hidden');
        if (window.lucide) lucide.createIcons();
      }
    };

    if (!appState.historyList || appState.historyList.length === 0) {
      apiClient.fetchHistory(appState.sessionId, 100).then(items => {
        appState.historyList = items;
        findAndShowModal(items);
      });
    } else {
      findAndShowModal(appState.historyList);
    }
  }

  closeHistoryModal() {
    const modal = document.getElementById('history-detail-modal');
    if (modal) {
      modal.classList.add('hidden');
    }
  }

  async deleteItem(itemId) {
    if (!confirm(`Delete history record #${itemId}?`)) return;
    try {
      await apiClient.deleteHistoryItem(itemId, appState.sessionId);
      await this.loadHistoryData();
    } catch (err) {
      alert(`Delete failed: ${err.message}`);
    }
  }

  async clearAllHistory() {
    if (!confirm("Are you sure you want to delete all historical analysis records for this session? This action cannot be undone.")) return;
    try {
      await apiClient.deleteAllHistory(appState.sessionId);
      appState.latestResult = null;
      await this.loadHistoryData();
    } catch (err) {
      alert(`Clear history failed: ${err.message}`);
    }
  }
}

// Global application instance
window.app = new MindMirrorApp();

document.addEventListener('DOMContentLoaded', () => {
  window.app.init();
});
