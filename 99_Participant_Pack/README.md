# Jumia Workshop 2025 - Participant Pack
## Workshop Content Overview

This participant pack contains all materials needed for the Jumia Data & AI Workshop.

---

## 📁 File Structure

### 00_Cheat_Sheet.md
Your survival guide for the workshop. Contains:
- Module 1: Blind Discovery prompts and guidance
- Module 2: Python transformation snippets for n8n
- Module 3: SOX Quality Gate checklist

**Action:** Export this to PDF before the workshop and keep it handy!

---

### 01_Data_Samples/

#### intella_sample.csv (44 products)
Real product data from Jumia with intentional issues for testing:
- **3 Jumia Express products** (dsc_custom_label_one = 1)
- **5 data anomalies** to discover:
  - Products with stock = 0
  - Missing image URLs
  - Negative prices

**Use Case:** Module 1 (Blind Discovery) and Module 2 (Transformation)

#### clean_feed_for_chatbot.json (39 products)
Pre-cleaned JSON output after transformation.
- Stock <= 0 products filtered out
- Categories properly formatted with ' > ' separator
- Ready for chatbot/RAG implementation

**Use Case:** Module 3 bonus (Chatbot demo)

#### sox_test_data.csv
Test dataset for SOX anomaly detection exercises.

**Use Case:** Module 3 (Quality Gate)

---

### 02_n8n_Templates/

#### Template_Intella.json
Starter workflow for the Intella feed transformation.

**Use Case:** Module 2 (n8n Python Code node)

#### Template_SOX.json
Starter workflow for the SOX quality gate agent.

**Use Case:** Module 3 (AI Agent implementation)

---

### 03_Exercises/

#### Jumia_Table_Columns.txt
List of 20 column names from the Jumia database schema.

**Use Case:** Module 1 - Copy this list and paste it into your AI assistant to generate SQL queries.

#### Blind_Discovery_Prompt.txt
Detailed instructions and suggested prompts for the "Data Hunt" exercise.

**Use Case:** Module 1 - Follow these steps when you have no documentation.

#### bad_query.sql
A deliberately inefficient SQL query with 3 performance crimes:
1. SELECT * (selects all columns)
2. YEAR(DATE(...)) on indexed column (breaks index)
3. Inefficient subquery with IN clause

**Challenge:** Paste this into Gemini/ChatGPT and ask: "Why is this query slow and how can I optimize it for Athena?"

**Use Case:** Module 4 (Efficiency Day)

#### Bad_SQL_Challenge.txt
Additional SQL optimization challenges.

---

## 🎯 Workshop Flow

### Day 1: Data Intelligence

**Module 1 (Morning): Blind Discovery**
→ Use `Jumia_Table_Columns.txt` + `Blind_Discovery_Prompt.txt`
→ Generate SQL with AI assistance

**Module 2 (Afternoon): Transformation**
→ Use `intella_sample.csv` + `Template_Intella.json`
→ Build Python transformation in n8n

**Module 3 (End of Day): Quality Gate**
→ Use `sox_test_data.csv` + `Template_SOX.json`
→ Create AI agent for anomaly detection

**Bonus: Chatbot**
→ Use `clean_feed_for_chatbot.json`
→ Build RAG chatbot with clean data

### Day 2: Efficiency & Best Practices

**Module 4: SQL Optimization**
→ Use `bad_query.sql`
→ Learn to spot and fix performance issues

---

## ✅ Pre-Workshop Checklist

- [ ] Export `00_Cheat_Sheet.md` to PDF
- [ ] Test opening all CSV files
- [ ] Verify n8n templates import correctly
- [ ] Keep `Jumia_Table_Columns.txt` easily accessible
- [ ] Bookmark AI tools: Gemini, ChatGPT, or Dust

---

## 🚀 Key Takeaways

1. **AI as a Discovery Tool**: Use AI to understand unknown schemas
2. **Quality Gates**: Prevent bad data with automated checks
3. **Efficiency Matters**: Know why queries are slow before optimizing
4. **Practical Skills**: Real-world scenarios from Jumia operations

---

**Prepared by:** Gustave Vernay (Avisia)  
**Date:** December 2025  
**Workshop Location:** Jumia HQ
