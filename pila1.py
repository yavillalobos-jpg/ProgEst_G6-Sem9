stack = []

def push(item, capacity):
    if not is_full(capacity):
      stack.append(item)
      return "Elemento apilado...."
    return "La pila esta llena"

def isEmpty():
    return not len(stack)

def is_full(capacity):
    return len(stack) == capacity

def peek():
    if not isEmpty():
        return stack[-1]
    return "La pila esta vacia"

def pop():
    if not isEmpty():
        return stack.pop()
    return "La pila esta vacia"

def show():
   message = ""
   for item in reversed(stack):
         message += f"|{item:>6} |\n"
         message += f"└" + "─"* 8 + "┘\n"
   return message

capacity = int(input("Dime el tamaño de la pila: "))
while True:
    item = input("Dime un valor: ")
    print(push(item, capacity))
    answer = input("Desea agregar otro elemento? (s/n): ")
    if answer.lower() == "n":
        break

print("Mostrar tope")
print(peek())
print(peek())


print("Desapilae")
while True:
    if answer.lower() == "s":
     print(pop())
    elif answer.lower() == "n":
      break
    else:
     print("Opcion no valida")

