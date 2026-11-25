from django.shortcuts import render
from django.views.generic import TemplateView


def vista_inicio(request):
    contexto = {
        "habilidades": ["Python", "Django", "Git"],
        "mensaje": "GRACIAS por VISITAR mi sitio.",
    }
    return render(request, "inicio.html", contexto)


class VistaAcercaDe(TemplateView):
    template_name = "acerca_de.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nombre"] = "Edwin"
        contexto["edad"] = 22
        return contexto


class VistaProyectos(TemplateView):
    template_name = "proyectos.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["proyectos"] = [
            "Tienda en línea",
            "Blog personal",
            "App de tareas",
        ]
        return contexto


def vista_cuadrado(request, numero):
    contexto = {
        "numero": numero,
        "resultado": numero * numero,
    }
    return render(request, "cuadrado.html", contexto)
