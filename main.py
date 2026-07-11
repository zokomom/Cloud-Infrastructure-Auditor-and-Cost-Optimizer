import typer

app = typer.Typer()


@app.command()
def audit():
    print("Starting AWS audit...")


@app.command()
def version():
    print("CloudGuard v1.0.0")


@app.command()
def config():
    print("Configuration command coming soon...")


if __name__ == "__main__":
    app()
