# Sistema de Tipos
Ø (): (En cualquier ámbito, en el ámbito global)</br>
Γ (Gamma): ambito (En un ámbito en particular)</br>
⊢ (Trinquete): a la derecha del trinquete es estrictamente verdadero </br>

Γ ⊢ M : A </br> 
M: Variable </br> 
A: Tipo de dato </br> </br> 

En el ambito gamma es estrictamente verdadero que la variable M es de tipo A.</br> 

## Tipos de datos
* int: 
    * $Ø ⊢ [0-9]: int$
* string:
    * $Ø ⊢ "[a-zA-Z0-9]": str$
* bool: 
    * $Ø ⊢ true: bool$
    * $Ø ⊢ false: bool$

## Reglas de ámbito
Ámbito estático ya que se realiza un análisis de programa fuente de manera estática y no en tiempo ejecución.

## Reglas de tipos
### Operaciones entre int

$$
Γ ⊢ a: int \\
{Γ ⊢ b: int \over a + b: int}
$$


```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[+]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[5];
      E --- G[11];
      
      A -.-|int| A;
      B -.-|int| B;
      C -.-|int| C;
      D -.-|int| D;
      E -.-|int| E;
      F -.-|int| F;
      G -.-|int| G;
```


$$
Γ ⊢ a: int \\
{Γ ⊢ b: int \over a - b: int}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[-]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[5];
      E --- G[11];
      
      A -.-|int| A;
      B -.-|int| B;
      C -.-|int| C;
      D -.-|int| D;
      E -.-|int| E;
      F -.-|int| F;
      G -.-|int| G;
```

$$
Γ ⊢ a: int \\
{Γ ⊢ b: int \over a * b: int}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[*]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[5];
      E --- G[11];
      
      A -.-|int| A;
      B -.-|int| B;
      C -.-|int| C;
      D -.-|int| D;
      E -.-|int| E;
      F -.-|int| F;
      G -.-|int| G;
```

$$
Γ ⊢ a: int \\
{Γ ⊢ b: int \over a / b: int}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H["/"]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[5];
      E --- G[11];
      
      A -.-|int| A;
      B -.-|int| B;
      C -.-|int| C;
      D -.-|int| D;
      E -.-|int| E;
      F -.-|int| F;
      G -.-|int| G;
```

</br>
</br>

### Operaciones entre string

$$
Γ ⊢ a: str \\
{Γ ⊢ b: str \over a + b: str}
$$


```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[+]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[L];
      
      A -.-|str| A;
      B -.-|str| B;
      C -.-|str| C;
      D -.-|str| D;
      E -.-|str| E;
      F -.-|str| F;
      G -.-|str| G;
```


$$
Γ ⊢ a: str \\
{Γ ⊢ b: str \over a - b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[-]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[L];
      
      A -.-|ERROR| A;
      B -.-|str| B;
      C -.-|str| C;
      D -.-|str| D;
      E -.-|str| E;
      F -.-|str| F;
      G -.-|str| G;
```

$$
Γ ⊢ a: str \\
{Γ ⊢ b: str \over a * b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[*]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[L];
      
      A -.-|ERROR| A;
      B -.-|str| B;
      C -.-|str| C;
      D -.-|str| D;
      E -.-|str| E;
      F -.-|str| F;
      G -.-|str| G;
```

$$
Γ ⊢ a: str \\
{Γ ⊢ b: str \over a / b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H["/"]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[L];
      
      A -.-|ERROR| A;
      B -.-|str| B;
      C -.-|str| C;
      D -.-|str| D;
      E -.-|str| E;
      F -.-|str| F;
      G -.-|str| G;
```

</br>
</br>

### Operaciones entre int y string
$$
Γ ⊢ a: str \\
{Γ ⊢ b: int \over a + b: ERROR}
$$


```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[+]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[11];
      
      A -.-|ERROR| A;
      B -.-|str| B;
      C -.-|int| C;
      D -.-|str| D;
      E -.-|int| E;
      F -.-|str| F;
      G -.-|int| G;
```


$$
Γ ⊢ a: str \\
{Γ ⊢ b: int \over a - b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[-]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[11];
      
      A -.-|ERROR| A;
      B -.-|str| B;
      C -.-|int| C;
      D -.-|str| D;
      E -.-|int| E;
      F -.-|str| F;
      G -.-|int| G;
```

$$
Γ ⊢ a: str \\
{Γ ⊢ b: int \over a * b: str}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[*]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[11];
      
      A -.-|str| A;
      B -.-|str| B;
      C -.-|int| C;
      D -.-|str| D;
      E -.-|int| E;
      F -.-|str| F;
      G -.-|int| G;
```

$$
Γ ⊢ a: str \\
{Γ ⊢ b: int \over a / b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H["/"]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[G];
      E --- G[11];
      
      A -.-|ERROR| A;
      B -.-|str| B;
      C -.-|int| C;
      D -.-|str| D;
      E -.-|int| E;
      F -.-|str| F;
      G -.-|int| G;
```


### Operaciones entre bool

$$
Γ ⊢ a: bool \\
{Γ ⊢ b: bool \over a + b: ERROR}
$$


```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[+]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[true];
      E --- G[false];
      
      A -.-|ERROR| A;
      B -.-|bool| B;
      C -.-|bool| C;
      D -.-|bool| D;
      E -.-|bool| E;
      F -.-|bool| F;
      G -.-|bool| G;
```


$$
Γ ⊢ a: bool \\
{Γ ⊢ b: bool \over a - b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[-]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[true];
      E --- G[false];
      
      A -.-|ERROR| A;
      B -.-|bool| B;
      C -.-|bool| C;
      D -.-|bool| D;
      E -.-|bool| E;
      F -.-|bool| F;
      G -.-|bool| G;
```

$$
Γ ⊢ a: bool \\
{Γ ⊢ b: bool \over a * b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H[*]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[true];
      E --- G[false];
      
      A -.-|ERROR| A;
      B -.-|bool| B;
      C -.-|bool| C;
      D -.-|bool| D;
      E -.-|bool| E;
      F -.-|bool| F;
      G -.-|bool| G;
```

$$
Γ ⊢ a: bool \\
{Γ ⊢ b: bool \over a / b: ERROR}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H["/"]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[true];
      E --- G[false];
      
      A -.-|ERROR| A;
      B -.-|bool| B;
      C -.-|bool| C;
      D -.-|bool| D;
      E -.-|bool| E;
      F -.-|bool| F;
      G -.-|bool| G;
```

$$
Γ ⊢ a: bool \\
{Γ ⊢ b: bool \over a \& b: bool}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H["&"]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[true];
      E --- G[false];
      
      A -.-|bool| A;
      B -.-|bool| B;
      C -.-|bool| C;
      D -.-|bool| D;
      E -.-|bool| E;
      F -.-|bool| F;
      G -.-|bool| G;
```

$$
Γ ⊢ a: bool \\
{Γ ⊢ b: bool \over a | b: bool}
$$

```mermaid
  graph TD;
      A[E] --- B[E];
      A --- H["|"]
      A --- C[E];
      B --- D[N];
      C --- E[N];
      D --- F[true];
      E --- G[false];
      
      A -.-|bool| A;
      B -.-|bool| B;
      C -.-|bool| C;
      D -.-|bool| D;
      E -.-|bool| E;
      F -.-|bool| F;
      G -.-|bool| G;
```

* Suponemos que solo las variables y metodos tienen un scope o global o local
* Todos los metodos de una clase son globales