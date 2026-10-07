/**
 * MindMirror AI - View Components Renderer
 * Clean, Modern, Feature-Focused UI with Prominent Wellness Insights & History Modal
 */

const components = {

  // ==================== 1. HOME VIEW ====================
  renderHome() {
    return `
      <div class="space-y-16 animate-fade-in py-2">
        
        <!-- HERO & QUICK TRY SECTION -->
        <section class="max-w-4xl mx-auto text-center space-y-6">
          
          <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-slate-900 border border-slate-800 text-teal-400 text-xs font-semibold shadow-sm">
            <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
            <span>AI Emotion & Action Recommendation System</span>
          </div>

          <h1 class="text-3xl sm:text-5xl font-extrabold font-display tracking-tight text-white leading-tight">
            Understand how you feel.<br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-cyan-300 to-indigo-400">Know exactly what to do next.</span>
          </h1>

          <p class="text-sm sm:text-base text-slate-300 max-w-2xl mx-auto font-normal leading-relaxed">
            Describe what's on your mind. MindMirror AI analyzes your emotional state, identifies the situation, and generates an immediate, personalized 5-step action plan.
          </p>

          <!-- QUICK INTERACTIVE INPUT CARD ON HOME -->
          <div class="pt-4 max-w-2xl mx-auto text-left">
            <div class="glass-panel-glow p-5 sm:p-6 rounded-3xl border border-teal-500/30 space-y-4 shadow-2xl">
              
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
                  Quick Reflection Analyzer
                </span>
                <span class="text-[11px] text-slate-400">Powered by DistilRoBERTa</span>
              </div>

              <!-- Quick Presets -->
              <div class="flex flex-wrap gap-1.5 text-xs">
                <button onclick="app.loadHomePreset(1)" class="px-2.5 py-1 rounded-lg bg-slate-900/90 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-teal-300 transition-colors">
                  📝 Exam Anxiety
                </button>
                <button onclick="app.loadHomePreset(2)" class="px-2.5 py-1 rounded-lg bg-slate-900/90 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-teal-300 transition-colors">
                  🎤 Presentation Stress
                </button>
                <button onclick="app.loadHomePreset(3)" class="px-2.5 py-1 rounded-lg bg-slate-900/90 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-teal-300 transition-colors">
                  📚 Workload Overload
                </button>
                <button onclick="app.loadHomePreset(4)" class="px-2.5 py-1 rounded-lg bg-slate-900/90 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-teal-300 transition-colors">
                  💻 Project Bug
                </button>
              </div>

              <!-- Input form -->
              <form onsubmit="app.handleHomeQuickAnalyze(event)" class="space-y-3">
                <textarea
                  id="home-reflection-input"
                  rows="3"
                  placeholder="Type what you are experiencing right now (e.g. I have an exam tomorrow and haven't studied anything...)"
                  class="w-full p-3.5 rounded-xl bg-slate-950/90 border border-slate-800 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-teal-500/50 text-sm leading-relaxed"
                  required
                  minlength="2"
                  maxlength="2500"
                ></textarea>

                <div class="flex items-center justify-end gap-3">
                  <button
                    type="submit"
                    class="px-5 py-2.5 rounded-xl font-bold text-xs uppercase tracking-wider bg-teal-400 hover:bg-teal-300 text-slate-950 shadow-lg shadow-teal-400/20 flex items-center gap-1.5 transition-all hover:scale-105"
                  >
                    <i data-lucide="zap" class="w-3.5 h-3.5 fill-slate-950"></i>
                    <span>Analyze & Get Action Plan</span>
                  </button>
                </div>
              </form>

            </div>
          </div>

        </section>

        <!-- CORE APPLICATION CAPABILITIES -->
        <section class="max-w-5xl mx-auto space-y-6">
          <div class="text-center space-y-1">
            <h2 class="text-xl sm:text-2xl font-bold font-display text-white">Application Capabilities</h2>
            <p class="text-xs text-slate-400">Everything designed to support your focus and clarity.</p>
          </div>

          <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5 hover:border-slate-700 transition-all">
              <div class="w-9 h-9 rounded-xl bg-teal-950 border border-teal-800 text-teal-400 flex items-center justify-center">
                <i data-lucide="brain" class="w-4 h-4"></i>
              </div>
              <h3 class="text-sm font-bold text-white font-display">Emotion Detection</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Evaluates probability distributions across 7 core emotion categories using a neural Transformer model.
              </p>
            </div>

            <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5 hover:border-slate-700 transition-all">
              <div class="w-9 h-9 rounded-xl bg-indigo-950 border border-indigo-800 text-indigo-400 flex items-center justify-center">
                <i data-lucide="compass" class="w-4 h-4"></i>
              </div>
              <h3 class="text-sm font-bold text-white font-display">Context Extraction</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Maps text to your life domain (Academic, Work, Relationships, etc.) and extracts the underlying situation.
              </p>
            </div>

            <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5 hover:border-slate-700 transition-all">
              <div class="w-9 h-9 rounded-xl bg-amber-950 border border-amber-800 text-amber-400 flex items-center justify-center">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
              </div>
              <h3 class="text-sm font-bold text-white font-display">Actionable 5-Step Triage</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Provides a concrete, prioritized roadmap tailored specifically to your situation and emotional intensity.
              </p>
            </div>

            <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5 hover:border-slate-700 transition-all">
              <div class="w-9 h-9 rounded-xl bg-rose-950 border border-rose-800 text-rose-400 flex items-center justify-center">
                <i data-lucide="trending-up" class="w-4 h-4"></i>
              </div>
              <h3 class="text-sm font-bold text-white font-display">Pattern & Trend Analytics</h3>
              <p class="text-xs text-slate-400 leading-relaxed">
                Tracks emotional shifts over time with Chart.js to help you identify recurring triggers and progress.
              </p>
            </div>

          </div>
        </section>

        <!-- QUICK LINKS FOOTER CARD -->
        <section class="max-w-4xl mx-auto glass-panel p-6 sm:p-8 rounded-3xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-6">
          <div class="space-y-1 text-center sm:text-left">
            <h3 class="text-base font-bold text-white font-display">Ready to explore historical analytics?</h3>
            <p class="text-xs text-slate-400">View real-time charts tracking your emotion distribution and intensity over time.</p>
          </div>
          <a href="#dashboard" class="px-5 py-2.5 rounded-xl font-bold text-xs uppercase tracking-wider bg-slate-900 hover:bg-slate-800 border border-slate-700 text-teal-300 flex items-center gap-2 transition-all hover:scale-105 shrink-0">
            <i data-lucide="bar-chart-3" class="w-4 h-4"></i>
            <span>Open Dashboard</span>
          </a>
        </section>

      </div>
    `;
  },

  // ==================== 2. ANALYZE VIEW ====================
  renderAnalyze() {
    return `
      <div class="max-w-4xl mx-auto space-y-8 animate-fade-in">
        
        <!-- HEADER -->
        <div class="space-y-1">
          <h2 class="text-2xl sm:text-3xl font-bold font-display text-white">Reflect & Analyze</h2>
          <p class="text-xs sm:text-sm text-slate-400">Describe what you are currently experiencing. MindMirror AI will evaluate your emotion, situation, and generate an actionable next step.</p>
        </div>

        <!-- DEMO PRESETS BUTTONS BAR -->
        <div class="p-4 rounded-2xl glass-panel border border-slate-800 space-y-2.5">
          <div class="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-teal-400"></i>
            <span>Demo Presets (Runs through real Transformer pipeline):</span>
          </div>
          <div class="flex flex-wrap gap-2">
            <button onclick="app.fillDemoText(1)" class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 text-teal-300 border border-teal-900/50 hover:border-teal-700 transition-colors">
              📝 Exam Anxiety
            </button>
            <button onclick="app.fillDemoText(2)" class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 text-teal-300 border border-teal-900/50 hover:border-teal-700 transition-colors">
              🎤 Presentation Nervousness
            </button>
            <button onclick="app.fillDemoText(3)" class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 text-teal-300 border border-teal-900/50 hover:border-teal-700 transition-colors">
              📚 Assignment Overload
            </button>
            <button onclick="app.fillDemoText(4)" class="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 text-teal-300 border border-teal-900/50 hover:border-teal-700 transition-colors">
              💻 Project Frustration
            </button>
          </div>
        </div>

        <!-- INPUT FORM -->
        <form id="analyze-form" onsubmit="app.handleAnalyzeSubmit(event)" class="space-y-4">
          <div class="relative">
            <textarea
              id="reflection-input"
              rows="4"
              placeholder="e.g. I have an exam tomorrow and I haven't studied anything. I feel like I'm going to fail..."
              class="w-full p-4 rounded-2xl bg-slate-900/90 border border-slate-800 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 text-sm sm:text-base leading-relaxed transition-all shadow-inner"
              required
              minlength="2"
              maxlength="2500"
              oninput="app.updateCharCount(this.value)"
            ></textarea>
            
            <div class="flex items-center justify-between px-2 pt-1 text-xs text-slate-400">
              <span id="char-counter">0 / 2500 characters</span>
              <span class="text-slate-400 italic">Natural language input</span>
            </div>
          </div>

          <div class="flex items-center justify-between pt-2">
            <button
              type="button"
              onclick="document.getElementById('reflection-input').value=''; app.updateCharCount('');"
              class="px-3 py-2 text-xs text-slate-400 hover:text-slate-200"
            >
              Clear Text
            </button>

            <button
              type="submit"
              id="analyze-btn"
              class="px-6 py-3 rounded-xl font-bold text-xs uppercase tracking-wider bg-teal-400 hover:bg-teal-300 text-slate-950 shadow-lg shadow-teal-400/20 flex items-center gap-2 transition-all hover:scale-105"
            >
              <i data-lucide="zap" class="w-4 h-4 fill-slate-950"></i>
              <span>Analyze Reflection</span>
            </button>
          </div>
        </form>

        <!-- REAL-TIME PROCESSING SPINNER -->
        <div id="loading-indicator" class="hidden p-8 rounded-2xl glass-panel border border-teal-500/30 text-center space-y-4 animate-fade-in">
          <div class="inline-block relative w-10 h-10">
            <div class="w-10 h-10 rounded-full border-4 border-teal-900 border-t-teal-400 animate-spin"></div>
          </div>
          <div class="space-y-1">
            <h4 class="text-sm font-semibold text-white">Running Neural Transformer Model...</h4>
            <p class="text-xs text-teal-300 font-mono">Tokenizing input & running inference</p>
          </div>
        </div>

        <!-- RESULTS CONTAINER -->
        <div id="result-container" class="hidden space-y-8 animate-fade-in"></div>

      </div>
    `;
  },

  // ==================== 3. ANALYSIS RESULT CARD ====================
  renderResultCard(res) {
    const emotionColorClass = `badge-${res.emotion.toLowerCase()}`;
    const intensityColor = res.intensity === 'High' ? 'text-rose-400 border-rose-500/30 bg-rose-950/40' : (res.intensity === 'Medium' ? 'text-amber-400 border-amber-500/30 bg-amber-950/40' : 'text-teal-400 border-teal-500/30 bg-teal-950/40');

    // Token explainability chips HTML
    const tokenChipsHtml = res.token_importance && res.token_importance.length > 0 
      ? res.token_importance.map(t => {
          let chipClass = 'token-weight-neutral';
          if (t.weight >= 0.7) chipClass = 'token-weight-high';
          else if (t.weight >= 0.4) chipClass = 'token-weight-med';
          else if (t.weight >= 0.15) chipClass = 'token-weight-low';

          return `<span class="token-chip ${chipClass}" title="Attribution weight: ${t.weight}">${t.word}</span>`;
        }).join('')
      : '<span class="text-xs text-slate-400">Token attribution computed.</span>';

    // Action plan steps HTML
    const stepsHtml = res.recommendation.map((step, idx) => `
      <li class="flex items-start gap-3.5 p-4 rounded-2xl bg-slate-900/80 border border-slate-800/90 hover:border-teal-500/50 transition-all shadow-sm">
        <span class="flex-shrink-0 w-7 h-7 rounded-xl bg-teal-950 border border-teal-700 text-teal-300 text-xs font-bold flex items-center justify-center font-mono shadow-inner">
          ${idx + 1}
        </span>
        <span class="text-sm text-slate-100 leading-relaxed font-normal">${step}</span>
      </li>
    `).join('');

    return `
      <!-- TOP METRIC CARDS GRID (NO TRUNCATION, FULL VISIBILITY) -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
        
        <!-- Detected Emotion -->
        <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Detected Emotion</span>
          <div class="flex items-center gap-2">
            <span class="text-base sm:text-lg font-bold text-white ${emotionColorClass} px-2.5 py-0.5 rounded-lg">
              ${res.emotion}
            </span>
          </div>
          <p class="text-[11px] text-slate-400 pt-1 font-mono">${Math.round(res.confidence * 100)}% ML Confidence</p>
        </div>

        <!-- Emotion Intensity -->
        <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Intensity Level</span>
          <div>
            <span class="text-base sm:text-lg font-bold px-2.5 py-0.5 rounded-lg border ${intensityColor}">
              ${res.intensity}
            </span>
          </div>
          <p class="text-[11px] text-slate-400 pt-1 font-mono">Score: ${res.intensity_score} / 1.0</p>
        </div>

        <!-- Context Domain (Fully Visible) -->
        <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Life Context</span>
          <div class="text-sm sm:text-base font-bold text-white leading-tight break-words">
            ${res.context}
          </div>
          <p class="text-[11px] text-teal-400 pt-1">Domain Verified</p>
        </div>

        <!-- Situation Dynamics (Fully Visible) -->
        <div class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Situation</span>
          <div class="text-xs font-semibold text-slate-200 leading-snug break-words">
            ${res.situation}
          </div>
          <p class="text-[11px] text-slate-400 pt-1">Context Anchors</p>
        </div>

      </div>

      <!-- CRISIS / SAFETY NOTIFICATION IF FLAGGED -->
      ${res.is_crisis_alert ? `
        <div class="p-4 rounded-2xl bg-rose-950/60 border border-rose-500/50 space-y-2 text-rose-200 animate-pulse">
          <div class="flex items-center gap-2 font-bold text-sm text-rose-300">
            <i data-lucide="life-buoy" class="w-5 h-5"></i>
            <span>Supportive Safety Notice</span>
          </div>
          <p class="text-xs leading-relaxed whitespace-pre-line">${res.crisis_guidance}</p>
        </div>
      ` : ''}

      <!-- HISTORICAL PATTERN NOTIFICATION (IF AVAILABLE) -->
      ${res.pattern_note ? `
        <div class="p-4 rounded-2xl bg-indigo-950/50 border border-indigo-500/40 flex items-start gap-3 text-indigo-200">
          <i data-lucide="trending-up" class="w-5 h-5 text-indigo-400 shrink-0 mt-0.5"></i>
          <div class="space-y-0.5">
            <span class="text-xs font-bold uppercase tracking-wider text-indigo-400">Historical Pattern Detected</span>
            <p class="text-xs text-slate-200 leading-relaxed">${res.pattern_note}</p>
          </div>
        </div>
      ` : ''}

      <!-- ⭐ WHAT CAN YOU DO RIGHT NOW? (ACTION RECOMMENDATION) -->
      <div class="glass-panel-glow p-6 sm:p-8 rounded-3xl border border-teal-500/30 space-y-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3.5">
            <div class="w-11 h-11 rounded-2xl bg-teal-500/20 border border-teal-500/40 flex items-center justify-center shadow-inner">
              <i data-lucide="check-square" class="w-5 h-5 text-teal-400"></i>
            </div>
            <div>
              <h3 class="text-lg sm:text-xl font-bold font-display text-white">What can you do right now?</h3>
              <p class="text-xs text-slate-400">Prioritized situation-specific next-step action plan</p>
            </div>
          </div>
          <span class="px-3 py-1 rounded-full text-xs font-bold bg-teal-950 text-teal-300 border border-teal-800">
            5-Step Action Plan
          </span>
        </div>

        <ul class="space-y-3">
          ${stepsHtml}
        </ul>
      </div>

      <!-- ⭐ PROMINENT PERSONALIZED WELLNESS & RESILIENCE INSIGHT -->
      ${res.general_suggestion ? `
        <div class="glass-panel p-6 sm:p-7 rounded-3xl border border-emerald-500/40 bg-gradient-to-r from-slate-900 via-emerald-950/20 to-slate-900 space-y-3 shadow-lg">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 shadow-inner">
                <i data-lucide="heart-handshake" class="w-5 h-5"></i>
              </div>
              <div>
                <h4 class="text-base font-bold font-display text-white">Personalized Wellness & Resilience Insight</h4>
                <p class="text-[11px] text-emerald-400/90 font-medium">Mindful grounding & mental wellbeing perspective</p>
              </div>
            </div>
            <span class="hidden sm:inline-flex px-3 py-1 rounded-full text-[11px] font-semibold bg-emerald-950/80 text-emerald-300 border border-emerald-800/60">
              Wellness Guidance
            </span>
          </div>

          <div class="p-4 rounded-2xl bg-slate-950/80 border border-emerald-900/40 text-sm sm:text-base text-emerald-100 font-medium leading-relaxed italic shadow-inner">
            "${res.general_suggestion}"
          </div>
        </div>
      ` : ''}

      <!-- EXPLAINABLE AI (XAI) SECTION -->
      <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <i data-lucide="binary" class="w-5 h-5 text-teal-400"></i>
            <h4 class="text-sm font-bold text-white font-display">Word-Level Importance (Explainable AI)</h4>
          </div>
          <span class="text-[11px] text-slate-400 font-mono">Token Attribution</span>
        </div>

        <div class="space-y-2">
          <div class="flex items-center justify-between text-[11px] text-slate-400">
            <span>Detected Language Signals:</span>
            <div class="flex items-center gap-3">
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded bg-rose-500"></span> High Influence</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded bg-amber-500"></span> Moderate</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded bg-teal-500"></span> Contextual</span>
            </div>
          </div>
          <div class="p-3.5 rounded-xl bg-slate-950/80 border border-slate-800/80 leading-loose">
            ${tokenChipsHtml}
          </div>
        </div>
      </div>

      <!-- ACTION BUTTONS -->
      <div class="flex flex-wrap items-center justify-between gap-4 pt-4 border-t border-slate-800">
        <button onclick="app.resetForNewAnalysis()" class="px-4 py-2 rounded-xl text-xs font-semibold bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-200 flex items-center gap-1.5 transition-colors">
          <i data-lucide="plus-circle" class="w-4 h-4 text-teal-400"></i>
          <span>Analyze Another Entry</span>
        </button>

        <div class="flex items-center gap-3">
          <a href="#history" class="px-4 py-2 rounded-xl text-xs font-semibold bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white flex items-center gap-1.5 transition-colors">
            <i data-lucide="history" class="w-4 h-4"></i>
            <span>View Full History</span>
          </a>

          <a href="#dashboard" class="px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider bg-teal-400 hover:bg-teal-300 text-slate-950 flex items-center gap-1.5 transition-colors shadow-md shadow-teal-400/20">
            <i data-lucide="bar-chart-2" class="w-4 h-4 fill-slate-950"></i>
            <span>Open Dashboard</span>
          </a>
        </div>
      </div>
    `;
  },

  // ==================== 4. DASHBOARD VIEW (FULLY CLICKABLE) ====================
  renderDashboard(data) {
    return `
      <div class="space-y-8 animate-fade-in">
        
        <!-- HEADER -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div class="space-y-1">
            <h2 class="text-2xl sm:text-3xl font-bold font-display text-white">Analytics & Emotion Trends</h2>
            <p class="text-xs sm:text-sm text-slate-400">Interactive analytics metrics. Click any card, pattern, or chart element below to filter and inspect history records.</p>
          </div>

          <div class="flex items-center gap-2">
            <button onclick="app.refreshDashboard()" class="px-3.5 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-medium text-slate-300 flex items-center gap-1.5 transition-colors">
              <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
              <span>Refresh Metrics</span>
            </button>
          </div>
        </div>

        <!-- CLICKABLE SUMMARY KPI CARDS -->
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
          
          <!-- Total Analyses (Clickable) -->
          <div 
            onclick="app.navigateToHistory()" 
            class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1 hover:border-teal-500/60 hover:bg-slate-900/90 transition-all cursor-pointer group shadow-sm hover:scale-[1.02]"
            title="Click to view all history records"
          >
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 group-hover:text-teal-400 transition-colors">Total Analyses</span>
              <i data-lucide="external-link" class="w-3 h-3 text-slate-500 group-hover:text-teal-400 transition-colors"></i>
            </div>
            <div class="text-2xl font-bold font-display text-white">${data.total_analyses}</div>
            <p class="text-[11px] text-teal-400">Click to view log &rarr;</p>
          </div>

          <!-- Top Emotion (Clickable) -->
          <div 
            onclick="app.filterHistoryByEmotion('${data.most_common_emotion}')" 
            class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1 hover:border-teal-500/60 hover:bg-slate-900/90 transition-all cursor-pointer group shadow-sm hover:scale-[1.02]"
            title="Click to view all '${data.most_common_emotion}' reflections"
          >
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 group-hover:text-teal-400 transition-colors">Top Emotion</span>
              <i data-lucide="filter" class="w-3 h-3 text-slate-500 group-hover:text-teal-400 transition-colors"></i>
            </div>
            <div class="text-xl font-bold text-teal-300 truncate">${data.most_common_emotion}</div>
            <p class="text-[11px] text-slate-400 group-hover:text-teal-300 transition-colors">Click to filter &rarr;</p>
          </div>

          <!-- Avg Intensity (Clickable) -->
          <div 
            onclick="app.scrollToChart('chart-intensity-bar')" 
            class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1 hover:border-amber-500/60 hover:bg-slate-900/90 transition-all cursor-pointer group shadow-sm hover:scale-[1.02]"
            title="Click to inspect Intensity Breakdown Chart"
          >
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 group-hover:text-amber-400 transition-colors">Avg Intensity</span>
              <i data-lucide="bar-chart" class="w-3 h-3 text-slate-500 group-hover:text-amber-400 transition-colors"></i>
            </div>
            <div class="text-2xl font-bold text-amber-300 font-mono">${data.avg_intensity_score} <span class="text-xs text-slate-400 font-normal">/ 1.0</span></div>
            <p class="text-[11px] text-slate-400 group-hover:text-amber-300 transition-colors">View intensity chart &rarr;</p>
          </div>

          <!-- Primary Domain (Clickable) -->
          <div 
            onclick="app.filterHistoryByContext('${data.most_common_context}')" 
            class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1 hover:border-indigo-500/60 hover:bg-slate-900/90 transition-all cursor-pointer group shadow-sm hover:scale-[1.02]"
            title="Click to view all '${data.most_common_context}' reflections"
          >
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 group-hover:text-indigo-400 transition-colors">Primary Domain</span>
              <i data-lucide="compass" class="w-3 h-3 text-slate-500 group-hover:text-indigo-400 transition-colors"></i>
            </div>
            <div class="text-base sm:text-lg font-bold text-indigo-300 truncate">${data.most_common_context}</div>
            <p class="text-[11px] text-slate-400 group-hover:text-indigo-300 transition-colors">Filter domain &rarr;</p>
          </div>

          <!-- Recent Trend (Clickable) -->
          <div 
            onclick="app.scrollToChart('chart-timeline-line')" 
            class="glass-panel p-4 rounded-2xl border border-slate-800 space-y-1 hover:border-teal-500/60 hover:bg-slate-900/90 transition-all cursor-pointer group shadow-sm hover:scale-[1.02]"
            title="Click to view Trajectory Timeline Chart"
          >
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 group-hover:text-teal-400 transition-colors">Recent Trend</span>
              <i data-lucide="trending-up" class="w-3 h-3 text-slate-500 group-hover:text-teal-400 transition-colors"></i>
            </div>
            <div class="text-base sm:text-lg font-bold text-white truncate">${data.recent_trend}</div>
            <p class="text-[11px] text-slate-400 group-hover:text-teal-300 transition-colors">Inspect timeline &rarr;</p>
          </div>

        </div>

        <!-- CLICKABLE PATTERN DETECTION INSIGHTS -->
        <div class="glass-panel p-6 rounded-2xl border border-indigo-500/30 space-y-3 bg-gradient-to-r from-slate-900/90 to-indigo-950/40">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <i data-lucide="sparkles" class="w-5 h-5 text-indigo-400"></i>
              <h3 class="text-sm font-bold text-white font-display">Calculated Pattern Analysis</h3>
            </div>
            <span class="text-[11px] text-indigo-300">Interactive Discovery</span>
          </div>
          <div class="grid sm:grid-cols-2 gap-2.5">
            ${data.active_patterns.map(p => `
              <div 
                onclick="app.navigateToHistory()"
                class="p-3 rounded-xl bg-slate-950/70 border border-indigo-900/40 hover:border-indigo-500/60 hover:bg-indigo-950/30 transition-all cursor-pointer flex items-start gap-2.5 text-xs text-slate-200 group"
                title="Click to view historical entries associated with this pattern"
              >
                <span class="text-indigo-400 font-bold mt-0.5">•</span>
                <span class="leading-relaxed group-hover:text-white transition-colors">${p}</span>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- 4 FULLY CLICKABLE CHART.JS CHARTS GRID -->
        <div class="grid md:grid-cols-2 gap-6">
          
          <!-- Chart 1: Emotion Distribution (Click Slices to Filter) -->
          <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-3 hover:border-slate-700 transition-all">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-slate-200">1. Emotion Category Distribution</h4>
              <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-teal-950 border border-teal-800 text-teal-300">Click slice to filter</span>
            </div>
            <div class="h-64 relative flex items-center justify-center cursor-pointer">
              <canvas id="chart-emotion-dist"></canvas>
            </div>
          </div>

          <!-- Chart 2: Intensity Over Time (Click Bar to View Full Analysis) -->
          <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-3 hover:border-slate-700 transition-all">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-slate-200">2. Emotion Intensity Over Time</h4>
              <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-amber-950 border border-amber-800 text-amber-300">Click bar to view</span>
            </div>
            <div class="h-64 relative cursor-pointer">
              <canvas id="chart-intensity-bar"></canvas>
            </div>
          </div>

          <!-- Chart 3: Emotion Trend Timeline (Click Point to View Full Analysis) -->
          <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-3 hover:border-slate-700 transition-all">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-slate-200">3. Emotion Trajectory Timeline</h4>
              <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-indigo-950 border border-indigo-800 text-indigo-300">Click point to view</span>
            </div>
            <div class="h-64 relative cursor-pointer">
              <canvas id="chart-timeline-line"></canvas>
            </div>
          </div>

          <!-- Chart 4: Context Distribution (Click Slice to Filter) -->
          <div class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-3 hover:border-slate-700 transition-all">
            <div class="flex items-center justify-between">
              <h4 class="text-sm font-bold text-slate-200">4. Domain Context Breakdown</h4>
              <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-rose-950 border border-rose-800 text-rose-300">Click slice to filter</span>
            </div>
            <div class="h-64 relative flex items-center justify-center cursor-pointer">
              <canvas id="chart-context-radar"></canvas>
            </div>
          </div>

        </div>

      </div>
    `;
  },

  // ==================== 5. HISTORY VIEW ====================
  renderHistory(items, filterLabel = '') {
    return `
      <div class="space-y-6 animate-fade-in max-w-5xl mx-auto">
        
        <!-- HEADER & ACTIONS -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div class="space-y-1">
            <div class="flex items-center gap-3">
              <h2 class="text-2xl sm:text-3xl font-bold font-display text-white">Analysis History Log</h2>
              ${filterLabel ? `
                <span class="px-2.5 py-1 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 text-xs font-semibold flex items-center gap-1.5">
                  <i data-lucide="filter" class="w-3.5 h-3.5"></i>
                  Filtered: ${filterLabel}
                  <button onclick="app.loadHistoryData()" class="ml-1 text-slate-400 hover:text-white font-bold">&times;</button>
                </span>
              ` : ''}
            </div>
            <p class="text-xs sm:text-sm text-slate-400">Chronological database records of your reflections, emotions, and generated action steps.</p>
          </div>

          <div class="flex items-center gap-3">
            ${filterLabel ? `
              <button onclick="app.loadHistoryData()" class="px-3 py-1.5 rounded-lg bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-medium text-slate-300 flex items-center gap-1 transition-colors">
                <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
                <span>Show All</span>
              </button>
            ` : ''}
            <button onclick="app.clearAllHistory()" class="px-3.5 py-1.5 rounded-lg bg-rose-950/60 hover:bg-rose-900 border border-rose-800/80 text-xs font-semibold text-rose-300 flex items-center gap-1.5 transition-colors">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
              <span>Clear All History</span>
            </button>
          </div>
        </div>

        <!-- ITEMS LIST -->
        ${items.length === 0 ? `
          <div class="p-12 text-center glass-panel rounded-2xl border border-slate-800 space-y-4">
            <div class="w-12 h-12 rounded-full bg-slate-900 border border-slate-800 mx-auto flex items-center justify-center text-slate-400">
              <i data-lucide="inbox" class="w-6 h-6"></i>
            </div>
            <div class="space-y-1">
              <h4 class="text-sm font-semibold text-white">No matching history records found</h4>
              <p class="text-xs text-slate-400">${filterLabel ? 'Try clearing the active filter or creating a new reflection.' : 'Start an analysis to begin tracking your emotional patterns over time.'}</p>
            </div>
            <a href="#analyze" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-lg text-xs font-semibold bg-teal-500 hover:bg-teal-400 text-slate-950 transition-colors">
              <i data-lucide="plus" class="w-4 h-4"></i>
              <span>Create Reflection Entry</span>
            </a>
          </div>
        ` : `
          <div class="space-y-4">
            ${items.map(item => `
              <div 
                onclick="app.viewHistoryDetails(${item.id})"
                class="glass-panel p-5 rounded-2xl border border-slate-800 space-y-3.5 hover:border-teal-500/50 hover:bg-slate-900/90 transition-all cursor-pointer group shadow-sm"
              >
                
                <div class="flex flex-wrap items-center justify-between gap-2 text-xs">
                  <div class="flex items-center gap-2">
                    <span class="font-bold text-white badge-${item.emotion.toLowerCase()} px-2.5 py-0.5 rounded-md">
                      ${item.emotion}
                    </span>
                    <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-800 text-slate-300 font-medium">
                      Intensity: <strong class="text-white">${item.intensity}</strong> (${item.intensity_score})
                    </span>
                    <span class="px-2 py-0.5 rounded bg-slate-900 border border-slate-800 text-teal-300 font-medium">
                      Context: ${item.context}
                    </span>
                  </div>

                  <div class="flex items-center gap-3 text-slate-400">
                    <span class="font-mono text-[11px]">${item.timestamp ? new Date(item.timestamp).toLocaleString() : ''}</span>
                    <button 
                      onclick="event.stopPropagation(); app.deleteItem(${item.id})" 
                      class="text-slate-400 hover:text-rose-400 p-1.5 rounded-lg hover:bg-slate-800 transition-colors" 
                      title="Delete record"
                    >
                      <i data-lucide="trash" class="w-3.5 h-3.5"></i>
                    </button>
                  </div>
                </div>

                <p class="text-sm text-slate-100 font-medium italic bg-slate-950/80 p-3.5 rounded-xl border border-slate-900 leading-relaxed">
                  "${item.text}"
                </p>

                <div class="pt-2 border-t border-slate-800/80 text-xs text-slate-300 flex items-center justify-between">
                  <span class="font-semibold text-teal-400 flex items-center gap-1.5">
                    <i data-lucide="check-square" class="w-3.5 h-3.5"></i>
                    ${item.recommendation.length}-Step Action Plan Available
                  </span>
                </div>

              </div>
            `).join('')}
          </div>
        `}

      </div>
    `;
  },

  // ==================== 6. HOW IT WORKS VIEW ====================
  renderHowItWorks() {
    return `
      <div class="space-y-12 animate-fade-in max-w-4xl mx-auto">
        
        <div class="text-center space-y-2">
          <h2 class="text-2xl sm:text-3xl font-bold font-display text-white">How MindMirror AI Works</h2>
          <p class="text-xs sm:text-sm text-slate-400 max-w-2xl mx-auto">
            A comprehensive Machine Learning pipeline combining Transformer NLP, intensity estimation, situational taxonomy, and heuristic recommendation matrices.
          </p>
        </div>

        <!-- 8-STAGE WORKFLOW PIPELINE -->
        <div class="space-y-4">
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <i data-lucide="git-branch" class="w-4 h-4 text-teal-400"></i>
            <span>The 8-Stage Machine Learning Workflow</span>
          </h3>

          <div class="grid gap-3 font-mono text-xs">
            
            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">1</span>
              <div>
                <strong class="text-white text-xs">Natural Language Input</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">User provides free-form reflection describing their immediate emotional state and situation.</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">2</span>
              <div>
                <strong class="text-white text-xs">Tokenization & Preprocessing</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Text is sanitized, bounded, and tokenized using byte-pair encoding (BPE) for neural input.</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">3</span>
              <div>
                <strong class="text-white text-xs">Pretrained Transformer Inference (PyTorch)</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Evaluates logits across 7 emotion classes using Hugging Face DistilRoBERTa.</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">4</span>
              <div>
                <strong class="text-white text-xs">Explainable AI (Token Perturbation)</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Computes token importance attribution by measuring class probability deltas: Attribution(w) = P(base) - P(masked).</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">5</span>
              <div>
                <strong class="text-white text-xs">Intensity Estimation</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Combines model probability magnitude with linguistic intensifiers and urgency cues into Low, Medium, or High.</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">6</span>
              <div>
                <strong class="text-white text-xs">Domain Context & Situation Extraction</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Identifies one of 8 life contexts (Academic, Work, Relationships, etc.) and extracts concrete situational dynamics.</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">7</span>
              <div>
                <strong class="text-white text-xs">Emotion-Aware Action Recommendation Synthesis</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Synthesizes Emotion + Intensity + Context + Situation + History into a structured 5-step prioritized action triage.</p>
              </div>
            </div>

            <div class="p-4 rounded-xl glass-panel border border-slate-800 flex items-start gap-4">
              <span class="w-7 h-7 rounded-lg bg-teal-950 border border-teal-800 text-teal-300 flex items-center justify-center font-bold">8</span>
              <div>
                <strong class="text-white text-xs">Persistence & Pattern Analytics</strong>
                <p class="text-slate-400 font-sans text-xs pt-1">Stores the analysis in SQLite and dynamically discovers recurring triggers across historical sessions.</p>
              </div>
            </div>

          </div>
        </div>

      </div>
    `;
  },

  // ==================== 7. SAFETY & PRIVACY VIEW ====================
  renderSafetyPrivacy() {
    return `
      <div class="space-y-8 animate-fade-in max-w-4xl mx-auto">
        <div class="space-y-1">
          <h2 class="text-2xl sm:text-3xl font-bold font-display text-white">Safety & Privacy Protocols</h2>
          <p class="text-xs sm:text-sm text-slate-400">Clear boundaries regarding prototype capabilities, user privacy, and supportive safety.</p>
        </div>

        <div class="grid gap-6">
          
          <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="shield-check" class="w-5 h-5 text-teal-400"></i>
              <span>Supportive Wellness Prototype Boundaries</span>
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              MindMirror AI is designed strictly as an emotion-aware machine learning prototype for supportive reflection and educational demonstration. 
              <strong>It does NOT diagnose medical or psychiatric conditions, prescribe medications, or guarantee outcomes.</strong>
            </p>
          </div>

          <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-3">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="lock" class="w-5 h-5 text-teal-400"></i>
              <span>Local Storage & Data Privacy</span>
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              Your reflection logs are stored in a local SQLite database (<code>mindmirror.db</code>) on your local machine. No text is sold or used for external advertising. You maintain full control to delete individual history entries or wipe your complete session history at any time.
            </p>
          </div>

          <div class="glass-panel p-6 rounded-2xl border border-rose-500/30 space-y-3 bg-rose-950/20">
            <h3 class="text-base font-bold text-rose-300 flex items-center gap-2">
              <i data-lucide="life-buoy" class="w-5 h-5 text-rose-400"></i>
              <span>Crisis & Emergency Resources</span>
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed">
              If you or someone you know is experiencing acute emotional distress or thoughts of self-harm, please reach out to dedicated human professionals:
            </p>
            <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
              <li><strong>US & Canada:</strong> Call or text <strong>988</strong> (Suicide & Crisis Lifeline).</li>
              <li><strong>Crisis Text Line:</strong> Text <strong>HOME</strong> to <strong>741741</strong>.</li>
              <li><strong>UK:</strong> Call <strong>111</strong> (NHS) or <strong>116 123</strong> (Samaritans).</li>
              <li><strong>International:</strong> Visit <a href="https://findahelpline.com" target="_blank" class="text-teal-400 underline">findahelpline.com</a>.</li>
            </ul>
          </div>

        </div>
      </div>
    `;
  },

  // ==================== 8. HISTORY DETAIL POP-UP MODAL (VERTICAL LAYOUT) ====================
  renderHistoryModal(item) {
    const emotionColorClass = `badge-${item.emotion.toLowerCase()}`;
    const intensityColor = item.intensity === 'High' ? 'text-rose-400 border-rose-500/30 bg-rose-950/40' : (item.intensity === 'Medium' ? 'text-amber-400 border-amber-500/30 bg-amber-950/40' : 'text-teal-400 border-teal-500/30 bg-teal-950/40');

    const stepsHtml = (item.recommendation || []).map((step, idx) => `
      <li class="flex items-start gap-3 p-3 rounded-xl bg-slate-950/90 border border-slate-800 text-xs sm:text-sm text-slate-200">
        <span class="flex-shrink-0 w-6 h-6 rounded-lg bg-teal-950 border border-teal-700 text-teal-300 text-xs font-bold flex items-center justify-center font-mono mt-0.5">
          ${idx + 1}
        </span>
        <span class="leading-relaxed">${step}</span>
      </li>
    `).join('');

    return `
      <!-- MODAL HEADER -->
      <div class="flex items-center justify-between pb-3 border-b border-slate-800 shrink-0">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-teal-500/20 border border-teal-500/40 flex items-center justify-center text-teal-400">
            <i data-lucide="file-text" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-base font-bold font-display text-white">Analysis Details</h3>
            <p class="text-[11px] text-slate-400 font-mono">${item.timestamp ? new Date(item.timestamp).toLocaleString() : 'Record Details'}</p>
          </div>
        </div>
        <button 
          onclick="app.closeHistoryModal()" 
          class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition-colors"
          title="Close details"
        >
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- VERTICAL DETAILS SECTION -->
      <div class="space-y-4 text-xs sm:text-sm py-1">

        <!-- 1. TEXT -->
        <div class="space-y-1">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Your Reflection</span>
          <div class="p-3.5 rounded-xl bg-slate-950/90 border border-slate-800 text-slate-100 font-medium italic leading-relaxed">
            "${item.text}"
          </div>
        </div>

        <!-- 2, 3, 4, 5. VERTICAL METRICS STACK -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          
          <!-- Detected Emotion -->
          <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Detected Emotion</span>
            <div class="flex items-center gap-2">
              <span class="font-bold text-white ${emotionColorClass} px-2.5 py-0.5 rounded-md text-xs">
                ${item.emotion}
              </span>
              <span class="text-[11px] text-slate-400 font-mono">${Math.round((item.confidence || 0.8) * 100)}% Confidence</span>
            </div>
          </div>

          <!-- Intensity Level -->
          <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Intensity Level</span>
            <div class="flex items-center gap-2">
              <span class="font-bold px-2 py-0.5 rounded-md border ${intensityColor} text-xs">
                ${item.intensity}
              </span>
              <span class="text-[11px] text-slate-400 font-mono">Score: ${item.intensity_score} / 1.0</span>
            </div>
          </div>

          <!-- Life Context -->
          <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Life Context</span>
            <div class="font-bold text-teal-300 text-xs sm:text-sm">
              ${item.context}
            </div>
          </div>

          <!-- Situation -->
          <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 space-y-1">
            <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400">Situation</span>
            <div class="font-medium text-slate-200 text-xs leading-snug">
              ${item.situation || 'General situational context'}
            </div>
          </div>

        </div>

        <!-- 6. WHAT CAN YOU DO RIGHT NOW? -->
        <div class="space-y-2 pt-1">
          <div class="flex items-center gap-2 text-teal-400 font-bold text-xs uppercase tracking-wider">
            <i data-lucide="check-square" class="w-4 h-4"></i>
            <span>What can you do right now?</span>
          </div>
          <ul class="space-y-2">
            ${stepsHtml}
          </ul>
        </div>

        <!-- 7. PERSONALIZED WELLNESS & RESILIENCE INSIGHT -->
        ${item.general_suggestion ? `
          <div class="p-4 rounded-2xl bg-slate-950 border border-emerald-500/40 space-y-1.5">
            <div class="flex items-center gap-2 text-emerald-400 font-bold text-xs">
              <i data-lucide="heart-handshake" class="w-4 h-4"></i>
              <span>Personalized Wellness & Resilience Insight</span>
            </div>
            <p class="text-xs sm:text-sm text-emerald-100 italic leading-relaxed">
              "${item.general_suggestion}"
            </p>
          </div>
        ` : ''}

      </div>

      <!-- MODAL FOOTER -->
      <div class="flex items-center justify-end pt-3 border-t border-slate-800 shrink-0">
        <button 
          onclick="app.closeHistoryModal()" 
          class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition-colors"
        >
          Close
        </button>
      </div>
    `;
  }
};

window.components = components;
