from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 30
config.background_color = "#0b0f1a"

SAFE_TOP, SAFE_BOTTOM = 6.4, -6.4
SAFE_LEFT, SAFE_RIGHT = -3.8, 3.8
TITLE_SIZE = 72; SUBTITLE_SIZE = 44; BIG_LABEL = 48; MEDIUM_LABEL = 40; SMALL_LABEL = 32

PALETTE = {
    "bg": "#0b0f1a",
    "accent": "#22d3ee",
    "accent2": "#f59e0b",
    "ok": "#10b981",
    "warn": "#ef4444",
    "text": "#f8fafc",
    "muted": "#94a3b8",
}
WATERMARK_HANDLE = "@eldiariodeunfisico"

class VerticalScene(Scene):
    def setup(self):
        super().setup()
        wm = Tex(WATERMARK_HANDLE, font_size=30, color=PALETTE["muted"])
        wm.set_opacity(0.55); wm.move_to([0, -7.4, 0])
        self.add(wm); self.watermark = wm

class CampoElectrico(VerticalScene):
    def construct(self):
        # Hook
        title = Title("El Campo Eléctrico", font_size=TITLE_SIZE, color=PALETTE["accent"])
        self.play(Write(title))
        self.wait(2)
        
        # Animación: Carga puntual
        charge = Dot(color=PALETTE["warn"], radius=0.2)
        charge_label = Tex(r"$+q$", font_size=MEDIUM_LABEL).next_to(charge, UP)
        
        self.play(FadeIn(charge), Write(charge_label))
        
        # Red de vectores
        def field_func(pos):
            x, y, z = pos
            r = np.sqrt(x**2 + y**2)
            if r < 0.5: return np.array([0, 0, 0])
            return np.array([x, y, 0]) / (r**3) * 0.8

        field = ArrowVectorField(
            field_func, 
            x_range=[-3, 3, 0.6], 
            y_range=[-4, 4, 0.6],
            colors=[PALETTE["accent"], PALETTE["accent2"]],
            length_func=lambda x: 0.3 + 0.2 * np.tanh(x)
        )
        
        self.play(Create(field), run_time=3)
        
        # Reducción de título
        self.play(title.animate.scale(0.4).to_corner(UL, buff=0.3))
        
        # Explicación visual: Ley de Coulomb / Fuerza
        test_charge = Dot(color=PALETTE["ok"], radius=0.15).move_to([2, 1, 0])
        force_arrow = Arrow(start=test_charge.get_center(), end=test_charge.get_center() + [0.8, 0.4, 0], 
                            color=PALETTE["ok"], buff=0)
        force_label = MathTex(r"\vec{F} = q\vec{E}", font_size=MEDIUM_LABEL, color=PALETTE["ok"]).next_to(force_arrow, UP)
        
        self.play(FadeIn(test_charge), GrowArrow(force_arrow), Write(force_label))
        self.wait(2)
        
        # Climax: Movimiento de la carga de prueba
        path = ArcBetweenPoints(start=[2, 1, 0], end=[1, 2.5, 0], angle=-0.5)
        self.play(MoveAlongPath(test_charge, path), 
                  UpdateFromFunc(force_arrow, lambda a: a.put_start_and_end_on(test_charge.get_center(), test_charge.get_center() + field_func(test_charge.get_center()) * 5)),
                  run_time=4, rate_func=linear)
        
        # Cierre
        formula = MathTex(r"\vec{E} = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \hat{r}", font_size=BIG_LABEL, color=PALETTE["text"])
        formula.move_to([0, -4, 0])
        
        self.play(FadeIn(formula))
        self.wait(3)
        
        # Limpieza final
        self.play(FadeOut(field), FadeOut(charge), FadeOut(test_charge), FadeOut(force_arrow), FadeOut(force_label), FadeOut(charge_label))
        self.play(formula.animate.move_to(ORIGIN))
        self.wait(2)

if __name__ == "__main__":
    from manim import *
    # Ejecución directa si se llama como script
    pass