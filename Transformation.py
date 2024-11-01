import math
class transformation:
    def translate2D(vetor,dx,dy):
        origem = vetor[0]
        componentes = vetor[1]
        origem_t = [origem[0]+dx,
                    origem[1]+dy]
        componentes_t = [componentes[0]+dx,
                         componentes[1]+dy]
        return [origem_t,componentes_t]
    def translate3D(vetor,dx,dy,dz):
        origem = vetor[0]
        componentes = vetor[1]
        origem_t = [origem[0]+dx,
                    origem[1]+dy,
                    origem[2]+dz]
        componentes_t = [componentes[0]+dx,
                         componentes[1]+dy,
                         componentes[2]+dz]
        return [origem_t,componentes_t]
    def rotation2D(vetor,angle):
        angle_radian = math.radians(angle)
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [
            componentes[0]*math.cos(angle_radian)+
            componentes[1]*math.sin(angle_radian),
       (-1)*componentes[0]*math.sin(angle_radian)+
            componentes[1]*math.cos(angle_radian)
        ]
        return [origem,componentes_r]
    def rotation3DX(vetor,angle):
        angle_radian = math.radians(angle)
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [
            componentes[0],
            componentes[1]*math.cos(angle_radian)+componentes[2]*math.sin(angle_radian),
            componentes[1]*math.sin(angle_radian)*(-1)+componentes[2]*math.cos(angle_radian)
        ]
        return [origem,componentes_r]
    def rotation3DY(vetor,angle):
        angle_radian = math.radians(angle)
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [
            componentes[0]*math.cos(angle_radian)+componentes[2]*math.sin(angle_radian),
            componentes[1],
            componentes[0]*math.sin(angle_radian)*(-1)+componentes[2]*math.cos(angle_radian)
        ]
        return [origem,componentes_r]
    def rotation3DZ(vetor,angle):
        angle_radian = math.radians(angle)
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [
            componentes[0]*math.cos(angle_radian)+componentes[1]*math.sin(angle_radian),
            componentes[0]*math.sin(angle_radian)*(-1)+componentes[1]*math.cos(angle_radian),
            componentes[2]
        ]
        return [origem,componentes_r]
    def reflection2DX(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [(-1)*componentes[0],componentes[1]]
        return [origem,componentes_r]
    def reflection2DY(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [componentes[0],componentes[1]*(-1)]
        return [origem,componentes_r]
    def reflection3DX(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [componentes[0]*(-1),componentes[1],componentes[2]]
        return [origem,componentes_r]
    def reflection3DY(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [componentes[0],componentes[1]*(-1),componentes[2]]
        return [origem,componentes_r]
    def reflection3DZ(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_r = [componentes[0],componentes[1],componentes[2]*(-1)]
        return [origem,componentes_r]
    def shearing(vetor,kx,ky):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_s = [
            componentes[0]+kx*componentes[1],
            componentes[0]*ky+componentes[1]
        ]
        return [origem,componentes_s]
    def projection2DX(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_p = [componentes[0],0]
        return [origem,componentes_p]
    def projection2DY(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_p = [0,componentes[1]]
        return [origem,componentes_p]
    def projection3DX(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_p = [componentes[0],0,0]
        return [origem,componentes_p]
    def projection3DY(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_p = [0,componentes[1],0]
        return [origem,componentes_p]
    def projection3DZ(vetor):
        origem = vetor[0]
        componentes = vetor[1]
        componentes_p = [0,0,componentes[1]]
        return [origem,componentes_p]
