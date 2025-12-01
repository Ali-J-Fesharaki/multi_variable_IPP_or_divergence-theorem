# Divergence Theorem = Integration by Parts in 3D

A Manim animation explaining the beautiful connection between the Divergence Theorem and Integration by Parts in higher dimensions.

## Overview

This project creates an educational YouTube-style animation that demonstrates how the Divergence Theorem is essentially integration by parts generalized to multiple dimensions and vector fields.

## Scenes

The animation consists of 7 scenes:

1. **Scene 1 - The 1D Analogy**: Shows integration by parts on a number line with boundary terms at endpoints
2. **Scene 2 - Replace Interval with Region**: Transforms from a 1D line to a 3D region with a boundary surface
3. **Scene 3 - Functions Become Fields**: Demonstrates how scalar functions become color fields and vector functions become arrow fields
4. **Scene 4 - Multivariable Integration-by-Parts**: Presents the Gauss-Green identity with animated derivative swapping
5. **Scene 5 - Divergence Theorem**: Shows how setting u=1 simplifies to the Divergence Theorem
6. **Scene 6 - Intuition Animation**: Visualizes divergence inside a region and flux through the boundary
7. **Scene 7 - Summary**: Split-screen comparison of 1D and 3D cases

## Installation

### Prerequisites

1. **Python 3.8+**
2. **System dependencies** (Ubuntu/Debian):
   ```bash
   sudo apt-get install libpango1.0-dev libcairo2-dev ffmpeg
   sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended
   ```

3. **Manim**:
   ```bash
   pip install manim
   ```

## Usage

### Render Individual Scenes

```bash
# Low quality preview (fastest, good for testing)
manim -pql divergence_theorem_animation.py Scene1_1DAnalogy
manim -pql divergence_theorem_animation.py Scene2_ReplaceInterval
manim -pql divergence_theorem_animation.py Scene3_FunctionsToFields
manim -pql divergence_theorem_animation.py Scene4_MultivariableIPP
manim -pql divergence_theorem_animation.py Scene5_DivergenceTheorem
manim -pql divergence_theorem_animation.py Scene6_Intuition
manim -pql divergence_theorem_animation.py Scene7_Summary

# Medium quality
manim -pqm divergence_theorem_animation.py Scene1_1DAnalogy

# High quality (for final render)
manim -pqh divergence_theorem_animation.py Scene1_1DAnalogy

# 4K quality (best for YouTube, slowest)
manim -qk divergence_theorem_animation.py Scene1_1DAnalogy
```

### Render Intro Animation

```bash
manim -pql divergence_theorem_animation.py DivergenceTheoremAnimation
```

### Output Formats

```bash
# MP4 video (default)
manim -pql divergence_theorem_animation.py Scene1_1DAnalogy

# GIF
manim -ql --format gif divergence_theorem_animation.py Scene1_1DAnalogy
```

### Output Location

Rendered files are saved to:
```
media/videos/divergence_theorem_animation/{quality}/
```

## Mathematical Content

### The Key Insight

**1D Integration by Parts:**
$$\int_a^b u'(x)v(x)\, dx = [u(x)v(x)]_a^b - \int_a^b u(x)v'(x)\, dx$$

**Multivariable Integration by Parts (Gauss-Green Identity):**
$$\int_\Omega \nabla u \cdot \vec{v}\, dV = \int_{\partial\Omega} u(\vec{v} \cdot \hat{n})\, dS - \int_\Omega u(\nabla \cdot \vec{v})\, dV$$

**The Divergence Theorem** (when u = 1):
$$\iiint_\Omega \nabla \cdot \vec{F}\, dV = \iint_{\partial\Omega} \vec{F} \cdot \hat{n}\, dS$$

## Creating a Full YouTube Video

1. Render all scenes in high quality:
   ```bash
   for scene in Scene1_1DAnalogy Scene2_ReplaceInterval Scene3_FunctionsToFields Scene4_MultivariableIPP Scene5_DivergenceTheorem Scene6_Intuition Scene7_Summary; do
       manim -qh divergence_theorem_animation.py $scene
   done
   ```

2. Combine the rendered videos using video editing software (e.g., DaVinci Resolve, Adobe Premiere, or FFmpeg)

3. Add narration audio to match the visual content

## License

MIT License