---
name: skill-web-architecture
description: Full-stack web architectural standards, module boundaries, and API contract design. MUST ACTIVATE when designing full-stack web application structure, choosing stack boundaries, or structuring API interactions between client and server.
---

# Overview

Web architecture decisions shape the foundation of a robust, scalable, and accessible application. This skill provides a framework for frontend component architecture and backend API design. Use these guidelines when designing new web features, making technology choices, or defining module boundaries.

# When to Use
- Designing new web features
- Component architecture decisions
- API design and specification
- Technology stack selection
- Performance optimization planning
- Accessibility compliance checks

# When NOT to Use
- Pure visual art direction, typography pairings, and aesthetics (use `skill-creative-design`)
- Motion animation engineering, Subgrid/Bento implementation, or UI component suites (use `skill-design-engineering` / `skill-frontend-architect`)
- Pure backend business logic (use `skill-backend-architect` if available)

# Component Architecture

Adhere to these principles when designing UI components:
- **Modular Composition**: Build complex UIs from small, reusable, and independent building blocks.
- **Clear Props/Interface Contracts**: Define strict inputs and outputs for every component using typed interfaces (e.g., TypeScript).
- **UI vs. Business Logic Separation**: Keep rendering logic separate from data fetching and state mutation. Use custom hooks or container components.
- **State Management Boundaries**: Deliberately decide between local component state and global application state. Avoid unnecessary global state.
- **Controlled vs. Uncontrolled Components**: Be explicit about who owns the state. Prefer controlled components for complex forms.
- **Render Optimization Patterns**: Use memoization (e.g., `React.memo`, `useMemo`) judiciously to prevent unnecessary re-renders.

# Accessibility Standards

WCAG 2.1 / 2.2 AA compliance is NON-NEGOTIABLE. Ensure the following:
- **Full Keyboard Navigation**: Every interactive element must be reachable and usable via keyboard alone.
- **Target Size**: Minimum interactive target area (24x24px minimum, 44x44px recommended).
- **Screen-Reader ARIA**: Use appropriate ARIA roles and labels for non-native interactive elements.
- **Color Contrast**: Maintain a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text (or APCA equivalent).
- **Focus Management**: Provide clearly visible focus indicators. Manage focus appropriately during state changes (e.g., modals).
- **Semantic HTML**: Avoid "div soup". Use semantic tags like `<nav>`, `<main>`, `<article>`, `<button>`.
- **Skip Navigation Links**: Provide mechanisms to bypass repetitive content blocks.

# Performance & Core Web Vitals

Design for performance from the start:
- **LCP (Largest Contentful Paint)**: Target < 2.5s. Optimize hero image loading and server response times.
- **INP (Interaction to Next Paint)**: Target < 200ms. Keep the main thread unblocked.
- **CLS (Cumulative Layout Shift)**: Target < 0.1. Reserve space for dynamic content (images, ads).
- **Bundle Size Budgets**: Implement code splitting and lazy loading for routes and heavy components.
- **Image Optimization**: Serve modern formats (WebP/AVIF), use lazy loading for below-the-fold images, and provide `srcset` for responsive images.
- **Critical Rendering Path**: Inline critical CSS and defer non-essential scripts.

# Contract-First API Design

APIs must be designed with strict contracts before implementation:
- **Design Before Code**: Define schemas, parameters, and error types explicitly BEFORE writing endpoint logic.
- **Hyrum's Law**: Assume users will depend on every observable behavior. Explicitly specify public contracts and aggressively hide implementation details.
- **Consistent Error Semantics**: Use structured error payloads and predictable HTTP status codes across all endpoints.
- **Versioning Strategy**: Establish a clear versioning strategy (e.g., URL path vs. header) from day one.

# Boundary Validation

Never trust inputs at system boundaries:
- **Runtime Validation**: Use tools like Zod or JSON Schema at interface boundaries to guarantee data shape.
- **Input Sanitization**: Sanitize all data at API entry points to prevent injection attacks.
- **Type Narrowing**: Use type guards at data boundaries to ensure type safety deeper in the application logic.

# Anti-Rationalization Table

| Agent Excuse | BLOCKED Rebuttal |
|--------------|------------------|
| "The user didn't ask for accessibility" | **BLOCKED:** WCAG 2.1 AA is a default requirement for all web interfaces. |
| "We can optimize performance later" | **BLOCKED:** Architecture decisions now determine the performance ceiling later. Optimize structural performance early. |
| "I'll define the API as I build" | **BLOCKED:** Contract-first is mandatory. Define schemas and types before implementation. |
| "This component is too simple to need a props interface" | **BLOCKED:** Every component, no matter how simple, gets a explicitly typed interface. |
| "SSR isn't needed for this page" | **BLOCKED:** Evaluate LCP impact and SEO requirements before deciding against SSR. |
| "The existing API pattern doesn't use validation" | **BLOCKED:** Don't propagate missing validation. Introduce runtime validation at boundaries for new code. |

# Red Flags
- Committing UI components without defined types/interfaces.
- Missing keyboard navigation support on interactive elements.
- Implementing an API without a prior schema definition.
- Trusting client data without server-side validation.

# Verification Gates
- [ ] Is the UI logic separated from the business logic?
- [ ] Does the UI meet WCAG 2.1 AA accessibility standards?
- [ ] Are performance budgets and Web Vitals explicitly addressed?
- [ ] Is the API contract defined and validated at runtime?
