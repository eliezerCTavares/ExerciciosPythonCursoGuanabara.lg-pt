def notas(*nts,sit=False):
    """ Função mostra situação e analisa notas do aluno: 
    :parâmetro nts: quantidade variável de notas.
    :parâmetro sit: valor opcional, para retornar ou não a situação do aluno.
    :return: retorna um dicionário com várias informações do aluno.
    """

    nt_dic = {}
    nt_dic ["Notas"] = len(nts)
    nt_dic ["Max"] = max(nts)
    nt_dic ["Min"] = min(nts)
    nt_dic ["media"] = sum(nts) / len(nts)

    if sit==True:
        if nt_dic ["media"] >=7:
            nt_dic ["sit"] = "Aprovado"
        elif nt_dic ["media"] >=5:
            nt_dic ["sit"] = "Recuperação"
        else:
            nt_dic ["sit"] = "Reprovado"

    return nt_dic


resp = notas (5.7, 7.3, 8.35, sit=True)
for x,z in resp.items():
    print(f"{x}: {z}", end=" | ")