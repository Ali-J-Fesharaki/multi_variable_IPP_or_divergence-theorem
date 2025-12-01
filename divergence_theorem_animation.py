"""
Divergence Theorem = Integration by Parts in 3D
A Manim animation explaining the connection between the Divergence Theorem
and Integration by Parts in higher dimensions.

To render the full animation:
    manim -pql divergence_theorem_animation.py DivergenceTheoremAnimation

To render individual scenes:
    manim -pql divergence_theorem_animation.py Scene1_1DAnalogy
    manim -pql divergence_theorem_animation.py Scene2_ReplaceInterval
    manim -pql divergence_theorem_animation.py Scene3_FunctionsToFields
    manim -pql divergence_theorem_animation.py Scene4_MultivariableIPP
    manim -pql divergence_theorem_animation.py Scene5_DivergenceTheorem
    manim -pql divergence_theorem_animation.py Scene6_Intuition
    manim -pql divergence_theorem_animation.py Scene7_Summary
"""

from manim import (
    Scene, ThreeDScene,
    MathTex, Text, VGroup,
    NumberLine, ThreeDAxes, Surface, Arrow, Arrow3D,
    Circle, Dot, Line,
    FadeIn, FadeOut, Write, Create, ReplacementTransform, Indicate,
    LEFT, RIGHT, UP, DOWN, ORIGIN, PI, TAU, UL,
    WHITE, YELLOW, BLUE, GREEN, RED, PURPLE, GOLD, TEAL,
    DEGREES, rate_functions,
    SurroundingRectangle, CurvedArrow, ParametricFunction,
)
import numpy as np


# Color constants for 3D scenes
BLUE_D = "#1C758A"
BLUE_E = "#29ABCA"


