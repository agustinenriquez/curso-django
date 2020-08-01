from django import template

register = template.Library()


@register.simple_tag()
def process_course_image_path_script():
    return """
        let imagen_curso = document.querySelector(\'img[id=imagen-curso]\');
        imagen_curso.src = imagen_curso.src.slice(imagen_curso.src.indexOf(\'static\')-1);
        """


@register.simple_tag()
def print_console_log():
    return "console.log('Hello world, im coding js using python')"


@register.simple_tag()
def test_jquery():
    return "$('div').toArray().forEach((e)=>{console.log(e)})"
