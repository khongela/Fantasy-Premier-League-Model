# ⚽ FPL Machine Learning Model (2020–2026)

A high-performance predictive analytics engine for Fantasy Premier League. This system translates five years of historical match data into point projections using a gradient-boosted decision tree architecture, currently maintaining a verified **RMSE of 2.58**.

---

### **💻 The Stack**
* **Languages:** Python
* **Data Science:** `Pandas`, `NumPy`
* **Machine Learning:** `XGBoost`
* **Evaluation:** `Scikit-Learn`

---

### **📊 Project Stats**
* **Data Volume:** 133k+ player-gameweek rows.
* **Accuracy:** Error margin of ~2.6 points per player.
* **Algorithm:** XGBoost Regressor (500 estimators, 0.05 learning rate).

---

### **🛠️ Data Pipeline**
1. **Cleaning:** Dropped managers (Pos 5), standardized numeric types, and removed special characters from player names.
2. **Encoding:** Teams, players, and seasons mapped to unique, consistent IDs to maintain cross-season logic.
3. **Lagging:** Implemented "Last Match" stats and "Rolling 3-Game Averages" to track momentum and form.
4. **Sentinel Strategy:** Utilized `-1` flags to handle missing historical metrics (like Expected Goals) in older seasons without losing row continuity.

---

### **🔝 Key Predictors**
* **Value (8.7%):** Market price as the primary proxy for long-term point potential.
* **Transfers In (7.8%):** Sentiment analysis via manager transaction volume (Wisdom of the Crowd).
* **Minutes (5.3%):** Security of starter status as the foundation for clean sheets and attacking returns.

---

### **🚀 Roadmap**
* **Linear Programming:** Automate squad selection using a constraint solver (`PuLP`).
* **Fixture Analysis:** Add Fixture Difficulty Ratings (FDR) to improve opponent strength logic.
