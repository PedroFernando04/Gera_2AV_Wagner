"""int atribuirAtributo(int numerodoDado, int *dadosatb, int *dadosUtilizados) {
    if (dadosUtilizados[numerodoDado - 1]) {

        return -1;
    }
    dadosUtilizados[numerodoDado - 1] = 1;// Marcar o dado como utilizado
    return dadosatb[numerodoDado - 1];
}"""

def atribuir_atributo(numero_dado, dados_atb, dados_utilizados):
    if dados_utilizados[numero_dado - 1]:
        return -1
    dados_utilizados[numero_dado - 1] = 1

    return dados_atb[numero_dado - 1]

