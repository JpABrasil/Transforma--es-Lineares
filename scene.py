from manim import *
from Transformation import transformation
class cena_translate2D(Scene):
    def construct(self):
        #Defininindo Vetor inicial e Vetor de Translação
        v0 = [[0,0],[1,1]]
        a = [3,1]
        v1 = transformation.translate2D(v0,a[0],a[1])
        #Animacao
        plano = NumberPlane(background_line_style={"stroke_opacity": 0.0})
        self.add(plano)
        self.wait(2)
        ponto_origem = Dot((v0[0][0],v0[0][1],0)) #0 a mais adicionado pela biblioteca de animação pedir 
        linha_v0 = Arrow([v0[0][0],v0[0][1],0],[v0[1][0],v0[1][1],0],buff=0)
        texto_origem = Text('O =(0, 0)',font_size=20).next_to(ponto_origem, DOWN)
        texto_linha_v0 = Text('v =(1, 1)',font_size=20).next_to(linha_v0.get_end(), RIGHT)
        self.play([Create(ponto_origem),Create(linha_v0),Create(texto_origem),Create(texto_linha_v0)])
        self.wait(2)
        linha_a = Arrow(ORIGIN,[a[0],a[1],0],buff=0)
        texto_linha_a= Text('a =(3, 1)',font_size=20).next_to(linha_a.get_end(), RIGHT)
        self.play([Create(linha_a),Create(texto_linha_a)])
        self.wait(2)
        linha_v1 = Arrow([v1[0][0],v1[0][1],0],[v1[1][0],v1[1][1],0],buff=0)
        texto_linha_v1= Text('va =(4, 2) - (3, 1)',font_size=20).next_to(linha_v1.get_end(), RIGHT)
        self.play([Transform(texto_linha_v0,texto_linha_v1),Transform(linha_v0,linha_v1)])
        self.wait(2)
class cena_translate3D(ThreeDScene):
    def construct(self):
        #Definindo Vetores e Transladando
        v0 = [[0,0,0],[1,1,1]]
        dx=3
        dy=1
        dz=2
        v1 = transformation.translate3D(v0,dx,dy,dz)
        axes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1])
        labels = axes.get_axis_labels(
            Text("x-axis"), Text("y-axis"), Text("z-axis").rotate(PI/2,axis=Y_AXIS).scale(0.5)
        )
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        self.add(axes,labels)
        linha_v0 = Vector(v0[1])
        texto_linha_v0 =Text("v = (1,1,1)",font_size=20).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/4,axis=Z_AXIS).next_to(linha_v0.get_end(),LEFT)
        linha_a = Vector([dx,dy,dz])
        texto_linha_a =Text("a = (3,1,2)",font_size=20).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/4,axis=Z_AXIS).next_to(linha_a.get_end(),LEFT)
        linha_v1 = Arrow([dx,dy,dz],v1[1])
        texto_linha_v1 =Text("va = (4,2,3) - (3,1,2) ",font_size=20).rotate(PI/2,axis=X_AXIS).rotate(PI*0.7,axis=Z_AXIS).next_to(linha_v1.get_end(),LEFT)
        self.play([Create(linha_v0),Create(texto_linha_v0)])
        self.wait(3)
        self.play([Create(linha_a),Create(texto_linha_a)])
        self.wait(3)
        self.play([Transform(linha_v0,linha_v1),Transform(texto_linha_v0,texto_linha_v1)])
        self.wait(3)
class cena_rotation2D(Scene):
    def construct(self):
        v0 = [[0,0],[1,1]]
        angle = 90
        v1 = transformation.rotation2D(v0,angle)
        plano = NumberPlane(background_line_style={"stroke_opacity": 0.0})
        self.add(plano)
        ponto_origem = Dot((v0[0][0],v0[0][1],0)) #0 a mais adicionado pela biblioteca de animação pedir 
        texto_origem = Text('O =(0, 0)',font_size=20).next_to(ponto_origem, DOWN + LEFT)
        linha_v0 = Arrow([v0[0][0],v0[0][1],0],[v0[1][0],v0[1][1],0],buff=0)
        linha_v02 = Arrow([v0[0][0],v0[0][1],0],[v0[1][0],v0[1][1],0],buff=0)
        texto_linha_v0 = Text('v =(1, 1)',font_size=20).next_to(linha_v0.get_end(), RIGHT)
        self.play([Create(ponto_origem),Create(linha_v0),Create(texto_origem),Create(texto_linha_v0)])
        self.wait(3)
        linha_v1 = Arrow([v1[0][0],v1[0][1],0],[v1[1][0],v1[1][1],0],buff=0)
        texto_linha_v1= Text(f'v = ({v1[1][0]:.3},{v1[1][1]:.3})',font_size=20).next_to(linha_v1.get_end(), RIGHT)
        a =Angle(linha_v0,linha_v1,other_angle=True)
        self.play([Create(a),Create(Text(f'â =90º',font_size=20).next_to(a.get_end(), RIGHT))])
        self.add(linha_v02)
        self.play([Transform(linha_v0,linha_v1),Transform(texto_linha_v0,texto_linha_v1)])
        self.wait(6)
