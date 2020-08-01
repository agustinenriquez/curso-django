from django import template

register = template.Library()


@register.simple_tag()
def process_course_image_path_script():
    return """<script>
        let imagen_curso = document.querySelector(\'img[id=imagen-curso]\');
        imagen_curso.src = imagen_curso.src.slice(imagen_curso.src.indexOf(\'static\')-1);
        </script>"""
