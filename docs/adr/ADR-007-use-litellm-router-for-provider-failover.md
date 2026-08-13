# ADR-007: Use LiteLLM Router for Provider Failover

## Status

Accepted

## Context

The introduction of the LLM Provider Abstraction Layer required a mechanism for managing multiple language model providers through a single interface. While Google ADK supports model configuration, the project required additional capabilities such as automatic provider failover and centralized routing without introducing provider-specific logic into individual AI agents.

The architecture required a solution that could improve reliability while keeping the implementation simple and extensible.

## Decision

LiteLLM Router was selected as the routing mechanism for the LLM Provider Abstraction Layer.

The router manages provider selection and automatically routes requests to a configured fallback provider when the primary provider is unavailable. AI agents communicate only with the provider abstraction layer and remain unaware of the underlying routing logic.

## Consequences

### Benefits

- Provides automatic provider failover.
- Improves system availability when a provider is temporarily unavailable.
- Centralizes routing logic in a single component.
- Allows new providers to be added with minimal changes to the application.
- Keeps AI agents independent of provider-specific implementation details.

### Trade-offs

- Introduces an external dependency for provider routing.
- Router configuration must be maintained as providers are added or updated.
- Debugging provider-related issues may require inspecting both the abstraction layer and the router configuration.