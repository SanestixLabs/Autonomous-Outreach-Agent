# ADR-004: Introduce a Memory Service

## Status

Accepted

## Context

The initial implementation processed each lead independently and did not retain any information after the AI pipeline completed. As a result, the system could not recognize previously processed leads, reuse AI outputs, or support intelligent follow-up workflows.

To evolve the project toward a production-ready architecture, the system required a centralized mechanism for storing lead information and customer interaction history.

## Decision

A dedicated Memory Service was introduced to act as the central repository for lead-related information.

The Memory Service is responsible for storing customer history, lead state, previous interactions, and cached AI outputs. Supporting services can retrieve and update this information to make workflow decisions and reduce unnecessary AI processing.

## Consequences

### Benefits

- Enables persistent lead and customer history.
- Supports follow-up workflows using previous interactions.
- Reduces unnecessary AI computation by reusing cached outputs.
- Establishes a single source of truth for lead state.
- Provides a foundation for future workflow orchestration.

### Trade-offs

- Introduces additional complexity for state management.
- Requires synchronization between services accessing shared data.
- Future implementations will require persistent storage to retain information across application restarts.