class Scene1_1DAnalogy(Scene):
    """Scene 1: The 1D Analogy - Integration by Parts on a number line."""
    
    def construct(self):
        # Title
        title = Text("Scene 1: The 1D Analogy", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create number line from a to b
        number_line = NumberLine(
            x_range=[0, 5, 1],
            length=8,
            include_numbers=False,
            include_tip=True
        ).shift(DOWN * 0.5)
        
        # Labels a and b
        a_label = MathTex("a").next_to(number_line.n2p(0.5), DOWN)
        b_label = MathTex("b").next_to(number_line.n2p(4.5), DOWN)
        
        # Markers for a and b
        a_dot = Dot(number_line.n2p(0.5), color=YELLOW)
        b_dot = Dot(number_line.n2p(4.5), color=YELLOW)
        
        self.play(Create(number_line), FadeIn(a_label, b_label, a_dot, b_dot))
        self.wait(0.5)
        
        # Draw u(x) as a curve
        def u_func(x):
            return 0.3 * np.sin(2 * x) + 1
        
        u_curve = ParametricFunction(
            lambda t: np.array([
                number_line.n2p(t)[0],
                u_func(t) + number_line.n2p(t)[1],
                0
            ]),
            t_range=[0.5, 4.5],
            color=BLUE
        )
        u_label = MathTex("u(x)", color=BLUE).next_to(u_curve, UP).shift(LEFT)
        
        self.play(Create(u_curve), Write(u_label))
        self.wait(0.5)
        
        # Draw v(x) as arrows along the line
        arrows = VGroup()
        for x_val in np.linspace(0.8, 4.2, 8):
            point = number_line.n2p(x_val)
            v_val = 0.2 + 0.1 * np.cos(x_val)
            arrow = Arrow(
                start=point + DOWN * 0.3,
                end=point + UP * v_val,
                color=GREEN,
                buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.3
            )
            arrows.add(arrow)
        
        v_label = MathTex("v(x)", color=GREEN).next_to(arrows, DOWN).shift(DOWN * 0.3)
        
        self.play(Create(arrows), Write(v_label))
        self.wait(0.5)
        
        # Narration text
        narration = Text(
            "Integration by parts moves a derivative\nfrom one function to another...",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1)
        
        # Clear for formula
        self.play(
            FadeOut(narration),
            u_curve.animate.scale(0.5).to_edge(LEFT).shift(UP * 2),
            arrows.animate.scale(0.5).to_edge(LEFT).shift(UP),
            u_label.animate.scale(0.7).to_edge(LEFT).shift(UP * 2.5),
            v_label.animate.scale(0.7).to_edge(LEFT).shift(UP * 0.5),
        )
        
        # Integration by parts formula
        formula_lhs = MathTex(
            r"\int_a^b", r"u'(x)", r"v(x)", r"\, dx"
        ).shift(UP * 0.5)
        formula_lhs[1].set_color(BLUE)
        formula_lhs[2].set_color(GREEN)
        
        self.play(Write(formula_lhs))
        self.wait(0.5)
        
        # Transform to right-hand side
        equals = MathTex("=").next_to(formula_lhs, RIGHT)
        
        formula_rhs = MathTex(
            r"u(b)v(b)", r"-", r"u(a)v(a)", r"-", r"\int_a^b", r"u(x)", r"v'(x)", r"\, dx"
        ).next_to(equals, RIGHT)
        formula_rhs[0].set_color(YELLOW)
        formula_rhs[2].set_color(YELLOW)
        formula_rhs[5].set_color(BLUE)
        formula_rhs[6].set_color(GREEN)
        
        self.play(Write(equals), Write(formula_rhs))
        self.wait(0.5)
        
        # Highlight boundary terms
        boundary_box = SurroundingRectangle(
            VGroup(formula_rhs[0], formula_rhs[1], formula_rhs[2]),
            color=YELLOW,
            buff=0.1
        )
        boundary_label = Text("Boundary Terms", font_size=20, color=YELLOW).next_to(boundary_box, UP)
        
        self.play(Create(boundary_box), Write(boundary_label))
        self.wait(0.5)
        
        # Highlight endpoints on number line
        self.play(
            a_dot.animate.scale(2).set_color(YELLOW),
            b_dot.animate.scale(2).set_color(YELLOW),
            Indicate(a_dot),
            Indicate(b_dot)
        )
        self.wait(0.5)
        
        # Final narration
        final_text = Text(
            "...but at a cost: a boundary term at the endpoints!",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)


class Scene2_ReplaceInterval(ThreeDScene):
    """Scene 2: Replace the Interval With a Region."""
    
    def construct(self):
        # Start with the line
        title = Text("Scene 2: From Line to Region", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # 1D line with endpoints
        line = Line(LEFT * 3, RIGHT * 3, color=WHITE, stroke_width=4)
        a_dot = Dot(LEFT * 3, color=YELLOW).scale(1.5)
        b_dot = Dot(RIGHT * 3, color=YELLOW).scale(1.5)
        a_label = MathTex("a").next_to(a_dot, DOWN)
        b_label = MathTex("b").next_to(b_dot, DOWN)
        
        line_group = VGroup(line, a_dot, b_dot, a_label, b_label)
        
        self.play(Create(line), FadeIn(a_dot, b_dot, a_label, b_label))
        self.wait(0.5)
        
        # Narration
        narration1 = Text(
            "What if instead of a line with two endpoints...",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration1)
        self.play(Write(narration1))
        self.wait(1)
        
        # Transition to 2D blob
        self.play(FadeOut(narration1))
        
        # Create a 2D blob (ellipse as approximation)
        blob_2d = Circle(radius=2, color=BLUE, fill_opacity=0.3).scale([1.3, 0.8, 1])
        
        self.play(
            ReplacementTransform(line_group, blob_2d)
        )
        self.wait(0.5)
        
        narration2 = Text(
            "...we use a whole region with a boundary all around it?",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration2)
        self.play(Write(narration2))
        self.wait(1)
        
        # Highlight the boundary
        boundary_highlight = blob_2d.copy().set_stroke(YELLOW, width=6).set_fill(opacity=0)
        
        self.play(Create(boundary_highlight))
        
        boundary_label = Text("Boundary", font_size=24, color=YELLOW)
        boundary_label.next_to(blob_2d, RIGHT)
        self.add_fixed_in_frame_mobjects(boundary_label)
        self.play(Write(boundary_label))
        self.wait(1)
        
        # Transition to 3D
        self.play(FadeOut(narration2, boundary_label))
        self.remove_fixed_in_frame_mobjects(narration2, boundary_label)
        
        # Move camera to 3D view
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)
        
        # Create 3D blob (sphere-like surface)
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u) * np.sin(v),
                1.2 * np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(24, 24),
            fill_opacity=0.5,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_color=WHITE,
            stroke_width=0.5
        )
        
        # Fade out 2D and show 3D
        self.play(
            FadeOut(blob_2d, boundary_highlight),
            FadeIn(sphere)
        )
        self.wait(0.5)
        
        # Create boundary surface highlight
        boundary_surface = Surface(
            lambda u, v: np.array([
                1.55 * np.cos(u) * np.sin(v),
                1.55 * np.sin(u) * np.sin(v),
                1.25 * np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(24, 24),
            fill_opacity=0.3,
            checkerboard_colors=[YELLOW, GOLD],
            stroke_color=YELLOW,
            stroke_width=1
        )
        
        narration3 = Text(
            "The surface of the blob is the boundary!",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration3)
        self.play(Write(narration3), FadeIn(boundary_surface))
        
        # Rotate to show 3D
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        self.wait(1)


class Scene3_FunctionsToFields(ThreeDScene):
    """Scene 3: Functions Become Fields."""
    
    def construct(self):
        title = Text("Scene 3: Functions Become Fields", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Set up 3D camera
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        # Create axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            z_length=4
        )
        
        self.play(Create(axes))
        self.wait(0.5)
        
        # Narration about scalar function
        narration1 = Text(
            "Scalar function u becomes a color field...",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration1)
        self.play(Write(narration1))
        
        # Create a scalar field visualization as colored surface
        def scalar_field_surface(u, v):
            x = 2 * np.cos(u) * np.sin(v)
            y = 2 * np.sin(u) * np.sin(v)
            z = 1.5 * np.cos(v)
            return np.array([x, y, z])
        
        scalar_surface = Surface(
            scalar_field_surface,
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(24, 24),
            fill_opacity=0.7,
            checkerboard_colors=[PURPLE, TEAL],
            stroke_width=0.5
        )
        
        u_label = MathTex("u", color=PURPLE, font_size=48)
        u_label.to_corner(UL).shift(DOWN)
        self.add_fixed_in_frame_mobjects(u_label)
        
        self.play(FadeIn(scalar_surface), Write(u_label))
        self.wait(1)
        
        self.play(FadeOut(narration1))
        self.remove_fixed_in_frame_mobjects(narration1)
        
        # Narration about vector field
        narration2 = Text(
            "Vector function v becomes arrows!",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration2)
        self.play(Write(narration2))
        
        # Create vector field arrows
        arrows = VGroup()
        for theta in np.linspace(0, TAU, 8, endpoint=False):
            for phi in np.linspace(0.3, PI - 0.3, 4):
                x = 2.2 * np.cos(theta) * np.sin(phi)
                y = 2.2 * np.sin(theta) * np.sin(phi)
                z = 1.7 * np.cos(phi)
                start = np.array([x, y, z])
                # Radial outward direction
                direction = start / np.linalg.norm(start) * 0.4
                arrow = Arrow3D(
                    start=start,
                    end=start + direction,
                    color=GREEN,
                    thickness=0.02,
                    height=0.1,
                    base_radius=0.04
                )
                arrows.add(arrow)
        
        v_label = MathTex(r"\vec{v}", color=GREEN, font_size=48)
        v_label.next_to(u_label, DOWN)
        self.add_fixed_in_frame_mobjects(v_label)
        
        self.play(Create(arrows), Write(v_label))
        self.wait(1)
        
        self.play(FadeOut(narration2))
        self.remove_fixed_in_frame_mobjects(narration2)
        
        # Final narration
        narration3 = Text(
            "Integration by parts becomes...",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration3)
        self.play(Write(narration3))
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        self.wait(1)


class Scene4_MultivariableIPP(Scene):
    """Scene 4: Show the Multivariable Integration-by-Parts Formula."""
    
    def construct(self):
        title = Text("Scene 4: Multivariable Integration by Parts", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # The Gauss-Green identity
        formula = MathTex(
            r"\int_\Omega",
            r"\nabla u",
            r"\cdot",
            r"\vec{v}",
            r"\, dV",
            r"=",
            r"\int_{\partial\Omega}",
            r"u",
            r"(",
            r"\vec{v}",
            r"\cdot",
            r"\hat{n}",
            r")",
            r"\, dS",
            r"-",
            r"\int_\Omega",
            r"u",
            r"(",
            r"\nabla \cdot",
            r"\vec{v}",
            r")",
            r"\, dV",
            font_size=40
        )
        
        # Color the terms
        formula[1].set_color(BLUE)  # nabla u
        formula[3].set_color(GREEN)  # v on LHS
        formula[7].set_color(BLUE)  # u in boundary term
        formula[9].set_color(GREEN)  # v in boundary term
        formula[11].set_color(YELLOW)  # n
        formula[16].set_color(BLUE)  # u in volume term
        formula[18].set_color(GREEN)  # nabla dot
        formula[19].set_color(GREEN)  # v on RHS
        
        self.play(Write(formula))
        self.wait(1)
        
        # Narration
        narration = Text(
            "This is integration by parts... in higher dimensions!",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(1)
        
        # Highlight the derivative swap animation
        # Create boxes around the derivative terms
        lhs_deriv_box = SurroundingRectangle(formula[1], color=BLUE, buff=0.1)
        rhs_deriv_box = SurroundingRectangle(VGroup(formula[18], formula[19]), color=GREEN, buff=0.1)
        
        self.play(Create(lhs_deriv_box))
        self.wait(0.5)
        
        # Animate the "swap"
        swap_text = Text("derivative swaps!", font_size=24, color=YELLOW)
        swap_text.next_to(formula, UP)
        
        # Create curved arrow showing the swap
        swap_arrow = CurvedArrow(
            formula[1].get_center() + UP * 0.5,
            formula[18].get_center() + UP * 0.5,
            angle=-PI/3,
            color=YELLOW
        )
        
        self.play(
            Create(swap_arrow),
            Write(swap_text),
            Create(rhs_deriv_box)
        )
        self.wait(1)
        
        # Highlight boundary term
        self.play(FadeOut(lhs_deriv_box, rhs_deriv_box, swap_arrow, swap_text))
        
        boundary_box = SurroundingRectangle(
            VGroup(formula[6:14]),
            color=YELLOW,
            buff=0.1
        )
        boundary_text = Text("Boundary Integral", font_size=24, color=YELLOW)
        boundary_text.next_to(boundary_box, UP)
        
        self.play(Create(boundary_box), Write(boundary_text))
        self.wait(1)
        
        # Show omega and partial omega labels
        omega_label = MathTex(r"\Omega = \text{Region}", font_size=28)
        boundary_label = MathTex(r"\partial\Omega = \text{Boundary}", font_size=28)
        labels = VGroup(omega_label, boundary_label).arrange(DOWN).to_edge(LEFT)
        
        self.play(Write(labels))
        self.wait(2)


class Scene5_DivergenceTheorem(Scene):
    """Scene 5: Special Case Gives Divergence Theorem."""
    
    def construct(self):
        title = Text("Scene 5: The Divergence Theorem", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Start with Gauss-Green identity
        gauss_green = MathTex(
            r"\int_\Omega",
            r"\nabla u",
            r"\cdot",
            r"\vec{v}",
            r"\, dV",
            r"=",
            r"\int_{\partial\Omega}",
            r"u",
            r"(",
            r"\vec{v}",
            r"\cdot",
            r"\hat{n}",
            r")",
            r"\, dS",
            r"-",
            r"\int_\Omega",
            r"u",
            r"(",
            r"\nabla \cdot",
            r"\vec{v}",
            r")",
            r"\, dV",
            font_size=36
        )
        gauss_green[1].set_color(BLUE)
        gauss_green[7].set_color(BLUE)
        gauss_green[16].set_color(BLUE)
        
        self.play(Write(gauss_green))
        self.wait(1)
        
        # Narration: Set u = 1
        narration1 = Text("Let's set u = 1...", font_size=28).to_edge(DOWN)
        self.play(Write(narration1))
        self.wait(0.5)
        
        # Highlight u terms
        u_boxes = VGroup(
            SurroundingRectangle(gauss_green[1], color=RED, buff=0.05),
            SurroundingRectangle(gauss_green[7], color=RED, buff=0.05),
            SurroundingRectangle(gauss_green[16], color=RED, buff=0.05),
        )
        self.play(Create(u_boxes))
        self.wait(0.5)
        
        # Transform: u = 1
        u_equals_1 = MathTex("u = 1", font_size=36, color=RED).next_to(gauss_green, UP)
        self.play(Write(u_equals_1))
        self.wait(0.5)
        
        # Simplify: nabla(1) = 0, so LHS = 0
        self.play(FadeOut(narration1))
        
        narration2 = Text("Since ∇(1) = 0, the left side vanishes!", font_size=28).to_edge(DOWN)
        self.play(Write(narration2))
        self.wait(1)
        
        # Show the simplified version
        self.play(FadeOut(gauss_green, u_boxes, u_equals_1, narration2))
        
        # Show: 0 = boundary - volume
        step1 = MathTex(
            r"0 = \int_{\partial\Omega} (1)(\vec{v} \cdot \hat{n})\, dS - \int_\Omega (1)(\nabla \cdot \vec{v})\, dV",
            font_size=32
        )
        self.play(Write(step1))
        self.wait(1)
        
        # Simplify
        step2 = MathTex(
            r"0 = \int_{\partial\Omega} \vec{v} \cdot \hat{n}\, dS - \int_\Omega \nabla \cdot \vec{v}\, dV",
            font_size=32
        ).shift(DOWN)
        self.play(Write(step2))
        self.wait(1)
        
        # Rearrange
        self.play(FadeOut(step1, step2))
        
        # Final Divergence Theorem
        div_theorem = MathTex(
            r"\iiint_\Omega",
            r"\nabla \cdot \vec{F}",
            r"\, dV",
            r"=",
            r"\iint_{\partial\Omega}",
            r"\vec{F} \cdot \hat{n}",
            r"\, dS",
            font_size=48
        )
        div_theorem[1].set_color(GREEN)
        div_theorem[5].set_color(YELLOW)
        
        box = SurroundingRectangle(div_theorem, color=GOLD, buff=0.2)
        theorem_label = Text("The Divergence Theorem", font_size=28, color=GOLD)
        theorem_label.next_to(box, UP)
        
        self.play(Write(div_theorem))
        self.play(Create(box), Write(theorem_label))
        self.wait(1)
        
        # Final narration
        narration_final = Text(
            "When u = 1, the Gauss-Green identity reduces to\nthe Divergence Theorem!",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(narration_final))
        self.wait(2)


class Scene6_Intuition(ThreeDScene):
    """Scene 6: Intuition Animation - Divergence and Flux."""
    
    def construct(self):
        title = Text("Scene 6: Intuition - Divergence = Flux", font_size=36)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Set up 3D camera
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        # Create a sphere (the region)
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u) * np.sin(v),
                1.5 * np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(24, 24),
            fill_opacity=0.3,
            checkerboard_colors=[BLUE_D, BLUE_E],
            stroke_width=0.5
        )
        
        self.play(FadeIn(sphere))
        self.wait(0.5)
        
        # Create arrows inside the region pointing outward (positive divergence)
        narration1 = Text(
            "Positive divergence: vectors spread outward",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration1)
        self.play(Write(narration1))
        
        # Create internal arrows
        internal_arrows = VGroup()
        np.random.seed(42)  # For reproducibility
        for _ in range(20):
            # Random point inside sphere
            r = np.random.uniform(0.3, 1.0)
            theta = np.random.uniform(0, TAU)
            phi = np.random.uniform(0.2, PI - 0.2)
            
            x = r * np.cos(theta) * np.sin(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(phi)
            
            start = np.array([x, y, z])
            # Outward direction
            direction = start / np.linalg.norm(start) * 0.3
            
            arrow = Arrow3D(
                start=start,
                end=start + direction,
                color=GREEN,
                thickness=0.02,
                height=0.08,
                base_radius=0.03
            )
            internal_arrows.add(arrow)
        
        self.play(Create(internal_arrows))
        self.wait(1)
        
        # Animate flux through boundary
        self.play(FadeOut(narration1))
        self.remove_fixed_in_frame_mobjects(narration1)
        
        narration2 = Text(
            "More flows OUT across the surface!",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration2)
        self.play(Write(narration2))
        
        # Create surface arrows (flux)
        surface_arrows = VGroup()
        for theta in np.linspace(0, TAU, 12, endpoint=False):
            for phi in np.linspace(0.3, PI - 0.3, 5):
                x = 1.5 * np.cos(theta) * np.sin(phi)
                y = 1.5 * np.sin(theta) * np.sin(phi)
                z = 1.5 * np.cos(phi)
                start = np.array([x, y, z])
                # Normal direction (outward)
                normal = start / np.linalg.norm(start)
                
                arrow = Arrow3D(
                    start=start,
                    end=start + normal * 0.5,
                    color=YELLOW,
                    thickness=0.02,
                    height=0.1,
                    base_radius=0.04
                )
                surface_arrows.add(arrow)
        
        self.play(
            Create(surface_arrows),
            sphere.animate.set_fill(opacity=0.1)
        )
        self.wait(1)
        
        # Final message
        self.play(FadeOut(narration2))
        self.remove_fixed_in_frame_mobjects(narration2)
        
        narration3 = Text(
            "Divergence inside = Flux outside\nJust like integration by parts!",
            font_size=24
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(narration3)
        self.play(Write(narration3))
        
        # Rotate to show
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        self.wait(1)


class Scene7_Summary(Scene):
    """Scene 7: Final Summary Frame - Split screen comparison."""
    
    def construct(self):
        title = Text("Scene 7: Summary", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)
        
        # Create split screen
        divider = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=2)
        self.play(Create(divider))
        
        # Left side: 1D
        left_title = Text("1D: Integration by Parts", font_size=24, color=BLUE)
        left_title.to_edge(LEFT).shift(UP * 2 + RIGHT * 1.5)
        
        # Number line with glowing endpoints
        line_1d = Line(LEFT * 3.5, LEFT * 0.5, color=WHITE)
        a_dot = Dot(LEFT * 3.5, color=YELLOW).scale(1.5)
        b_dot = Dot(LEFT * 0.5, color=YELLOW).scale(1.5)
        
        # Glow effect for endpoints
        a_glow = Circle(radius=0.3, color=YELLOW, fill_opacity=0.3).move_to(a_dot)
        b_glow = Circle(radius=0.3, color=YELLOW, fill_opacity=0.3).move_to(b_dot)
        
        line_1d_group = VGroup(line_1d, a_dot, b_dot, a_glow, b_glow)
        line_1d_group.shift(DOWN * 0.5)
        
        # 1D formula
        formula_1d = MathTex(
            r"\int_a^b u'v\, dx = [uv]_a^b - \int_a^b uv'\, dx",
            font_size=24
        )
        formula_1d.next_to(line_1d_group, DOWN)
        
        # Boundary label
        boundary_1d = Text("Endpoints", font_size=20, color=YELLOW)
        boundary_1d.next_to(formula_1d, DOWN)
        
        self.play(Write(left_title), Create(line_1d_group))
        self.play(Write(formula_1d), Write(boundary_1d))
        self.wait(0.5)
        
        # Right side: 3D
        right_title = Text("3D: Divergence Theorem", font_size=24, color=GREEN)
        right_title.to_edge(RIGHT).shift(UP * 2 + LEFT * 1.5)
        
        # 3D region (represented as 2D circle for this scene)
        blob = Circle(radius=1.2, color=GREEN, fill_opacity=0.3)
        blob.shift(RIGHT * 2 + DOWN * 0.5)
        
        # Glowing boundary
        boundary_glow = Circle(radius=1.3, color=YELLOW, stroke_width=4)
        boundary_glow.move_to(blob)
        
        # Add some arrows pointing out
        arrows = VGroup()
        for angle in np.linspace(0, TAU, 8, endpoint=False):
            start = blob.get_center() + np.array([
                1.2 * np.cos(angle),
                1.2 * np.sin(angle),
                0
            ])
            end = start + np.array([
                0.4 * np.cos(angle),
                0.4 * np.sin(angle),
                0
            ])
            arrow = Arrow(start, end, color=YELLOW, buff=0, stroke_width=2)
            arrows.add(arrow)
        
        region_group = VGroup(blob, boundary_glow, arrows)
        
        # 3D formula
        formula_3d = MathTex(
            r"\int_\Omega \nabla \cdot \vec{F}\, dV = \int_{\partial\Omega} \vec{F} \cdot \hat{n}\, dS",
            font_size=24
        )
        formula_3d.next_to(region_group, DOWN)
        
        # Boundary label
        boundary_3d = Text("Surface Boundary", font_size=20, color=YELLOW)
        boundary_3d.next_to(formula_3d, DOWN)
        
        self.play(Write(right_title), Create(region_group))
        self.play(Write(formula_3d), Write(boundary_3d))
        self.wait(1)
        
        # Final narration
        final_text = Text(
            "The Divergence Theorem is Integration by Parts...\nin many dimensions, for vector fields!",
            font_size=28,
            color=GOLD
        ).to_edge(DOWN)
        
        self.play(Write(final_text))
        
        # Pulse the boundaries
        self.play(
            a_glow.animate.scale(1.5).set_opacity(0.6),
            b_glow.animate.scale(1.5).set_opacity(0.6),
            boundary_glow.animate.set_stroke(width=8),
            rate_func=rate_functions.there_and_back,
            run_time=2
        )
        
        self.wait(2)


class DivergenceTheoremAnimation(Scene):
    """
    Main animation that combines all scenes.
    This creates a simple intro animation.
    For the full video, render individual scenes and combine them.
    """
    
    def construct(self):
        intro_text = Text(
            "Divergence Theorem = Integration by Parts in 3D",
            font_size=40,
            color=GOLD
        )
        
        subtitle = Text(
            "A Mathematical Animation",
            font_size=28
        ).next_to(intro_text, DOWN)
        
        self.play(Write(intro_text))
        self.play(Write(subtitle))
        self.wait(2)
        
        self.play(FadeOut(intro_text, subtitle))
        
        # Show overview of what's coming
        overview = VGroup(
            Text("In this video:", font_size=32),
            Text("1. 1D Integration by Parts", font_size=24),
            Text("2. From Lines to Regions", font_size=24),
            Text("3. Functions to Fields", font_size=24),
            Text("4. The Gauss-Green Identity", font_size=24),
            Text("5. The Divergence Theorem", font_size=24),
            Text("6. Visual Intuition", font_size=24),
            Text("7. Summary", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        self.play(Write(overview))
        self.wait(3)
        self.play(FadeOut(overview))
        
        # Note to user
        note = Text(
            "Render individual scenes for the full animation:\n"
            "manim -pql divergence_theorem_animation.py Scene1_1DAnalogy\n"
            "(and so on for Scene2 through Scene7)",
            font_size=20,
            color=YELLOW
        )
        self.play(Write(note))
        self.wait(3)


if __name__ == "__main__":
    print("Divergence Theorem Animation")
    print("=" * 50)
    print("\nTo render the animation, use one of these commands:\n")
    print("Full intro animation:")
    print("  manim -pql divergence_theorem_animation.py DivergenceTheoremAnimation")
    print("\nIndividual scenes:")
    print("  manim -pql divergence_theorem_animation.py Scene1_1DAnalogy")
    print("  manim -pql divergence_theorem_animation.py Scene2_ReplaceInterval")
    print("  manim -pql divergence_theorem_animation.py Scene3_FunctionsToFields")
    print("  manim -pql divergence_theorem_animation.py Scene4_MultivariableIPP")
    print("  manim -pql divergence_theorem_animation.py Scene5_DivergenceTheorem")
    print("  manim -pql divergence_theorem_animation.py Scene6_Intuition")
    print("  manim -pql divergence_theorem_animation.py Scene7_Summary")
    print("\nQuality options:")
    print("  -pql  = preview quality, low resolution (fastest)")
    print("  -pqm  = preview quality, medium resolution")
    print("  -pqh  = preview quality, high resolution")
    print("  -qk   = 4K quality (slowest, best for YouTube)")