class cena_rotation3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-1, 1, 1], y_range=[-1, 1, 1], z_range=[-1, 1, 1],)
        labels = axes.get_axis_labels(
            Text("x"), Text("y"), Text("z").rotate(PI/2,axis=Y_AXIS).scale(0.5)
        )
        
        self.add(axes,labels)
        self.camera.set_zoom(0.6)
        self.set_camera_orientation(phi=2*PI/5, theta=PI/10)
        eq11 = MathTex(r"""
                        v = \begin{bmatrix}
                        1\\
                        0\\
                        1
                        \end{bmatrix}, \ 
                        R_x = \begin{bmatrix}
                        1 & 0 & 0\\
                        0 & \cos \theta  & \sin \theta \\
                        0 & -\sin \theta  & \cos \theta 
                        \end{bmatrix}, \ 
                        \theta = 180^\circ
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(5*OUT).shift(7.5*DOWN)
        eq12 = MathTex(r"""
                        v = \begin{bmatrix}
                        1\\
                        0\\
                        -1
                        \end{bmatrix}, \ 
                        R_z = \begin{bmatrix}
                        cos \theta & -\sin \theta & 0\\
                        \sin \theta & \cos \theta & 0 \\
                        0 & 0 & 1
                        \end{bmatrix}, \ 
                        \theta = 90^\circ
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(5*OUT).shift(7.5*DOWN)
        eq13 = MathTex(r"""
                        v = \begin{bmatrix}
                        0\\
                        1\\
                        -1
                        \end{bmatrix}, \ 
                        R_y = \begin{bmatrix}
                        cos \theta & 0 & \sin \theta\\
                        0 & 1 & 0 \\
                        -\sin \theta & 0 & cos \theta 
                        \end{bmatrix}, \ 
                        \theta = 180^\circ
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(5*OUT).shift(7.5*DOWN)
        eq21 = MathTex(r"""
                        v_x\ =\ \begin{bmatrix}
                        1 & 0 & 0\\
                        0 & cos180^\circ & sin180^\circ\\
                        0 & -sin180^\circ & cos180^\circ
                        \end{bmatrix}\begin{bmatrix}
                        1\\
                        0\\
                        1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq22 = MathTex(r"""
                        v_x\ =\ \begin{bmatrix}
                        1 & 0 & 0\\
                        0 & -1 & 0\\
                        0 & 0 & -1
                        \end{bmatrix}\begin{bmatrix}
                        1\\
                        0\\
                        1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq23 = MathTex(r"""
                        v_x=\begin{bmatrix}
                        1*1+0*0+0*1\\
                        0*1+0*( -1) +0*1\\
                        0*1+0*0+1*( -1)
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq24 = MathTex(r"""
                        v_x=\begin{bmatrix}
                        1\\
                        0\\
                        -1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq25 = MathTex(r"""
                        v_z\ =\ \begin{bmatrix}
                        cos90^\circ & -\sin90^\circ & 0\\
                        \sin90^\circ & \cos90^\circ & 0 \\
                        0 & 0 & 1
                        \end{bmatrix}\begin{bmatrix}
                        1\\
                        0\\
                        -1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq26 = MathTex(r"""
                        v_z\ =\ \begin{bmatrix}
                        0 & -1 & 0\\
                        1 & 0 & 0 \\
                        0 & 0 & 1
                        \end{bmatrix}\begin{bmatrix}
                        1\\
                        0\\
                        -1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq27 = MathTex(r"""
                        v_z\ =\ \begin{bmatrix}
                        0*1+0*(-1)+0*(-1)\\
                        1*1+0*0+0*(-1)\\
                        0*1+0*0+1*(-1)
                        \end{bmatrix}
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq28 = MathTex(r"""
                        v_z=\begin{bmatrix}
                        0\\
                        1\\
                        -1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq29 = MathTex(r"""
                        v_y\ =\ \begin{bmatrix}
                        cos180^\circ & 0 & \sin180^\circ\\
                        0 & 1 & 0 \\
                        -\sin180^\circ & 0 & \cos180^\circ
                        \end{bmatrix}\begin{bmatrix}
                        0\\
                        1\\
                        -1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq210 = MathTex(r"""
                        v_y\ =\ \begin{bmatrix}
                        -1 & 0 & 0\\
                        0 & 1 & 0 \\
                        0 & 0 & -1
                        \end{bmatrix}\begin{bmatrix}
                        0\\
                        1\\
                        -1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq211 = MathTex(r"""
                        v_y\ =\ \begin{bmatrix}
                        -1*0+1*0+0*(-1)\\
                        0*0+1*1+0*(-1)\\
                        0*0+0*1+(-1)*(-1)
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        eq212 = MathTex(r"""
                        v_y\ =\ \begin{bmatrix}
                        0\\
                        1\\
                        1
                        \end{bmatrix}\\
                        """,font_size = 40).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).shift(3*OUT).shift(9*DOWN)
        self.play(Write(eq11))
        v0 = [[0,0,0],[1.0,0,1.0]]
        vetor_v0 = Vector(v0[1])
        texto_v0 = Text(f"v = ({v0[1][0]},{v0[1][1]},{v0[1][2]})",font_size=28,color='WHITE').rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).next_to(vetor_v0.get_end(),2*UP)
        a = 180
        v1 = transformation.rotation3DX(v0,a)
        vetor_v1 =Vector(v0[1]).rotate(-PI,about_point=ORIGIN,axis=RIGHT)
        texto_v1 = Text(f"v = ({v1[1][0]},{round(v1[1][1],1)},{v1[1][2]})",font_size=28).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).next_to(vetor_v1.get_end(),2*UP)
        v2 = transformation.rotation3DZ(v1,-90)
        vetor_v2 = Vector(v2[1])
        texto_v2 = Text(f"v = ({round(v2[1][0],1)},{round(v2[1][1],1)},{round(v2[1][2],1)})",font_size=28).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).next_to(vetor_v2.get_end(),2*UP)
        v3 = transformation.rotation3DY(v2,180)
        vetor_v3 = Vector(v3[1])
        texto_v3 = Text(f"v = ({round(v3[1][0],1)},{round(v3[1][1],1)},{round(v3[1][2],1)})",font_size=28).rotate(PI/2,axis=Y_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/12,axis=Z_AXIS).next_to(vetor_v3.get_end(),2*UP)
        self.play([Create(vetor_v0),Create(texto_v0)])
        self.wait(2)
        self.play(Write(eq21))
        self.wait(2)
        self.play(Transform(eq21,eq22))
        self.wait(2)
        self.play(Transform(eq21,eq23))
        self.wait(2)
        self.play(Transform(eq21,eq24))
        self.play([Rotate(vetor_v0, -PI,about_point=ORIGIN,axis=RIGHT),Transform(texto_v0,texto_v1)])
        self.wait(2)
        self.play(Transform(eq11,eq12))
        self.play(Transform(eq21,eq25))
        self.wait(2)
        self.play(Transform(eq21,eq26))
        self.wait(2)
        self.play(Transform(eq21,eq27))
        self.wait(2)
        self.play(Transform(eq21,eq28))
        self.wait(2)
        self.play([Rotate(vetor_v0, PI/2,about_point=ORIGIN,axis=OUT),Transform(texto_v0,texto_v2)])
        self.wait(2)
        self.play(Transform(eq11,eq13))
        self.play(Transform(eq21,eq29))
        self.wait(2)
        self.play(Transform(eq21,eq29))
        self.wait(2)
        self.play(Transform(eq21,eq210))
        self.wait(2)
        self.play(Transform(eq21,eq211))
        self.wait(2)
        self.play(Transform(eq21,eq212))
        self.play([Rotate(vetor_v0, -PI,about_point=ORIGIN,axis=UP),Transform(texto_v0,texto_v3)])
        self.wait(3)
class cena_reflection2D(Scene):
    def construct(self):
        v0 = [[0,0],[1,1]]
        v1 = transformation.reflection2DX(v0)
        v2 = transformation.reflection2DY(v1)
        #Animacao
        plano = NumberPlane(background_line_style={"stroke_opacity": 0.0})
        self.add(plano)
        self.wait(2)
        ponto_origem = Dot((v0[0][0],v0[0][1],0)) #0 a mais adicionado pela biblioteca de animação pedir 
        linha_v0 = Arrow([v0[0][0],v0[0][1],0],[v0[1][0],v0[1][1],0],buff=0)
        texto_origem = Text('O =(0, 0)',font_size=20).next_to(ponto_origem, DOWN).shift(RIGHT)
        texto_linha_v0 = Text('v =(1, 1)',font_size=20).next_to(linha_v0.get_end(), RIGHT)
        self.play([Create(ponto_origem),Create(linha_v0),Create(texto_origem),Create(texto_linha_v0)])
        self.wait(2)
        texto_k = Text('Reflexão em X',font_size=20).shift(RIGHT*2.5).shift(UP*2.5)
        self.play(Create(texto_k))
        self.wait(2)
        linha_v1 = Arrow([v1[0][0],v1[0][1],0],[v1[1][0],v1[1][1],0],buff=0)
        texto_linha_v1= Text(f"v' =({v1[1][0]},{v1[1][1]})",font_size=20).next_to(linha_v1.get_end(), LEFT)
        self.play([Transform(texto_linha_v0,texto_linha_v1),Transform(linha_v0,linha_v1)])
        self.wait(2)
        texto_2 = Text('Reflexão em Y',font_size=20).shift(RIGHT*2.5).shift(UP*2.5)
        self.play(Transform(texto_k,texto_2))
        self.wait(2)
        linha_v2 = Arrow([v2[0][0],v2[0][1],0],[v2[1][0],v2[1][1],0],buff=0)
        texto_linha_v2= Text(f"v' =({v2[1][0]},{v2[1][1]})",font_size=20).next_to(linha_v2.get_end(), LEFT)
        self.play([Transform(texto_linha_v0,texto_linha_v2),Transform(linha_v0,linha_v2)])
        self.wait(2)
class cena_reflection3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-1, 1, 1], y_range=[-1, 1, 1], z_range=[-1, 1, 1],)
        labels = axes.get_axis_labels(
            Text("x"), Text("y"), Text("z").rotate(PI/2,axis=Y_AXIS).scale(0.5)
        )

        self.add(axes,labels)
        self.camera.set_zoom(1)
        self.set_camera_orientation(phi=2*PI/5, theta=PI/10)
        v0 = [[0,0,0],[1,-1,1]]
        linha_v0 = Vector(v0[1],color='white',)
        texto_linha_v0 =Text("v = (1,-1,1)",font_size=20).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).rotate(PI/10,Z_AXIS).next_to(linha_v0.get_end(),DOWN)
        self.play(Create(linha_v0))
        self.wait(2)
        self.play(Create(texto_linha_v0))
        self.wait(2)
        texto1 = Text("Reflexão em X",font_size=24).rotate(PI/2,X_AXIS).rotate(PI/2,Z_AXIS).rotate(PI/10,Z_AXIS).shift(OUT*2).shift(UP*1.5)
        self.play(Create(texto1))
        self.wait(2)
        v1 = transformation.reflection3DX(v0)
        linha_v1 = Vector(v1[1],color='white',)
        texto_linha_v1 =Text("v = (-1,-1,1)",font_size=20).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).rotate(PI/10,Z_AXIS).next_to(linha_v1.get_end(),DOWN)
        self.play(Transform(linha_v0,linha_v1))
        self.play(Transform(texto_linha_v0,texto_linha_v1))
        self.wait(2)
        texto2 = Text("Reflexão em Y",font_size=24).rotate(PI/2,X_AXIS).rotate(PI/2,Z_AXIS).rotate(PI/10,Z_AXIS).shift(OUT*2).shift(UP*1.5)
        self.play(Transform(texto1,texto2))
        self.wait(2)
        v2 = transformation.reflection3DY(v1)
        linha_v2 = Vector(v2[1],color='white',)
        texto_linha_v2 =Text("v = (-1,1,1)",font_size=20).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).rotate(PI/10,Z_AXIS).next_to(linha_v2.get_end(),UP)
        self.play(Transform(linha_v0,linha_v2))
        self.play(Transform(texto_linha_v0,texto_linha_v2))
        self.wait(2)
        texto3 = Text("Reflexão em Z",font_size=24).rotate(PI/2,X_AXIS).rotate(PI/2,Z_AXIS).rotate(PI/10,Z_AXIS).shift(OUT*2).shift(UP*1.5)
        self.play(Transform(texto1,texto3))
        self.wait(2)
        v3 = transformation.reflection3DZ(v2)
        linha_v3 = Vector(v3[1],color='white',)
        texto_linha_v3 =Text("v = (-1,1,-1)",font_size=20).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).rotate(PI/10,Z_AXIS).next_to(linha_v3.get_end(),UP)
        self.play(Transform(linha_v0,linha_v3))
        self.play(Transform(texto_linha_v0,texto_linha_v3))
        self.wait(2)  
