
def funcao_teste(a:str, b:int) -> str:
    return str(a * b)

print(funcao_teste(1,2))


def uma_funcao_documentada(*args, **kwargs) -> float:
    """
    retorna o resultado da operação matematica com os números informados
    
    args:
      param1 (int): primeiro valor do calculo
      param2 (int): segundo valor do calculo
      paramN (int): demais valores para o calculo
    kwargs:
      oper (string): simbolo da operação do calculo
        '+' para soma
        '-' para subtração
        '*' para multiplicação
        '/' para divisção
    """
    pass

uma