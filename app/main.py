import typer
from rich import print
from app.aws import get_caller_identity

app = typer.Typer()


@app.command()
def audit():
    print("Starting AWS audit...")


@app.command()
def version():
    print("CloudGuard v1.0.0")


@app.command()
def config():
    identity = get_caller_identity()

    if identity is None:
        print("[red]AWS credentials not found.[/red]")
        print("Run: aws configure")
        return

    print("[green]Connected to AWS[/green]\n")

    print(f"Account ID : {identity['Account']}")
    print(f"User ARN   : {identity['Arn']}")
    print(f"User ID    : {identity['UserId']}")


if __name__ == "__main__":
    app()
