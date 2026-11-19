from manim import *
import numpy as np

# Original educational animation inspired by clean mathematical explainer aesthetics.
# No existing video or animation has been copied.

class GradientExplainer(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#10131D"
        accent, gold, coral, blue = "#55D6BE", "#FFC857", "#FF6B6B", "#6CA6FF"
        title = Text("THE GRADIENT", font_size=46, weight=BOLD, color=WHITE)
        subtitle = Text("Why does it point uphill the fastest?", font_size=25, color=accent)
        group = VGroup(title, subtitle).arrange(DOWN, buff=0.22)
        self.play(FadeIn(group, shift=UP))
        self.wait(1.5)
        self.play(group.animate.scale(0.62).to_edge(UP))

        axes = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[0, 10, 2],
            x_length=6.2, y_length=6.2, z_length=3.5,
            axis_config={"color": GREY_B})
        surface = Surface(
            lambda u, v: axes.c2p(u, v, u*u + 2*v*v),
            u_range=[-1.6, 1.6], v_range=[-1.3, 1.3],
            resolution=(22, 22), fill_opacity=0.72,
            checkerboard_colors=["#24466A", "#2B8C88"],
            stroke_color=BLUE_E, stroke_width=0.35)
        self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES, zoom=0.82)
        self.play(Create(axes), FadeIn(surface), run_time=3)
        label = MathTex(r"z=f(x,y)=x^2+2y^2", color=WHITE).to_corner(UL)
        self.add_fixed_in_frame_mobjects(label)
        self.play(Write(label))
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(surface), FadeOut(axes))

        definition = VGroup(
            Text("For a two-variable function", font_size=29),
            MathTex(r"f(x,y)", color=gold),
            Text("the gradient collects its partial derivatives:", font_size=27),
            MathTex(r"\nabla f(x,y)=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)", color=accent)
        ).arrange(DOWN, buff=0.32)
        self.play(FadeIn(definition)); self.wait(3); self.play(FadeOut(definition))

        plane = NumberPlane(x_range=[-3,3,1], y_range=[-3,3,1],
                            background_line_style={"stroke_color": GREY_D, "stroke_opacity": 0.45})
        self.play(Create(plane))
        contours = VGroup()
        for c in [1,2,3,4,5,6,8,10]:
            contours.add(Ellipse(width=2*np.sqrt(c)*0.95, height=2*np.sqrt(c/2)*0.95,
                                 color=blue if c%2 else "#477C9E", stroke_width=2.2))
        contours.move_to(plane.get_origin())
        self.play(LaggedStart(*[Create(e) for e in contours], lag_ratio=0.12), run_time=3)
        p = plane.c2p(1,1)
        dot = Dot(p, color=gold, radius=0.09)
        point_label = MathTex("P=(1,1)", color=gold).next_to(dot, UR)
        self.play(FadeIn(dot), Write(point_label))
        grad_arrow = Arrow(p, p + 1.1*RIGHT + 2.2*UP, buff=0, color=accent,
                           stroke_width=7, max_tip_length_to_length_ratio=0.18)
        grad_label = MathTex(r"\nabla f(1,1)=(2,4)", color=accent).next_to(grad_arrow.get_end(), RIGHT)
        self.play(GrowArrow(grad_arrow), Write(grad_label)); self.wait(3)
        self.play(FadeOut(VGroup(plane, contours, dot, point_label, grad_arrow, grad_label)))

        work = VGroup(
            Text("WORKED EXAMPLE", font_size=34, color=gold, weight=BOLD),
            MathTex(r"f(x,y)=x^2+2y^2"),
            MathTex(r"f_x=2x,\qquad f_y=4y"),
            MathTex(r"\nabla f(x,y)=(2x,4y)", color=accent),
            MathTex(r"\nabla f(1,1)=(2,4)", color=gold),
            MathTex(r"\|\nabla f(1,1)\|=\sqrt{2^2+4^2}=2\sqrt5")
        ).arrange(DOWN, buff=0.34)
        self.play(Write(work), run_time=4); self.wait(4); self.play(FadeOut(work))

        proof = VGroup(
            Text("WHY IS THIS THE STEEPEST DIRECTION?", font_size=30, color=gold, weight=BOLD),
            MathTex(r"D_{\mathbf u}f=\nabla f\cdot\mathbf u"),
            MathTex(r"=\|\nabla f\|\,\|\mathbf u\|\cos\theta"),
            MathTex(r"\|\mathbf u\|=1\quad\Rightarrow\quad D_{\mathbf u}f=\|\nabla f\|\cos\theta"),
            MathTex(r"\text{Maximum when }\cos\theta=1\ (\theta=0)", color=accent),
            MathTex(r"\therefore\quad \mathbf u=\frac{\nabla f}{\|\nabla f\|}", color=gold)
        ).arrange(DOWN, buff=0.32)
        self.play(FadeIn(proof), run_time=2); self.wait(5); self.play(FadeOut(proof))

        summary = VGroup(
            Text("THREE TAKEAWAYS", font_size=40, color=gold, weight=BOLD),
            Text("1. The gradient is built from partial derivatives.", font_size=26),
            Text("2. It is perpendicular to a level curve.", font_size=26),
            Text("3. It points toward the greatest instantaneous increase.", font_size=26, color=accent),
            Text("Mohammad Mustafa • E25B070875", font_size=21, color=GREY_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        self.play(FadeIn(summary, shift=UP)); self.wait(5); self.play(FadeOut(summary))
        credits = VGroup(
            Text("THANK YOU", font_size=48, color=accent, weight=BOLD),
            Text("M3 • Gradient: Direction of Steepest Increase", font_size=23),
            Text("AI assistance disclosed in project README", font_size=18, color=GREY_B)
        ).arrange(DOWN, buff=0.3)
        self.play(FadeIn(credits)); self.wait(3)
