import jinja2


string_template = """
Hi {{ nome }},

SYour jey has expired and your computer is about to explode if you do nothing.
click below to be hacked:

{{ link }}

{% for idx in lista_de_numeros %}
{{ idx }}
{% endfor %}

"""

template = jinja2.Template(string_template)
redered_template = template.render({
    "nome": "Lojas Renner",
    "link": "http://caixaeconomica02.com.br",
    "lista_de_numeros": [1, 2, 3, 4, 5]
})

print(redered_template)

