import apurar_concurso
import atualizar_estatisticas


def apresentacao_inicial():
    while True :
        try:
            opcao=input(""" \n
            selecione uma opção valida:
            1-Registrar novos concursos
            2-Atualizar estatisticas no banco de dados
            Digite aqui sua respostas:  """)
            opcao= int(opcao)
        except Exception as e:
            print("Ocorreu um erro! Por favor escolha uma opção válida")

        if opcao == 1 or opcao == 2:
            break
        else:
            continue
    return opcao




def opcoes_atualizarbd(opcao):
    
    while True:
        try:
            resposta=int(input("""\n Escolha o tipo de jogo:
            1-Lotofácil
            2-Lotomania
            3-Mega-Sena
                Digite aqui sua respostas: """))
        
               
        except Exception as e:
            print("Ocorreu um erro! Por favor escolha uma opção válida")

        if resposta == 1 or resposta == 2 or resposta == 3:           
            jogo=modo_de_jogo(resposta)
            concurso=1
        if opcao == 1:
            while True:
                try:
                    concurso=int(input("""Em qual concurso parou?
                    Digite aqui sua respostas: """))
                    
                        
                except Exception as e:
                    print("Ocorreu um erro! Por favor digite apenas os numeros do concurso")

                break
        break
       
    return jogo,concurso
    
def modo_de_jogo(tipo_jogo):
    if tipo_jogo == 1:
        tipo_jogo = 'Lotofacil'
    elif tipo_jogo == 2:
        tipo_jogo = "Lotomania"
    elif tipo_jogo == 3:
        tipo_jogo = "Mega-Sena"
    return tipo_jogo

    

#incia o programa
opcao = apresentacao_inicial()


if opcao == 1:
    jogo,ultimo_concurso=opcoes_atualizarbd(opcao)

    #instancia a classe
    insertbd=apurar_concurso.Loteria(jogo)
    insertbd.obter_resultado()
    print("Realizado com sucesso!")

elif opcao == 2:
    modojogo,ultimo_concurso=opcoes_atualizarbd(opcao)

    #instancia a classe
    atualizebd=atualizar_estatisticas.Atualizarbd(modojogo,ultimo_concurso)
    #executa os metodos
    atualizebd.modo_jogo()
    atualizebd.analise_individual()
    atualizebd.analise_geral_freq()
    atualizebd.analise_geral_par_impar()
    atualizebd.analise_geral_soma_total()
    atualizebd.quantoTempoNaoSai()
    atualizebd.atualizado_em()
    
    print("Realizado com sucesso!")


   

    
    

    
