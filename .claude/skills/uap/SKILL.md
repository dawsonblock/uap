```markdown
# uap Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill introduces the core development patterns and workflows used in the `uap` TypeScript codebase. It covers coding conventions, file organization, and step-by-step guides for maintaining documentation and domain-specific manuscripts. Whether you're updating documentation or contributing code, this guide will help you align with the project's established practices.

## Coding Conventions

### File Naming
- **PascalCase** is used for file names.
  - Example: `MyModule.ts`, `UserProfile.ts`

### Import Style
- **Relative imports** are preferred.
  - Example:
    ```typescript
    import { UserService } from './UserService';
    ```

### Export Style
- **Named exports** are used instead of default exports.
  - Example:
    ```typescript
    // In UserService.ts
    export function getUser(id: string) { ... }
    export const USER_ROLE = 'admin';

    // In another file
    import { getUser, USER_ROLE } from './UserService';
    ```

### Commit Messages
- **Freeform style** with no strict prefixes.
- Average commit message length is about 30 characters.
  - Example: `Fix typo in documentation`

## Workflows

### Update Documentation File
**Trigger:** When someone needs to correct, clarify, or align documentation.  
**Command:** `/update-doc`

1. Edit the relevant documentation file (e.g., `README.md`, `REFERENCES.md`, `CHANGELOG.md`, or any `.md` file).
2. Make the necessary corrections or updates.
3. Commit the changes with a descriptive message.
   - Example: `Clarify setup instructions in README.md`

**Files Involved:**
- `README.md`
- `REFERENCES.md`
- `CHANGELOG.md`
- Any `*.md` file

---

### Fix or Rewrite Domain-Specific Manuscript
**Trigger:** When someone identifies errors or needs to update content in a manuscript file.  
**Command:** `/fix-manuscript`

1. Identify the manuscript file requiring changes (e.g., `uap-speculative-framework.md`, `uap-comprehensive.md`, `uap-physics-map-bridge.md`).
2. Edit the file to fix errors or rewrite content as needed.
3. Commit the changes with a message indicating the fix or rewrite.
   - Example: `Rewrite introduction in uap-comprehensive.md`

**Files Involved:**
- `uap-speculative-framework.md`
- `uap-comprehensive.md`
- `uap-physics-map-bridge.md`

## Testing Patterns

- **Test files** follow the `*.test.*` naming convention.
  - Example: `UserService.test.ts`
- **Testing framework** is not specified; check individual test files for framework usage.
- To add a test:
  1. Create a file named `ModuleName.test.ts`.
  2. Place your test code inside, following the conventions of the testing framework in use.

## Commands

| Command           | Purpose                                                      |
|-------------------|--------------------------------------------------------------|
| /update-doc       | Update or align existing documentation files                  |
| /fix-manuscript   | Fix errors or rewrite domain-specific manuscript files        |
```
