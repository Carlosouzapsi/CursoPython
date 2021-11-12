limite_min_plano = int(input('Informe a quantidade de minutos: '))
limite_msg_plano = int(input('Informe a quantidade de mensagens: '))

def verifica_plano(num_min, num_msg):
    cobranca = 0
    if num_min <= 50 and num_msg <= 50:
        cobranca = 15
    elif num_min >= 50:
        cobranca = 15 + num_min * 0.25
    elif num_msg >= 50:
        cobranca = 15 + num_msg * 0.15
    elif num_min >= 50 and num_msg >= 50:
        cobranca = 15 + (num_min * 0.25) + (num_min * 0.15)
    return cobranca

taxas_call_center = verifica_plano(limite_min_plano,limite_msg_plano) * 0.44
add_limite_cobranca_msg = (limite_min_plano - 50) * 0.15
add_limite_cobranca_min = (limite_min_plano - 50) * 0.25
impostos_gerais = (verifica_plano(limite_min_plano, limite_msg_plano) + taxas_call_center) * 0.5
valor_total = (verifica_plano(limite_min_plano, limite_msg_plano)) + taxas_call_center + impostos_gerais
print(f'Minutos a mais de uso do plano em ligações: {limite_min_plano - 50}')
print(f'SMS a mais de uso do plano em mensagens de texto: {limite_msg_plano - 50}')
print(f'Adicional cobrado em mensagens: {add_limite_cobranca_msg} U$')
print(f'Adicional cobrado em mensagens: {add_limite_cobranca_min} U$')
print(f'Total de Taxas Call Center: {taxas_call_center:.2f} U$')
print(f'Imposto sob o total: {impostos_gerais:.2f} U$')
print(f'Valor total da conta de telefone: {valor_total:.2f} U$')














