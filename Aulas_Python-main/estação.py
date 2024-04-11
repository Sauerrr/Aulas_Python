
mes = input("Digite um mes do ano:")
if mes in ("Dezembro", "Janeiro", "Fevereiro"):
    Categoria = "Verão"
elif mes in ("Março", "Abril", "Maio"):
    Categoria = "Outono"
elif mes in ("Junho" ,"Julho" , "Agosto" ):
    Categoria = "Inverno"
else:
    Categoria = "Primavera"

print(f"A estação é:{Categoria}")