class cena_shearing(Scene):
    def construct(self):
    #Defininindo Vetor inicial e Vetor de Translação
        v0 = [[0,0],[1,1]]
        v1 = transformation.shearing(v0,0,1)
        #Animacao
        plano = NumberPlane(background_line_style={"stroke_opacity": 0.0})
        self.add(plano)
        self.wait(2)
        ponto_origem = Dot((v0[0][0],v0[0][1],0)) #0 a mais adicionado pela biblioteca de animação pedir 
        linha_v0 = Arrow([v0[0][0],v0[0][1],0],[v0[1][0],v0[1][1],0],buff=0)
        texto_origem = Text('O =(0, 0)',font_size=20).next_to(ponto_origem, DOWN)
        texto_linha_v0 = Text('v =(1, 1)',font_size=20).next_to(linha_v0.get_end(), RIGHT)
        self.play([Create(ponto_origem),Create(linha_v0),Create(texto_origem),Create(texto_linha_v0)])
        self.wait(2)
        texto_k = Text('kx = 0  ky = 1',font_size=20).shift(RIGHT*2.5).shift(UP*2.5)
        self.play(Create(texto_k))
        self.wait(2)
        eq1 = MathTex(r"""
                        v'=\begin{bmatrix}
                        1 & 0\\
                        ky & 1
                        \end{bmatrix}\begin{bmatrix}
                        x\\
                        y
                        \end{bmatrix}\\
                      """,font_size = 32).shift(RIGHT*5.0).shift(UP*2.5)
        eq2 = MathTex(r"""
                        v'=\begin{bmatrix}
                        1*x\ +\ 0*y\\
                        ky*x\ +\ 1*y
                        \end{bmatrix}\\
                      """,font_size = 32).shift(RIGHT*5.0).shift(UP*2.5)
        eq3 = MathTex(r"""
                        v'=\begin{bmatrix}
                        x\\
                        ky*x\ +\ y
                        \end{bmatrix}\\
                      """,font_size = 32).shift(RIGHT*5.0).shift(UP*2.5)
        eq4 = MathTex(r"""
                       v'=\begin{bmatrix}
                        1\\
                        1*1\ +\ 1*1
                        \end{bmatrix}\\
                      """,font_size = 32).shift(RIGHT*5.0).shift(UP*2.5)
        eq5 = MathTex(r"""
                    v'=\begin{bmatrix}
                    1\\
                    2
                    \end{bmatrix}\\
                    """,font_size = 32).shift(RIGHT*5.0).shift(UP*2.5)
        self.play(Create(eq1))
        self.wait(2)
        self.play(Transform(eq1,eq2))
        self.wait(2)
        self.play(Transform(eq1,eq3))
        self.wait(2)
        self.play(Transform(eq1,eq4))
        self.wait(2)
        self.play(Transform(eq1,eq5))
        linha_v1 = Arrow([v1[0][0],v1[0][1],0],[v1[1][0],v1[1][1],0],buff=0)
        texto_linha_v1= Text(f"v' =({v1[1][0]},{v1[1][1]})",font_size=20).next_to(linha_v1.get_end(), RIGHT)
        self.play([Transform(texto_linha_v0,texto_linha_v1),Transform(linha_v0,linha_v1)])
        self.wait(2)
        texto_k2 = Text('kx = 1',font_size=20).shift(RIGHT*2.5).shift(UP*2.5)
