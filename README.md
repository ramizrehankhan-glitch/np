# AI Guardian landing page (from Figma)

Static HTML/CSS build of the Figma frame **"Design | AI Guardian - v2"**
([Figma file](https://www.figma.com/design/AqFuDxdDNrvH5SziHe3g15/Untitled?node-id=1-6200), node `1:6200`, 1760px wide).
Font sizes, weights, line heights, letter spacing, colors, radii, shadows and spacing are taken
from Figma's design data. The page is exact at a 1760px-wide viewport and still works down to about 1280px.

Open `index.html` in a browser. It needs no server, no build step and no external requests. The fonts are self-hosted in `fonts/`.

## Structure

```
index.html          generated — do not edit by hand
build.py            python3 build.py → regenerates index.html from sections/ + css/
sections/NN-*.html  one file per page section, in page order
css/base.css        reset, page column, shared .eyebrow pill and .btn buttons
css/fonts.css       @font-face rules for Plus Jakarta Sans, Inter, Roboto, Cousine
css/NN-*.css        styles for each section, scoped under its section class
assets/             icons (SVG) and images (PNG), prefixed with their section number
fonts/              woff2 files (latin + latin-ext subsets)
```

To change a section, edit `sections/NN-*.html` or `css/NN-*.css`, then run `python3 build.py`.

## Section status

| #  | Section | Figma node | Status |
|----|---------|-----------|--------|
| 01 | Hero | 1:6238 | ✅ built |
| 02 | Product walkthrough | 1:6262 | ✅ built |
| 03 | The problem | 1:6321 | ⏳ not built |
| 04 | Shadow AI | 1:6331 | ⏳ not built |
| 05 | How it works | 1:6467 | ⏳ not built |
| 06 | Capabilities at a glance | 1:6580 | ✅ built |
| 07 | AI spend optimization | 1:6670 | ✅ built |
| 08 | Real-time guardrails | 1:6849 | ⏳ not built |
| 09 | The AI Guardian approach | 1:6906 | ✅ built |
| 10 | Multi-agent work | 1:6919 | ✅ built |
| 11 | Hierarchical governance | 1:6960 | ⏳ not built |
| 12 | Adopt it in stages | 1:7077 | ✅ built |
| 13 | Investment / pricing | 1:7136 | ✅ built |
| 14 | Implementation approach | 1:7190 | ⏳ not built |
| 15 | Use cases (carousel) | 1:7279 | ✅ built |
| 16 | Competitive position | 1:7369 | ⏳ not built |
| 17 | Gaps in native Azure governance (table) | 1:7473 | ✅ built |
| 18 | FAQ (accordion) | 1:7615 | ✅ built |

Sections marked ⏳ were not built because the account hit the Figma MCP **Starter-plan tool-call
limit** partway through the conversion. They were left out rather than guessed. Once Figma
access is available again, each one needs a `get_design_context` call on its node to be built the
same way. Because every section is its own file, each one can be added without touching the others.

## Known gaps in the built sections

- **Asset fidelity.** The figma.com asset URLs are blocked by the network policy of the build
  environment. The hero's images and icons were exported directly from Figma. In the other sections:
  - Most Font Awesome icons are the matching glyphs from Font Awesome 6 Free (Solid), stored as
    local SVGs.
  - A few images were cropped from Figma preview renders, so they are slightly soft. These are
    the walkthrough screen (`02-walkthrough-screen.png`), the Microsoft visual
    (`07-microsoft-visual.png`), the approach photo (`09-approach-photo.png`) and the multi-agent
    mockup (`10-multi-agent-mockup.png`).
  - A few small SVGs were redrawn by hand to match the design: the browser tab controls in 02, the
    carousel arrows in 06, the check icon and logo in 17, and the chevrons in 18.
  - Re-exporting these from Figma will make them exact.
- **Placeholder links.** The design has no booking form or destination URLs. The "Book a demo"
  style buttons point to `#book-demo`, and "View Microsoft governance guidance" points to
  `#microsoft-guidance`. Replace these with the real URLs.
- **FAQ.** Only the first question has answer text in the Figma file. The other questions open
  but show no answer until copy is added.
- **Carousels.** Sections 06 and 15 show "01 / 04" in Figma but contain only three cards. Section
  15's pager counts the real cards. Section 06 has no hidden cards to page to.
