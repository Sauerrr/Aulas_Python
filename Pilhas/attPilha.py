class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)- 1]
    
    def size(self):
        return len(self.items)

pilhaCopos = Stack()

# Estamos num bar, e estamos tomando Whisky. A cada copo que tomamos o garçom leva embora.

pilhaCopos.push('Copo 1')
pilhaCopos.push('Copo 2')
pilhaCopos.push('Copo 3')
print(pilhaCopos.items)

#O primeiro copo foi tomado:
print(pilhaCopos.peek())
pilhaCopos.pop()
print(pilhaCopos.items)

#O segundo copo foi tomado:
print(pilhaCopos.peek())
pilhaCopos.pop()
print(pilhaCopos.items)

#O Terceiro copo foi tomado:
print(pilhaCopos.peek())    
pilhaCopos.pop()
print(pilhaCopos.items)