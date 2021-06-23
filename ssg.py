import typer
from ssg.site import Site

def main(source="content", dest="default"):
    config = {"source":source, "dest":dest}
    Site({**config}).build()

typer.run(main)

