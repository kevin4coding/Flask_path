# Flask Learning Path

## How to run Flask web server on real time
**Introduction**  
Flask is using Werkzeug library for allowing 'auto reload' function available that can be enabled by doing one of the following:
`app.run(debug=True)`
or
`app.debug=True`

## Templates Engine in Flask ##
### Jinja2 template engine ###
This is where one can take advantage of Jinja2 template engine, on which Flask is based. Instead of returning hardcode HTML from the function, a HTML file can be rendered by the render_template() function.

### Location ### 
Flask will try to find the HTML file in the templates folder, in the same folder in which this script is present. The term ‘web templating system’ refers to designing an HTML script in which the variable data can be inserted dynamically. A web template system comprises of a template engine, some kind of data source and a template processor.

### Syntax ###
Flask uses jinja2 template engine. A web template contains HTML syntax interspersed placeholders for variables and expressions (in these case Python expressions) which are replaced values when the template is rendered.
The jinja2 template engine uses the following delimiters for escaping from HTML.

- {% ... %} for Statements
- {{ ... }} for Expressions to print to the template output
- {# ... #} for Comments not included in the template output
- \# ... ## for Line Statements
