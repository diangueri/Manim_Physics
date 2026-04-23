import numpy as np
from manim import (
    Scene, Tex, MathTex, Text, VGroup, Arrow, Dot,
    Write, FadeIn, FadeOut, Create, ReplacementTransform,
    DOWN, UP, LEFT, RIGHT, ORIGIN, PI, linear,
    ValueTracker, always_redraw, TracedPath
)

# Importamos la clase base desde el archivo de referencia
# Nota: VerticalScene ya maneja el setup del watermark y las constantes
from vertical_scene import VerticalScene, PALETTE, TITLE_SIZE, BIG_LABEL, MEDIUM_LABEL, SAFE_TOP, SAFE_BOTTOM

class LeyDeOhm(VerticalScene):
    def construct(self):
        # 1. HOOK
        title = self.add_title("Ley de Ohm", "El flujo de la corriente")
        self.wait(2)
        
        # Reducción del título (Regla 2.4)
        self.play(title.animate.scale(0.4).to_corner(UP + LEFT, buff=0.3), run_time=0.6)

        # 2. ESCENARIO DEL CIRCUITO
        # Representación visual: Un circuito simple con resistencia
        resistor = VGroup(
            *[Tex(r"$\sim$", color=PALETTE["accent2"]).shift(i * 0.5 * RIGHT) for i in range(5)]
        ).move_to([0, 1, 0])
        
        wire_top = Arrow([-2, 1, 0], [2, 1, 0], buff=0, color=PALETTE["text"])
        wire_bot = Arrow([2, -1, 0], [-2, -1, 0], buff=0, color=PALETTE["text"])
        
        circuit = VGroup(resistor, wire_top, wire_bot)
        self.play(Create(circuit), run_time=1.5)

        # 3. ANIMACIÓN DE ELECTRONES (Regla 2.1 y 2.2)
        electron = Dot(color=PALETTE["accent"], radius=0.15)
        path = [
            [-2, 1, 0], [2, 1, 0], [2, -1, 0], [-2, -1, 0], [-2, 1, 0]
        ]
        
        # Etiqueta de Voltaje y Resistencia
        v_label = MathTex(r"V", color=PALETTE["accent"]).next_to(wire_top, UP)
        r_label = MathTex(r"R", color=PALETTE["accent2"]).next_to(resistor, DOWN)
        self.play(FadeIn(v_label), FadeIn(r_label))

        # Movimiento de electrones
        self.add(electron)
        for i in range(3):
            self.play(electron.animate.move_to(path[i+1]), run_time=1.5, rate_func=linear)

        # 4. CLIMAX VISUAL: Fórmula
        self.clear_scene(keep_watermark=True)
        
        formula = MathTex(r"V = I \cdot R", font_size=80, color=PALETTE["text"])
        self.play(Write(formula), run_time=1)
        self.wait(1)

        # Desglose visual
        v_text = Text("Voltaje (Fuerza)", font_size=MEDIUM_LABEL, color=PALETTE["accent"]).shift(UP * 2)
        i_text = Text("Intensidad (Flujo)", font_size=MEDIUM_LABEL, color=PALETTE["text"]).shift(ORIGIN)
        r_text = Text("Resistencia (Oposición)", font_size=MEDIUM_LABEL, color=PALETTE["accent2"]).shift(DOWN * 2)

        self.play(
            FadeIn(v_text, shift=RIGHT),
            FadeIn(i_text, shift=RIGHT),
            FadeIn(r_text, shift=RIGHT),
            formula.animate.scale(0.6).to_edge(UP, buff=2)
        )
        
        # 5. CIERRE
        self.wait(3)
        
        # Resumen final
        final_msg = Text("¡Más resistencia, menos flujo!", font_size=BIG_LABEL, color=PALETTE["ok"])
        final_msg.move_to([0, -3, 0])
        self.play(FadeIn(final_msg))
        
        self.wait(2)