# SimularLambda.py

import TesteAutomacao

# Simulando o evento Lambda
evento = {}       # pode personalizar os dados aqui
contexto = None   # normalmente não usado em teste local

# Executar a função como se fosse a Lambda
resultado = TesteAutomacao.lambda_handler(evento, contexto)

print("Resultado da execução:")
print(resultado)
