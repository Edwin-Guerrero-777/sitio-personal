from django.test import SimpleTestCase
from django.urls import reverse


class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertTemplateUsed(respuesta, "inicio.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")


class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/acerca-de/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertTemplateUsed(respuesta, "acerca_de.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertContains(respuesta, "Me llamo Edwin")


class PruebasPaginaProyectos(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/proyectos/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("proyectos"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("proyectos"))
        self.assertTemplateUsed(respuesta, "proyectos.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("proyectos"))
        self.assertContains(respuesta, "<h1>Proyectos</h1>")


class PruebasPaginaCuadrado(SimpleTestCase):
    def test_cuadrado_de_siete(self):
        respuesta = self.client.get(reverse("cuadrado", args=[7]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "49")

    def test_cuadrado_con_texto_da_404(self):
        respuesta = self.client.get("/cuadrado/abc/")
        self.assertEqual(respuesta.status_code, 404)
