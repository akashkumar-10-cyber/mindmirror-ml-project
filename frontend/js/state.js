/**
 * MindMirror AI - Application State Store
 */

class StateStore {
  constructor() {
    this.sessionId = this.getOrInitSessionId();
    this.currentView = 'home';
    this.latestResult = null;
    this.isAnalyzing = false;
    this.historyList = [];
    this.dashboardData = null;
    this.modelStatus = null;
  }

  getOrInitSessionId() {
    let sid = localStorage.getItem('mindmirror_session_id');
    if (!sid) {
      sid = 'user_' + Math.random().toString(36).substring(2, 10);
      localStorage.setItem('mindmirror_session_id', sid);
    }
    return sid;
  }

  resetSession() {
    const newSid = 'user_' + Math.random().toString(36).substring(2, 10);
    localStorage.setItem('mindmirror_session_id', newSid);
    this.sessionId = newSid;
    this.latestResult = null;
    this.historyList = [];
    this.dashboardData = null;
    return newSid;
  }
}

window.appState = new StateStore();
