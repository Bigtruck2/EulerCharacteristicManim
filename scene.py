import math

import manim.constants
from manim import *


class CreateCircle(Scene):
    def construct(self):
        vertices = [n + 1 for n in range(4)]
        edges = [(n + 1, n + 2) for n in range(4 - 1)]
        g = Graph(vertices, edges, layout='circular')
        tex_labels = []
        face1 = MathTex(r"F_{1}").scale(.75)
        for v in g.vertices:
            label = MathTex(fr"V_{v}").scale(0.5).next_to(g.vertices[v], DOWN)
            tex_labels.append(label)
        for e in g.edges:
            label2 = MathTex(fr"E{e}").scale(0.5).next_to(g.edges[e], np.array((0.0, 0.0, 0.0)))
            tex_labels.append(label2)
        label_group = VGroup(*tex_labels)
        equation = VGroup(MathTex(fr"V-E+F=2"), MathTex(f"{g.vertices.__len__()}-{g.edges.__len__()}+1=2")).arrange(
            DOWN).to_edge(DOWN)
        explanation = Text("Edges = v \n so v−(v−1)+1=2").to_edge(LEFT).scale(.5)
        self.play(Create(g), Create(label_group), Write(face1), Write(equation), Write(explanation))
        self.wait(2)
        self.play(FadeOut(equation, explanation))
        g.add_edges((4, 1))
        g.update_edges(g)
        label_group.add(MathTex(fr"E{(4, 1)}").scale(0.5).next_to(g.edges[(4, 1)], np.array((0.0, 0.0, 0.0))))
        face2 = MathTex(r"F_{2}").scale(.75).to_corner(UP + LEFT)
        explanation2 = Text("Adding an edge \n without adding a \n vertex creates \n a new face").to_edge(LEFT).shift(LEFT).scale(.5)
        equation = VGroup(MathTex(fr"V-E+F=2"), MathTex(f"{g.vertices.__len__()}-{g.edges.__len__()}+2=2")).arrange(
            DOWN).to_edge(DOWN)
        self.play(Write(equation), Write(face2), Write(explanation2))
        self.wait(2)
        self.play(FadeOut(g, label_group, face1, equation, face2, explanation2))
