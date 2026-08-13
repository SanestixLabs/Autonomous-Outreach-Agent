# ADR-006: Introduce an LLM Provider Abstraction Layer

## Status

Accepted

## Context

Initially, AI agents were configured to communicate directly with a specific language model provider. This tightly coupled the agent implementations to a single provider, making it difficult to switch providers, introduce new providers, or implement provider-specific features such as automatic failover.

The project required a more flexible design that would allow AI agents to remain independent of the underlying LLM provider while supporting future extensibility.

## Decision

An LLM Provider Abstraction Layer was introduced as the interface between AI agents and language model providers.

Instead of referencing a specific provider directly, each AI agent requests a model through the provider abstraction layer. The abstraction layer is responsible for provider selection and exposing a consistent interface to all AI agents.

This design allows provider-specific logic to remain centralized without requiring changes to individual agent implementations.

## Consequences

### Benefits

- Decouples AI agents from individual LLM providers.
- Simplifies switching between supported providers.
- Centralizes provider configuration and management.
- Makes it easier to introduce new providers in the future.
- Provides a foundation for implementing features such as automatic provider failover.

### Trade-offs

- Introduces an additional abstraction layer that must be maintained.
- Provider-specific features may require updates to the abstraction layer.
- Debugging provider-related issues may require tracing requests through the abstraction layer.