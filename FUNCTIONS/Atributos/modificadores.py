"""int modificadores (int valor){
	 if (valor == 1) {
        return -3;
    } else if (valor >= 2 && valor <= 4) {
        return -2;
    } else if (valor >= 5 && valor <= 7) {
        return -1;
    } else if (valor >= 8 && valor <= 11) {
        return 0;
    }  else if (valor >= 12 && valor <= 14) {
        return 1;
	} else if (valor >= 15 && valor <= 17) {
        return 2;
	}else {
		return 3;
    }
}"""

def modificadores(valor):
    if valor == 1:
        return -3
    elif valor >=2 and valor <=4:
        return -2
    elif valor >= 5 and valor <= 7:
        return -1
    elif valor >= 8 and valor <= 11:
        return 0
    elif valor >= 12 and valor <= 14:
        return 1
    elif valor >= 15 and valor <= 17:
        return 2
    else:
        return 3