class cena_projection2D(Scene):
      def construct(self):
        v0 = [[0,0],[1,1]]
        v1 = transformation.projection2DX(v0)
        v2 = transformation.projection2DY(v0)
        #Animacao
        plano = NumberPlane(background_line_style={"stroke_opacity": 0.0})
        self.add(plano)
        self.wait(2)
        ponto_origem = Dot((v0[0][0],v0[0][1],0)) #0 a mais adicionado pela biblioteca de animação pedir 
        linha_v0 = Arrow([v0[0][0],v0[0][1],0],[v0[1][0],v0[1][1],0],buff=0)
        texto_origem = Text('O =(0, 0)',font_size=20).next_to(ponto_origem, DOWN).shift(RIGHT)
        texto_linha_v0 = Text('v =(1, 1)',font_size=20).next_to(linha_v0.get_end(), RIGHT)
        self.play([Create(ponto_origem),Create(linha_v0),Create(texto_origem),Create(texto_linha_v0)])
        self.wait(2)
        texto_k = Text('Projeção Eixo X',font_size=20,color= 'blue').shift(RIGHT*2.5).shift(UP*2.5)
        self.play(Create(texto_k))
        self.wait(2)
        linha_v1 = Vector(v1[1],stroke_opacity=1,color='blue')
        self.play(Create(linha_v1))
        ortogonal_x = DashedLine(linha_v0.get_end(),linha_v1.get_end(),color='blue')
        self.play(Create(ortogonal_x))
        self.wait(2)
        texto_k = Text('Projeção Eixo Y',font_size=20,color= 'red').shift(RIGHT*2.5).shift(UP*2)
        self.play(Create(texto_k))
        self.wait(2)
        linha_v2 = Vector(v2[1],stroke_opacity=1,color='red')
        self.play(Create(linha_v2))
        ortogonal_x = DashedLine(linha_v0.get_end(),linha_v2.get_end(),color='red')
        self.play(Create(ortogonal_x))
        self.wait(2)
