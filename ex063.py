def fibonacci(n):
  """
  Função recursiva para calcular o n-ésimo termo da sequência de Fibonacci.

  Args:
    n: O número do termo da sequência que deseja calcular.

  Returns:
    O n-ésimo termo da sequência de Fibonacci.
  """
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
  """
  Função principal que solicita o número de termos da sequência de Fibonacci e imprime a sequência.
  """
  numero_termos = int(input("Digite o número de termos da sequência de Fibonacci: "))
  print("Sequência de Fibonacci:")
  for i in range(numero_termos):
    print(fibonacci(i))


if __name__ == "__main__":
  main()
