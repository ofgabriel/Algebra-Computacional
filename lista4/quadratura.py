W = {2:{"pontos": [-0.5773502691896257,0.5773502691896257],"pesos": [1.0,1.0]},
        3:{"pontos": [0.0,-0.7745966692414834,0.7745966692414834],"pesos": [0.8888888888888888,0.5555555555555556,0.5555555555555556]},
        4:{"pontos": [-0.3399810435848563,0.3399810435848563,-0.8611363115940526,0.8611363115940526],"pesos": [0.6521451548625461,0.6521451548625461,0.3478548451374538,0.3478548451374538]},
        5:{"pontos": [0.0,-0.5384693101056831,0.5384693101056831,-0.9061798459386640,0.9061798459386640],"pesos": [0.5688888888888889,0.4786286704993665,0.4786286704993665,0.2369268850561891,0.2369268850561891]},
        6:{"pontos": [0.6612093864662645,-0.6612093864662645,-0.2386191860831969,0.2386191860831969,-0.9324695142031521,0.9324695142031521],"pesos": [0.3607615730481386,0.3607615730481386,0.4679139345726910,0.4679139345726910,0.1713244923791704,0.1713244923791704]},
        7:{"pontos": [0.0,0.4058451513773972,-0.4058451513773972,-0.7415311855993945,0.7415311855993945,-0.9491079123427585,0.9491079123427585],"pesos": [0.4179591836734694,0.3818300505051189,0.3818300505051189,0.2797053914892766,0.2797053914892766,0.1294849661688697,0.1294849661688697]}}


def quadratura(fun,a,b,np):
    # Integra no intervalo [a,b] com np pontos.
    N = (grau + 1)/2
    pesos = W.get(np).get("pesos")
    pontos = W.get(np).get("pontos")
    soma = 0
    for i in range(np):
        soma += fun(((a+b+pontos[i])*abs(b-a))/2)*pesos[i]

    return soma


