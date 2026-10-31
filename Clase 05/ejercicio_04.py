"""
    Programación Orientada a Objetos (POO)
    Participación
Requerimientos:
- Crear una clase Alumno
- Debe tener un atributo de nacionalidad con el valor de "Peruano"
- Crear un método que indicará el promedio del alumno
- Tendrá 3 notas para 3 cursos (Cálculo II, Matemática Discreta y Redes neuronales), la nota inicial de c/u será de 0
(puedes basarte en diccionarios)
- Crear un método donde indicará qué curso fue que tuvo la mayor nota
- Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio  (>= 13)
- Las notas serás pasadas por parámetro al momento de instanciar la clase
- Habrá un método adicional para obtener el nombre y distrito de residencia del alumno
-  Instanciar la clase para el caso de 2 alumnos por lo menos

Entregar solución al correo: docente.cerseu.unmsm@gmail.com
Asunto: Participación  - Examen final
Entrega máxima: 8:00 pm - 28 de Set.
"""

class Alumno:

    def __init__(self, nota_1=0, nota_2=0, nota_3=0):
        self.nacionalidad = "Peruano"
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3

    def promedio(self):
        pass

    def aprobado(self):
        pass

alumno_1 = Alumno(13, 15, 11)
alumno_2 = Alumno()