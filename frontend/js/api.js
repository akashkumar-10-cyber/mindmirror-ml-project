/**
 * MindMirror AI - API Client
 * Facilitates asynchronous communication with FastAPI backend endpoints.
 */

const API_BASE = '/api';

const apiClient = {
  /**
   * Submits natural language reflection to the ML analysis pipeline.
   */
  async analyzeText(text, sessionId = 'default_user') {
    const response = await fetch(`${API_BASE}/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, session_id: sessionId })
    });

    if (!response.ok) {
      const err = await response.json().catch(() => ({ detail: 'Analysis failed' }));
      throw new Error(err.detail || `Server error: ${response.status}`);
    }

    return await response.json();
  },

  /**
   * Retrieves historical analysis records.
   */
  async fetchHistory(sessionId = 'default_user', limit = 50) {
    const response = await fetch(`${API_BASE}/history?session_id=${encodeURIComponent(sessionId)}&limit=${limit}`);
    if (!response.ok) throw new Error('Failed to fetch history');
    return await response.json();
  },

  /**
   * Retrieves dashboard aggregated metrics and chart coordinates.
   */
  async fetchDashboard(sessionId = 'default_user') {
    const response = await fetch(`${API_BASE}/dashboard?session_id=${encodeURIComponent(sessionId)}`);
    if (!response.ok) throw new Error('Failed to fetch dashboard metrics');
    return await response.json();
  },

  /**
   * Retrieves detected patterns and trends.
   */
  async fetchPatterns(sessionId = 'default_user') {
    const response = await fetch(`${API_BASE}/patterns?session_id=${encodeURIComponent(sessionId)}`);
    if (!response.ok) throw new Error('Failed to fetch patterns');
    return await response.json();
  },

  /**
   * Deletes all history for the active session.
   */
  async deleteAllHistory(sessionId = 'default_user') {
    const response = await fetch(`${API_BASE}/history?session_id=${encodeURIComponent(sessionId)}`, {
      method: 'DELETE'
    });
    if (!response.ok) throw new Error('Failed to clear history');
    return await response.json();
  },

  /**
   * Deletes a specific history record.
   */
  async deleteHistoryItem(itemId, sessionId = 'default_user') {
    const response = await fetch(`${API_BASE}/history/${itemId}?session_id=${encodeURIComponent(sessionId)}`, {
      method: 'DELETE'
    });
    if (!response.ok) throw new Error('Failed to delete history record');
    return await response.json();
  },

  /**
   * Health and model diagnostics check.
   */
  async checkHealth() {
    try {
      const response = await fetch(`${API_BASE}/health`);
      if (!response.ok) return { status: 'offline' };
      return await response.json();
    } catch {
      return { status: 'offline' };
    }
  }
};

window.apiClient = apiClient;
