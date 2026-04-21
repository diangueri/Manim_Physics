import numpy as np
from manim import (
    ThreeDScene, Surface, ThreeDAxes, DEGREES, PI,
    Tex, MathTex, Text, VGroup, Arrow, Dot,
    Create, FadeIn, FadeOut, Write,
    UP, DOWN, LEFT, RIGHT, ORIGIN,
    linear, smooth, always_redraw, ValueTracker
)

# Importamos la clase base y constantes desde vertical_scene.py
# Nota: VerticalScene y sus helpers son la base.
from vertical_scene import (
    VerticalScene, PALETTE, TITLE_SIZE, BIG_LABEL, 
    MEDIUM_LABEL, SAFE_TOP, SAFE_BOTTOM
)

class SegundaLeyNewton(VerticalScene):
    def construct(self):
        # 1. HOOK (0-3s)
        title = self.add_title(r"Segunda Ley de Newton", r"$F = m \cdot a$")
        self.wait(2)
        
        # Reducción de título (Regla 2.4)
        self.play(title.animate.scale(0.4).to_corner(LEFT + UP, buff=0.3), run_time=0.6)

        # 2. DESARROLLO (6-25s)
        # Escenario: Bloque siendo empujado
        bloque = VGroup(
            Tex(r"m", font_size=BIG_LABEL, color=PALETTE["accent"]),
            # Representación visual de un objeto
            # Usamos un rectángulo simple pero animado
        )
        caja = VGroup(
            Tex(r"m", font_size=BIG_LABEL, color=PALETTE["text"]),
        )
        # Dibujamos una caja real
        from manim import Rectangle
        caja_rect = Rectangle(width=1.5, height=1.5, color=PALETTE["accent"], fill_opacity=0.3)
        caja_label = Tex(r"$m$", font_size=BIG_LABEL)
        caja_grupo = VGroup(caja_rect, caja_label).move_to(ORIGIN)

        self.play(FadeIn(caja_grupo), run_time=1)

        # Vector Fuerza
        fuerza = self.vector(ORIGIN, RIGHT * 2, color=PALETTE["accent2"])
        f_label = MathTex(r"\vec{F}", color=PALETTE["accent2"]).next_to(fuerza, UP)
        
        self.play(Create(fuerza), Write(f_label))
        self.wait(1)

        # 3. CLIMAX VISUAL (25-45s)
        # Animación de aceleración
        # Mostramos cómo la fuerza causa movimiento
        self.play(caja_grupo.animate.shift(RIGHT * 3), 
                  fuerza.animate.shift(RIGHT * 3),
                  f_label.animate.shift(RIGHT * 3),
                  run_time=3, rate_func=linear)
        
        # Ecuación dinámica
        formula = self.formula_box(r"F = m \cdot a", y=-3, font_size=60, color=PALETTE["ok"])
        self.play(FadeIn(formula, shift=UP))
        
        # Explicación visual de la relación
        relacion = Text("Más fuerza = Más aceleración", font_size=MEDIUM_LABEL, color=PALETTE["muted"])
        relacion.move_to([0, -4.5, 0])
        self.play(Write(relacion))
        
        self.wait(3)

        # 4. CIERRE (45-55s)
        self.clear_scene()
        resumen = VGroup(
            Tex(r"Fuerza $\propto$ Aceleración", font_size=BIG_LABEL, color=PALETTE["accent"]),
            Tex(r"Masa $\propto$ Inercia", font_size=BIG_LABEL, color=PALETTE["accent2"])
        ).arrange(DOWN, buff=1)
        
        self.play(FadeIn(resumen[0]), run_time=1)
        self.wait(1)
        self.play(FadeIn(resumen[1]), run_time=1)
        
        self.wait(2)

    def vector(self, start, end, color=None, buff=0):
        # Sobreescritura local para asegurar visibilidad si el helper fallara
        return Arrow(start, end, color=color or PALETTE["accent"], buff=buff,
                     stroke_width=8, max_tip_length_to_length_ratio=0.25)