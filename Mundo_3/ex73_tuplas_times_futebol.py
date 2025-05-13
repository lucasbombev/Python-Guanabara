'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

times = ('Palmeiras','Flamengo','Bragantino','Cruzeiro','Fluminense','Ceará','Atlético-MG','Bahia','Botafogo','Corinthians','Fortaleza','Mirassol','Internacional','Vitória','Grêmio','São Paulo','Vasco da Gama','Juventude','Santos','Sport Recife')
primeiros = times[0:5]
ultimos = times[-4:20]
print(20*"-=")
print(f"Os 5 primeiros são {primeiros}")
print(20*"-=")
print(f"Os 4 últimos são {ultimos}")
print(20*"-=")
print(f"Times em ordem alfabética: {sorted(times)}")
print(20*"-=")
print(f"O time que está na 8ª colocação é o {times[7]}")