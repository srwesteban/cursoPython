class Alumno:
    Nombre = None
    Nota = None

    def __init__(self,nombre,nota):
        self.Nombre = nombre
        self.Nota = nota

    def __str__(self):
        return f"Alumno: {self.Nombre} Nota: {self.Nota}" 
    
    def aprobado(Alunmo):
        if nuevoAlumno.Nota>= 3:
            return "aprobado"
        else:
            return "reprobado"
            
            
nuevoAlumno = Alumno("William Esteban",5)

print(nuevoAlumno)
evaluacion = Alumno.aprobado(nuevoAlumno)

print(evaluacion)