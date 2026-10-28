## Web Application Rules (Additive if project uses web frontend)

### Frontend Code Quality
- HTML: 2-space indent, lowercase tags, self-closing void elements (`<br />`, `<img />`)
- CSS: 4-space indent, kebab-case class names, no `!important` without justification
- JavaScript/TypeScript: Follow existing project style (ESLint/Prettier config if present)
- No inline styles or event handlers in HTML — use separate JS/CSS files

### Security (Web-Specific)
- Validate and sanitize all user input on the backend, not just frontend
- Use HTTPS for production; HTTP acceptable only for localhost development
- Set appropriate CORS headers if serving to multiple origins
- Escape dynamic content in HTML templates to prevent XSS

### Testing Strategy
- Frontend: Manual testing via browser unless project has established E2E framework
- Integration: Verify backend serves frontend correctly at expected endpoints

### Dependency Management
- JavaScript dependencies: npm/pip packages listed in requirements; no bundler unless required
- Pin major versions for reproducibility

### Paired Documentation
- `web/index.html` → documented within main application doc (`docs/src/<app>.md`)
- Complex frontend components → separate docs in `docs/guides/frontend-<component>.md`

### File Structure
```
repo-root/
├── www/                # Frontend assets
│   ├── index.html      # Main page
│   ├── css/            # Stylesheets
│   └── js/             # JavaScript modules
```