class cena_projection3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-1, 1, 1], y_range=[-1, 1, 1], z_range=[-1, 1, 1],)
        labels = axes.get_axis_labels(
            Text("x"), Text("y"), Text("z").rotate(PI/2,axis=Y_AXIS).scale(0.5)
        )
        self.add(axes,labels)
        self.camera.set_zoom(1)
        self.set_camera_orientation(phi=2*PI/5, theta=PI/10)
        v0 = [[0,0,0],[1,1,1]]
        linha_v0 = Vector(v0[1],color='white',)
        texto_linha_v0 =Text("v = (1,1,1)",font_size=20).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).rotate(PI/10,Z_AXIS).next_to(linha_v0.get_end(),UP)
        self.play(Create(linha_v0))
        self.wait(2)
        self.play(Create(texto_linha_v0))
        self.wait(2)
        texto1 = Text("Projeção em X",font_size=20,color='blue').rotate(PI/2,X_AXIS).rotate(PI/2,Z_AXIS).rotate(PI/10,Z_AXIS).shift(OUT*1.5).shift(UP*2.4)
        self.play(Write(texto1))
        self.wait(2)
        v1 = transformation.projection3DX(v0)
        linha_v1 = Vector(v1[1],stroke_opacity=1,color='blue')
        self.play(Create(linha_v1))
        ortogonal_x = DashedLine(linha_v0.get_end(),linha_v1.get_end(),color='blue')
        self.play(Create(ortogonal_x))
        self.wait(2)
        texto2 = Text("Projeção em Y",font_size=20,color='red').rotate(PI/2,X_AXIS).rotate(PI/2,Z_AXIS).rotate(PI/10,Z_AXIS).shift(OUT*1.5).shift(UP*2.4)
        self.play(FadeOut(texto1, shift=ORIGIN, scale=0.8))
        self.play(Write(texto2))
        self.wait(2)
        v2 = transformation.projection3DY(v0)
        linha_v2 = Vector(v2[1],stroke_opacity=1,color='red')
        self.play(Create(linha_v2))
        ortogonal_y = DashedLine(linha_v0.get_end(),linha_v2.get_end(),color='red')
        self.play(Create(ortogonal_y))
        self.wait(2)
        texto3 = Text("Projeção em Z",font_size=20,color='yellow').rotate(PI/2,X_AXIS).rotate(PI/2,Z_AXIS).rotate(PI/10,Z_AXIS).shift(OUT*1.5).shift(UP*2.4)
        self.play(FadeOut(texto2, shift=ORIGIN, scale=0.8))
        self.play(Write(texto3))
        self.wait(2)
        v3 = transformation.projection3DZ(v0)
        linha_v3 = Vector(v3[1],stroke_opacity=1,color='yellow')
        self.play(Create(linha_v3))
        ortogonal_z = DashedLine(linha_v0.get_end(),linha_v3.get_end(),color='yellow')
        self.play(Create(ortogonal_z))
        self.wait(2)