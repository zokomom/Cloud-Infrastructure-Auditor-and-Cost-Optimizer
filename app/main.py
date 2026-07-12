import typer
from rich import print
from app.aws import get_caller_identity, get_region, get_profile

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
        print("[red]AWS credentials not configured[/red]")
        print("Run: aws configure")
        return
    print("\n", end="")
    print("[bold green]CloudGuard Configuration[/bold green]\n")

    print(f"Profile    : {get_profile()}")
    print(f"Region     : {get_region()}")
    print(f"Account ID : {identity['Account']}")
    print(f"User ARN   : {identity['Arn']}")
