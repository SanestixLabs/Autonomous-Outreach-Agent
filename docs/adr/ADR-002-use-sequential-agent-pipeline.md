# ADR-002: Use a Sequential AI Agent Pipeline

## Status

Accepted

## Context

The Autonomous Outreach Agent consists of multiple AI agents responsible for different stages of the B2B outreach process. Each stage depends on information produced by previous stages. For example, lead qualification requires the structured output of the company analysis, while service recommendation and personalized email generation depend on the results of earlier agents.

The project required a workflow that ensured data was generated, validated, and passed between agents in a predictable and consistent manner.

## Decision

The system uses a sequential AI agent pipeline in which agents execute in a predefined order.

The execution flow is:

1. Company Analysis Agent
2. Lead Qualification Agent
3. Service Recommendation Agent
4. Personalized Email Agent

Each agent consumes the structured output produced by the previous stage before continuing the workflow.

## Consequences

### Benefits

- Ensures each agent has the required context before execution.
- Produces deterministic and predictable workflow execution.
- Simplifies debugging by isolating failures to a specific stage.
- Enables validation between pipeline stages.
- Supports future workflow extensions without changing individual agent responsibilities.

### Trade-offs

- Agents cannot execute in parallel.
- Overall execution time depends on the completion of previous stages.
- Changes to the execution order require orchestration updates.