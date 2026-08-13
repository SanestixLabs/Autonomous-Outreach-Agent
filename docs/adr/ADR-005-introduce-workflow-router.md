# ADR-005: Introduce a Workflow Router

## Status

Accepted

## Context

The original architecture executed the same sequential AI pipeline for every lead regardless of its current state. As the project evolved, it became clear that different lead states require different workflows. For example, a new lead should pass through the complete AI pipeline, while an existing lead that requires a follow-up should reuse previous AI outputs and generate only a follow-up email.

The system required a mechanism to determine the appropriate workflow for each lead instead of always executing the same sequence of agents.

## Decision

A Workflow Router was introduced to select the appropriate workflow based on the lead's current state.

The router receives the lead state from upstream services and determines which workflow should be executed. This enables the system to support multiple workflow paths while keeping workflow selection separate from the implementation of individual AI agents.

## Consequences

### Benefits

- Enables state-driven workflow execution.
- Prevents unnecessary execution of the complete AI pipeline.
- Supports specialized workflows such as new lead processing and follow-up outreach.
- Improves extensibility by allowing new workflows to be added without modifying existing agents.
- Separates workflow selection from business logic implemented within AI agents.

### Trade-offs

- Introduces additional routing logic into the system.
- Requires consistent lead state information to make routing decisions.
- Future workflows will require maintenance as the number of supported lead states grows.