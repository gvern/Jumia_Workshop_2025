# Risk Matrix Template

Use this template for Risk Storming sessions to identify potential risks and define appropriate guardrails.

| Risk Scenario | Impact (1-5) | Proposed Guardrail (Hard Rule or AI?) |
| :--- | :--- | :--- |
| Selling items at $0 | 5 (Revenue Loss) | Hard Rule (If price <= 0, Stop) |
| Chatbot hallucinates stock | 3 (Customer Frustration) | System Prompt Constraint |
| | | |
| | | |
| | | |

## Instructions

1. **Risk Scenario**: Describe what could go wrong in your AI/automation workflow
2. **Impact (1-5)**: Rate the business impact if this risk materializes (1=Low, 5=Critical)
3. **Proposed Guardrail**: Define whether you need a hard-coded validation rule or an AI-based constraint

## Examples of Guardrails

- **Hard Rules**: Price validation, data format checks, required field validation
- **AI-Based**: Content moderation, sentiment analysis, contextual relevance checks
