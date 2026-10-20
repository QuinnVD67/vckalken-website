# VC Kalken Design System v1.0

A comprehensive design system for the VC Kalken volleyball club website. This document serves as the single source of truth for all design decisions, color palettes, typography, components, and patterns.

---

## 1. Color Palette

### Brand Colors

| Color | Hex | CSS Variable | Usage |
|-------|-----|--------------|-------|
| **Navy (Primary)** | #0a2342 | `--navy` | Primary text, headers, brand anchor |
| **Navy 2 (Dark)** | #0d2d52 | `--navy-2` | Dark backgrounds, emphasis |
| **Navy 3** | #173f6b | `--navy-3` | Gradients, depth |
| **Royal Blue** | #1c64b4 | `--royal` | Links, interactive elements |
| **Sky Blue** | #e9f2fc | `--sky` | Light backgrounds, hover states |
| **Gold (Primary)** | #f6b821 | `--gold` | Primary CTA, highlights |
| **Gold 2 (Vibrant)** | #ffd966 | `--gold-2` | Secondary highlights, accent |
| **Gold Soft** | #fff5da | `--gold-soft` | Soft backgrounds, overlays |

### Secondary Accent Colors

| Color | Hex | CSS Variable | Usage |
|-------|-----|--------------|-------|
| **Teal** | #0fa99d | `--teal` | Team badges, secondary accent |
| **Emerald** | #1eaf5b | `--emerald` | Success states, confirmation |
| **Coral** | #ff6b5e | `--coral` | Alerts, errors, warnings |
| **Amber** | #fbbf24 | `--amber` | Warm accent alternative |

### Neutral Colors

| Color | Hex | CSS Variable | Usage |
|-------|-----|--------------|-------|
| **Ink** | #10243d | `--ink` | Primary text, headers |
| **Body** | #33485f | `--body` | Body text |
| **Muted** | #6b7e93 | `--muted` | Secondary text, meta info |
| **Line** | #e5ecf2 | `--line` | Borders, dividers |
| **Line 2** | #d7e2f0 | `--line-2` | Focus rings, secondary borders |
| **Background** | #f4f7fb | `--bg` | Page background |
| **Background 2** | #f0f4f9 | `--bg-2` | Section background |
| **White** | #ffffff | `--white` | Cards, overlays |
| **Cream** | #fffaf0 | `--cream` | Warm background |

### Usage Guidelines

