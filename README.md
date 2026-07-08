# Recorrido por Niveles en un Árbol Binario

## Descripción

Este proyecto implementa el algoritmo **Level Order Traversal**  para un árbol binario de búsqueda (Binary Search Tree - BST).

El recorrido por niveles visita los nodos **nivel por nivel**, comenzando desde la raíz y recorriendo cada nivel de izquierda a derecha.

Para realizar el recorrido se utiliza una **cola (Queue)** implementada mediante una lista de Python.

---

## Estructura del proyecto

El programa contiene:

* **Node:** representa un nodo del árbol.
* **BinarySearchTree:** permite crear e insertar nodos en el árbol.
* **levelOrder(root):** realiza el recorrido por niveles.

---

## Árbol de ejemplo

Los valores insertados son:

```text
4, 2, 7, 1, 3, 6, 9
```

El árbol construido es:

```text
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```

---

## Salida esperada

```text
Recorrido Level Order:
4 2 7 1 3 6 9
```

---

## Funcionamiento del algoritmo

1. Verifica que el árbol no esté vacío.
2. Crea una cola e inserta la raíz.
3. Mientras la cola tenga elementos:

   * Extrae el primer nodo.
   * Imprime su valor.
   * Agrega el hijo izquierdo (si existe).
   * Agrega el hijo derecho (si existe).
4. Finaliza cuando la cola queda vacía.

---

## Complejidad

### Complejidad temporal

En esta implementación la cola se maneja mediante una lista de Python.

La operación:

```python
queue.pop(0)
```

elimina el primer elemento de la lista y desplaza los restantes una posición hacia la izquierda, por lo que tiene un costo de **O(n)**.

Como esta operación se realiza para cada uno de los **n** nodos del árbol, la complejidad temporal total es:

```text
O(n²)
```

---

### Complejidad espacial

La cola puede almacenar hasta un número proporcional de nodos del árbol en el peor caso.

Por ello, la complejidad espacial es:

```text
O(n)
```

---

## Ejecución

Ejecute el archivo con Python:

```bash
python nombre_del_archivo.py
```

No es necesario instalar librerías adicionales, ya que la implementación utiliza únicamente estructuras de datos básicas de Python.
