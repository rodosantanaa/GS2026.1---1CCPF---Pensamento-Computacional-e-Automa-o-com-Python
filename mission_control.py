nome_missao = "Orion Test Alpha"
nome_equipe = "Equipe Apollo"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Ordem: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

pontuacao_areas = [0, 0, 0, 0, 0] 

# --- FUNÇÕES DE ANÁLISE ---

def analisar_temperatura(temp):
    # Regras de temperatura
    if temp < 18 or (temp > 30 and temp <= 35):
        return 1, "ATENÇÃO", "Temperatura elevada/baixa"
    elif temp >= 18 and temp <= 30:
        return 0, "NORMAL", "Temperatura estável"
    else:
        return 2, "CRÍTICO", "Risco de superaquecimento"

def analisar_comunicacao(com):
    # Regras de comunicação
    if com < 30:
        return 2, "CRÍTICO", "Comunicação em nível crítico"
    elif com >= 30 and com <= 59:
        return 1, "ATENÇÃO", "Comunicação instável"
    else:
        return 0, "NORMAL", "Comunicação estável"

def analisar_bateria(bat):
    # Regras de bateria
    if bat < 20:
        return 2, "CRÍTICO", "Bateria em nível crítico"
    elif bat >= 20 and bat <= 49:
        return 1, "ATENÇÃO", "Bateria abaixo do recomendado"
    else:
        return 0, "NORMAL", "Energia estável"

def analisar_oxigenio(oxi):
    # Regras de oxigênio
    if oxi < 80:
        return 2, "CRÍTICO", "Oxigênio em nível crítico"
    elif oxi >= 80 and oxi <= 89:
        return 1, "ATENÇÃO", "Oxigênio abaixo do ideal"
    else:
        return 0, "NORMAL", "Oxigênio adequado"

def analisar_estabilidade(est):
    # Regras de estabilidade
    if est < 40:
        return 2, "CRÍTICO", "Estabilidade operacional crítica"
    elif est >= 40 and est <= 69:
        return 1, "ATENÇÃO", "Estabilidade operacional reduzida"
    else:
        return 0, "NORMAL", "Estabilidade operacional adequada"

def classificar_ciclo(pontuacao_total):
    # Classificação do risco total do ciclo
    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL", "Manter operação normal e continuar monitoramento."
    elif pontuacao_total <= 5:
        return "MISSÃO EM ATENÇÃO", "Monitorar sistemas em atenção e preparar plano."
    else:
        return "MISSÃO CRÍTICA", "Ativar modo de segurança e priorizar suporte à vida."

# --- PROCESSAMENTO PRINCIPAL ---

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

risco_primeiro_ciclo = 0
risco_ultimo_ciclo = 0
ciclo_mais_critico = 0
maior_risco_registrado = -1
ciclos_criticos = 0
soma_medias = [0, 0, 0, 0, 0]

# Estrutura de repetição para percorrer os ciclos 
for i in range(len(dados_missao)):
    ciclo_atual = i + 1
    dados = dados_missao[i]
    
    # Extraindo dados
    temp = dados[0]
    com = dados[1]
    bat = dados[2]
    oxi = dados[3]
    est = dados[4]
    
    # Somando para cálculo de médias
    for j in range(5):
        soma_medias[j] += dados[j]
    
    # Analisando cada parâmetro
    pts_temp, class_temp, rec_temp = analisar_temperatura(temp)
    pts_com, class_com, rec_com = analisar_comunicacao(com)
    pts_bat, class_bat, rec_bat = analisar_bateria(bat)
    pts_oxi, class_oxi, rec_oxi = analisar_oxigenio(oxi)
    pts_est, class_est, rec_est = analisar_estabilidade(est)
    
    # Atualizando pontos acumulados por área
    pontuacao_areas[0] += pts_temp
    pontuacao_areas[1] += pts_com
    pontuacao_areas[2] += pts_bat
    pontuacao_areas[3] += pts_oxi
    pontuacao_areas[4] += pts_est
    
    # Cálculo de risco por ciclo
    pontuacao_ciclo = pts_temp + pts_com + pts_bat + pts_oxi + pts_est
    
    # Classificação de cada ciclo
    classificacao, recomendacao_geral = classificar_ciclo(pontuacao_ciclo)
    
    # Registrando estatísticas gerais
    if i == 0:
        risco_primeiro_ciclo = pontuacao_ciclo
    if i == (len(dados_missao) - 1):
        risco_ultimo_ciclo = pontuacao_ciclo
        
    if pontuacao_ciclo > maior_risco_registrado:
        maior_risco_registrado = pontuacao_ciclo
        ciclo_mais_critico = ciclo_atual
        
    if classificacao == "MISSÃO CRÍTICA":
        ciclos_criticos += 1

    # Exibindo resultados do ciclo no terminal
    print(f"\nCICLO {ciclo_atual}")
    print(f"Temperatura: {temp} °C | {class_temp} | {rec_temp}")
    print(f"Comunicação: {com}% | {class_com} | {rec_com}")
    print(f"Bateria: {bat}% | {class_bat} | {rec_bat}")
    print(f"Oxigênio: {oxi}% | {class_oxi} | {rec_oxi}")
    print(f"Estabilidade: {est}% | {class_est} | {rec_est}")
    print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao_geral}")

# --- RELATÓRIO FINAL ---

# Análise de tendência
tendencia = ""
if risco_ultimo_ciclo > risco_primeiro_ciclo:
    tendencia = "A missão apresentou tendência de piora."
elif risco_ultimo_ciclo < risco_primeiro_ciclo:
    tendencia = "A missão apresentou tendência de melhora."
else:
    tendencia = "A missão permaneceu estável em relação ao início."

# Identificação da área mais afetada
maior_pontuacao_area = -1
indice_area_afetada = 0
for i in range(len(pontuacao_areas)):
    if pontuacao_areas[i] > maior_pontuacao_area:
        maior_pontuacao_area = pontuacao_areas[i]
        indice_area_afetada = i

area_mais_afetada = areas_monitoradas[indice_area_afetada]

# Cálculo do risco médio
risco_medio = sum(pontuacao_areas) / len(dados_missao)

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"\nQuantidade de ciclos analisados: {len(dados_missao)}")

print(f"\nMédia de temperatura: {soma_medias[0]/len(dados_missao):.2f} °C")
print(f"Média de comunicação: {soma_medias[1]/len(dados_missao):.2f}%")
print(f"Média de bateria: {soma_medias[2]/len(dados_missao):.2f}%")
print(f"Média de oxigênio: {soma_medias[3]/len(dados_missao):.2f}%")
print(f"Média de estabilidade: {soma_medias[4]/len(dados_missao):.2f}%")

print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco_registrado}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {ciclos_criticos}")

print(f"\nTendência da missão:\n{tendencia}")

print("\nPontuação acumulada por área:")
for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

print(f"\nÁrea mais afetada:\n{area_mais_afetada}")

# Classificação final baseada no último ciclo ou risco médio
classificacao_final, _ = classificar_ciclo(risco_ultimo_ciclo)
print(f"\nClassificação final da missão (Baseada no último ciclo):\n{classificacao_final}")
print("=" * 60)