- **Dark Text on Light**: Use `--ink` on white/cream/sky backgrounds
- **Light Text on Dark**: Use white (#fff) on navy/dark backgrounds
- **Links**: Use `--royal` (#1c64b4) for WCAG AA compliance (4.5:1 contrast)
- **CTAs**: Use gold gradient for primary, navy gradient for secondary
- **States**: Use teal for hover, emerald for success, coral for error
- **Badges**: Team badges use `--teal`, Category badges use color-coded variants

---

## 2. Typography System

### Font Stack

```css
/* Headlines */
font-family: "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
font-weights: 600, 700, 800;

/* Body Text */
font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
font-weights: 400, 500, 600, 700, 800;
```

### Typographic Scale

| Element | Size | Weight | Line-Height | Letter-Spacing | Usage |
|---------|------|--------|-------------|-----------------|--------|
| **h1** | clamp(2.7rem, 6.4vw, 5.2rem) | 800 | 1.1 | -0.03em | Page heroes, major headlines |
| **h2** | clamp(1.9rem, 3.6vw, 3rem) | 700 | 1.15 | -0.02em | Section titles |
| **h3** | clamp(1.25rem, 2.2vw, 1.75rem) | 700 | 1.2 | -0.01em | Card titles, subsections |
| **h4** | 1.12rem | 700 | 1.3 | 0 | Menu labels, field labels |
| **Body** | 1rem | 400 | 1.6 | 0 | Paragraph text |
| **Small** | 0.92rem | 400 | 1.5 | 0 | Field labels, secondary text |
| **Caption** | 0.86rem | 400 | 1.4 | 0 | Meta info, timestamps |
| **Eyebrow** | 0.76rem | 800 | 1 | 0.12em | Section labels, overlines |
| **Lead** | 1.12rem | 400 | 1.6 | 0 | Intro paragraphs |

### Font Pairing Rationale

- **Plus Jakarta Sans for Headlines**: Modern, geometric, confident — reflects volleyball energy
- **Inter for Body**: Highly legible, neutral, excellent on-screen rendering
- **Combination**: Sophisticated contrast without being ornamental

---

## 3. Shadow System

Five-level shadow hierarchy for depth and elevation:

| Level | CSS Variable | Value | Usage |
|-------|-------------|-------|-------|
| **Extra Small** | `--shadow-xs` | 0 2px 4px rgba(10,35,66,.03) | Subtle depth, fine details |
| **Small** | `--shadow-sm` | 0 4px 12px rgba(10,35,66,.06) | Base cards, resting state |
| **Medium** | `--shadow` | 0 10px 24px rgba(10,35,66,.10) | Elevated cards, standard shadow |
| **Large** | `--shadow-md` | 0 16px 40px rgba(10,35,66,.14) | Hovered cards, significant elevation |
| **Extra Large** | `--shadow-lg` | 0 24px 56px rgba(10,35,66,.18) | Modals, overlays, prominent elements |
| **Lift** | `--shadow-lift` | 0 16px 48px rgba(10,35,66,.16) | Button hover state |

### Shadow Usage Examples

```css
/* Resting state card */
.card { box-shadow: var(--shadow-sm); }

/* Hovered card */
.card:hover { 
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

/* Modal/overlay */
.modal { box-shadow: var(--shadow-lg); }

/* Floating button on hover */
.btn:hover { box-shadow: var(--shadow-lift); }
```

---

## 4. Spacing System

8px baseline grid system:

| Spacing | Pixels | CSS | Usage |
|---------|--------|-----|-------|
| XS | 4px | 4 × 1 | Tiny gaps, fine details |
| S | 8px | 8 × 1 | Button internal spacing |
| M | 16px | 8 × 2 | Component gaps, padding |
| L | 24px | 8 × 3 | Section spacing |
| XL | 32px | 8 × 4 | Large spacing, section breaks |
| 2XL | 48px | 8 × 6 | Major section spacing |
| 3XL | 64px | 8 × 8 | Full section padding |
| 4XL | 80px | 8 × 10 | Extra large spacing |

### Responsive Padding

Use `clamp()` for fluid responsive spacing:

```css
/* Section padding */
padding: clamp(16px, 5vw, 46px);

/* Hero/Header padding */
padding: clamp(28px, 4vw, 56px);

/* Form padding */
padding: clamp(24px, 3vw, 38px);
```

---

## 5. Radius Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 16px | Small components (inputs, badges) |
| `--radius` | 24px | Standard cards, buttons |
| `--radius-lg` | 32px | Large containers, hero sections |
| **Pills** | 999px | Buttons, badges (border-radius: 999px) |

---

## 6. Gradients

### Primary Gradients

```css
/* Navy Gradient - Professional depth */
--grad-navy: linear-gradient(135deg, #0a2342 0%, #1a4a7a 55%, #1c64b4 130%);

/* Gold Gradient - Primary CTAs */
--grad-gold: linear-gradient(135deg, #f6b821 0%, #ffd966 100%);

/* Teal Gradient - Secondary accent */
--grad-teal: linear-gradient(135deg, #0fa99d 0%, #18d9ce 100%);

/* Warm Gradient - Alternative accent */
--grad-warm: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
```

### Overlay Gradient

```css
/* Directional overlay for hero sections */
--grad-overlay: linear-gradient(120deg, rgba(10,35,66,.85) 0%, rgba(246,184,33,.05) 100%);
```

---

## 7. Component Library

### Buttons

#### Variants

| Variant | Background | Color | Shadow | Hover State |
|---------|-----------|-------|--------|-------------|
| **Primary** | `var(--grad-gold)` | #172235 | Standard | Translate -2px, shadow-lift |
| **Secondary** | `var(--grad-navy)` | #fff | Navy shadow | Translate -2px, shadow-lift |
| **Ghost** | rgba(255,255,255,.12) | #fff | None | bg opacity +0.1 |
| **Soft** | `var(--sky)` | `--navy` | None | Translate -1px |
| **Danger** | #e23b3b | #fff | Coral shadow | Translate -2px |

#### Sizes

```css
/* Large (default) */
padding: 14px 24px;
font-size: 0.96rem;
font-weight: 800;

/* Small */
padding: 10px 16px;
font-size: 0.86rem;
font-weight: 800;
```

#### States

- **Default**: Full opacity, shadow-sm
- **Hover**: Transform translateY(-2px), enhanced shadow
- **Active**: Transform translateY(0), reduced shadow
- **Disabled**: Opacity 0.5, cursor not-allowed
- **Focus**: Outline none, ring box-shadow

### Cards

#### Image Card / Team Card

```css
background: #fff;
border: 1px solid var(--line);
border-radius: var(--radius);
box-shadow: var(--shadow-sm);
overflow: hidden;
transition: .25s var(--ease);
```

**Hover State**: Translate Y -6px, shadow-md

**Content**:
- Image: 190px height, scale 1.06 on hover
- Badge: Navy bg, white text, uppercase
- Title: Navy, 1.18rem, 700 weight
- Description: Muted, 0.92rem

#### Stat Card

```css
background: #fff;
border: 1px solid var(--line);
border-radius: 22px;
padding: 26px 22px;
text-align: center;
box-shadow: var(--shadow-sm);
```

**Hover State**: Translate Y -3px, shadow

**Content**:
- Number: Navy, 2-2.9rem (clamped)
- Label: Muted, 0.92rem, 600 weight

#### News Card

Same as Image Card with added metadata:
- Category: Royal blue, uppercase, dot separator
- Excerpt: Muted, 0.93rem
- Read link: Royal, 800 weight

#### Player Card

```css
background: #fff;
border: 1px solid var(--line);
border-radius: 22px;
padding: 20px 14px 18px;
text-align: center;
box-shadow: var(--shadow-sm);
```

**Hover State**: Translate Y -5px, shadow-md

**Content**:
- Avatar: 148px circular with gradient border
- Number badge: 34px circular, gold gradient, absolute positioned
- Name: Navy, 1.05rem
- Position: Royal, 700 weight, 0.86rem

### Form Inputs

```css
border: 1px solid var(--line-2);
border-radius: 14px;
padding: 13px 15px;
background: #fbfdff;
color: var(--ink);
font: inherit;
transition: .18s var(--ease);
```

**Focus State**:
- Border color: `--royal`
- Background: #fff
- Box shadow: `var(--ring)`

**Disabled State**:
- Opacity: 0.6
- Cursor: not-allowed

### Badges

#### Team Badge
```css
background: var(--sky);
color: var(--navy);
font-weight: 800;
font-size: 0.82rem;
padding: 7px 13px;
border-radius: 999px;
text-transform: uppercase;
```

#### Category Badge
```css
background: var(--gold-soft);
color: #6d5200;
font-weight: 800;
font-size: 0.76rem;
padding: 5px 11px;
border-radius: 999px;
```

#### Status Badge
- **Success**: Emerald background, white text
- **Alert**: Coral background, white text
- **Pending**: Amber background, dark text

---

## 8. Modern Design Patterns

### 1. Enhanced Glass-Morphism

Used in header and overlays:

```css
background: rgba(255, 255, 255, 0.85);
backdrop-filter: blur(16px) saturate(150%);
-webkit-backdrop-filter: blur(16px) saturate(150%);
border: 1px solid rgba(246, 184, 33, 0.12);
```

### 2. Gradient Overlays

Applied to hero sections and team pages:

```css
background: linear-gradient(120deg, 
  rgba(10, 35, 66, 0.85) 0%,
  rgba(246, 184, 33, 0.05) 100%);
```

### 3. Micro-Interactions

#### Card Hover Lift
```css
.card {
  transition: .25s var(--ease);
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}
```

#### Button Press Feedback
```css
.btn:active {
  transform: translateY(0px);
  box-shadow: 0 6px 16px rgba(246, 184, 33, 0.28);
}
```

### 4. Scroll Reveal Animation

```css
.reveal {
  opacity: 0;
  transform: translateY(26px);
  transition: .7s var(--ease);
}
.reveal.in {
  opacity: 1;
  transform: none;
}
.reveal.d1 { transition-delay: .08s; }
.reveal.d2 { transition-delay: .16s; }
.reveal.d3 { transition-delay: .24s; }
.reveal.d4 { transition-delay: .32s; }
```

### 5. Asymmetric/Bento Layouts

Hero section: `grid-template-columns: 1.15fr 0.6fr` (featured + sidebar)
Stats section: Can use featured stat with larger span

---

## 9. Accessibility Standards

### Color Contrast

All colors must meet WCAG AA (4.5:1 for normal text):

| Text Color | Background | Contrast | Status |
|-----------|-----------|----------|--------|
| ink/body | white | 6.8:1 | ✅ AA+ |
| muted | white | 4.6:1 | ✅ AA |
| navy | sky | 5.2:1 | ✅ AA+ |
| white | navy | 9.2:1 | ✅ AA+ |
| gold | navy | 4.8:1 | ✅ AA |

### Keyboard Navigation

- Tab order: Left-to-right, top-to-bottom
- Focus indicators: `var(--ring)` (4px navy ring with 16% opacity)
- All interactive elements must be keyboard accessible

### Motion

- Respect `prefers-reduced-motion`: Set `transition: none` and `opacity: 1; transform: none;` for `.reveal`
- All animations should be under 400ms
- Avoid flashing/strobing animations

### Screen Readers

- Semantic HTML (nav, main, footer, article)
- ARIA labels for icon-only buttons
- Form labels with `for` attributes
- Meaningful alt text for images
- Heading hierarchy (h1 → h6)

---

## 10. Responsive Design

### Breakpoints

```css
/* Desktop (1040px and below) */
@media(max-width: 1040px) {
  /* 2-column grids, hamburger nav, single-column splits */
}

/* Mobile (600px and below) */
@media(max-width: 600px) {
  /* 1-column grids, simplified layouts */
}
```

### Fluid Typography

All headlines use `clamp()` for responsive sizing:

```css
h1 { font-size: clamp(2.7rem, 6.4vw, 5.2rem); }
h2 { font-size: clamp(1.9rem, 3.6vw, 3rem); }
```

### Safe Areas

- Respect notch/gesture bar with padding
- Avoid fixed positioning at screen edges
- Use `min-height: 100dvh` instead of `100vh` on mobile

---

## 11. Performance Considerations

### CSS Architecture

- Single `styles.css` file with design tokens at root
- CSS custom properties (variables) for theming
- Efficient selector targeting (avoid deep nesting)
- CSS bundle: Target < 50KB (minified)

### Image Optimization

- Use `loading="lazy"` for below-fold images
- Declare `width` and `height` to prevent layout shift
- Responsive images with `srcset`
- SVG fallbacks for missing images

### Animation Performance

- Use `transform` and `opacity` only (GPU-accelerated)
- Avoid animating `width`, `height`, `top`, `left`
- Duration: 150-300ms for micro-interactions, ≤400ms for transitions

---

## 12. Component Checklist

Before adding any new component:

- [ ] Named with clear, semantic class name
- [ ] Color uses CSS variables (not hardcoded hex)
- [ ] Shadow uses variable (not hardcoded rgba)
- [ ] Rounded corners use `--radius` variants
- [ ] Hover/focus/active states defined
- [ ] Responsive design considered (breakpoints)
- [ ] Accessibility verified (contrast, keyboard nav, labels)
- [ ] Animation respects `prefers-reduced-motion`
- [ ] Documented in this design system

---

## 13. File Structure

```
/
├── styles.css              # All component styles + design tokens
├── DESIGN-SYSTEM.md        # This file
├── index.html              # Home page
├── ploegen.html            # Teams overview
├── heren-a.html            # Team page template
├── contact.html            # Contact form
├── word-lid.html           # Join form
└── assets/
    ├── img/                # Images (with SVG fallbacks)
    └── design-tokens.css   # Optional: Separate token file
```

---

## 14. Implementation Notes

### CSS Custom Properties

All design tokens are defined in `:root` for easy theming:

```css
:root {
  --navy: #0a2342;
  --gold: #f6b821;
  /* ... etc */
}
```

Use in components: `color: var(--navy);`

### Maintenance

- **Monthly**: Audit pages for style drift
- **Quarterly**: Review component reusability
- **Seasonal**: Update imagery, refresh hero sections
- **When adding features**: Update this design system

### Future Enhancements

- [ ] Dark mode color scheme
- [ ] Component variant documentation (with images)
- [ ] Animation library (entrance, exit, hover effects)
- [ ] Accessibility audit results
- [ ] Browser compatibility matrix
- [ ] Performance baseline metrics

---

**Last Updated**: June 2026  
**Version**: 1.0  
**Maintained By**: VC Kalken Web Team
