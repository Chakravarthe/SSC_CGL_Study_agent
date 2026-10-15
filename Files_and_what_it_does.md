## 🚀 Quick Start Execution

Run these CLI commands in order to initialize your session, evaluate your starting baseline, and begin practicing:

```bash
# 1. Initialize your profile
python agent.py init

# 2. Run the baseline diagnostic assessment
python agent.py diagnostic

# 3. Generate your personalized study plan for today
python agent.py today

# 4. Check your real-time mastery metrics and streaks
python agent.py status
```

---

## ⚙️ Core Engine Features

*   **Onboarding (`init`):** Saves your name, target exam date, and preferred daily study hours to configure your timeline.
*   **Diagnostic Mode (`diagnostic`):** Prompts you with two exploratory questions per topic to establish your baseline mastery scores instead of assessing a rigid grade.
*   **Intelligent Planner (`today`):** Dynamically prioritizes your weakest subjects first. During the final 14 days before your exam, it automatically toggles into an aggressive revision and mock test delivery mode.
*   **Adaptive Practice:** Generates clean, variable-based questions with randomized numeric values and fresh patterns to completely prevent rote memorization. The dynamic difficulty engine scales up with correct answers and scales down to reinforce concepts after a mistake. Every topic is supplemented with real-life contextual examples.
*   **Spaced Repetition Engine:** Automatically schedules forgotten or challenging topics to resurface for review at strategic intervals of 1, 3, 7, 21, and 45 days. Failing a review cycle resets the internal counter back to day one.
*   **Progress Insights (`status`):** Renders your precise mastery percentage per topic, identifies upcoming review windows, and tracks your consecutive daily learning streaks.

### 📚 Supported Syllabus Topics
The current build comprehensively evaluates **five core quantitative aptitude segments**:
1. Percentage
2. Simple Interest
3. Speed-Time-Distance
4. Ratio & Proportion
5. Number Series

---

## 🗺️ Next Steps & Feature Roadmap

- [ ] **LLM Integration & RAG Tuning:** Connect an LLM indexed over official syllabus guidelines and previous years' question papers to provide step-by-step contextual explanations whenever a student gets stuck.
- [ ] **Syllabus Expansion:** Ingest more topics and scale the question bank data directly from historical paper sets.
- [ ] **Omnichannel Interfaces:** Build out accessible presentation layers via Telegram, WhatsApp, or a web-based client front-end.
- [ ] **Comprehensive Simulation:** Implement timed full-length mock examinations alongside a dedicated error-type analytics dashboard.
