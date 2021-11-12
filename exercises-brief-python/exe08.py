# Exercise 8: Widgets and Gizmos
# (15 Lines)
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos from the user. Then your program should compute
# and display the total weight of the parts.

widgets = int(input('Informe a quantidade de Widgets: '))
gizmo = int(input('Informe a quantidade de gizmos: '))


def pesoTotal(w, g):
    peso_total_w = widgets * 75
    peso_total_g = gizmo * 112
    print(f'Peso total de widgets: {peso_total_w:.2f} gramas')
    print(f'Peso total de gizmo: {peso_total_g:.2f} gramas')

### Chamando a função:
pesoTotal(widgets, gizmo)

