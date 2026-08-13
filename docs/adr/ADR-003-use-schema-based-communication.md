# ADR-003: Use Structured Schema-Based Communication Between Agents

## Status

Accepted

## Context

The Autonomous Outreach Agent consists of multiple AI agents that exchange information throughout the outreach pipeline. Relying on unstructured natural language outputs between agents would make the system difficult to validate, increase the likelihood of inconsistent data, and complicate downstream processing.

The project required a reliable and consistent method for passing information between agents while ensuring outputs could be validated before progressing through the pipeline.

## Decision

The system uses structured schema-based communication between AI agents.

Each agent produces outputs conforming to predefined Pydantic schemas, which are consumed by downstream agents and supporting services.

This approach standardizes the data exchanged throughout the pipeline and enables automated validation before subsequent processing.

## Consequences

### Benefits

- Provides a consistent data format across the entire pipeline.
- Simplifies communication between agents.
- Enables schema validation before downstream processing.
- Reduces errors caused by inconsistent or malformed outputs.
- Makes the system easier to maintain and extend as new agents are introduced.

### Trade-offs

- Schema definitions must be maintained as the system evolves.
- Changes to shared schemas may require updates to multiple agents.
- Structured outputs introduce additional development effort compared to passing free-form text.