"""void AtD20(int *dadosmatriz, int qntdados) {
    for (int i = 0; i < qntdados; i++) {
        dadosmatriz[i] = (rand() % 20) + 1;
    }
}"""
import random

def AtD20(qntDados):
    dadosMatriz = []
    for i in range (0, qntDados):
        dadosMatriz.append(random.randint(0, 20))
    return dadosMatriz
