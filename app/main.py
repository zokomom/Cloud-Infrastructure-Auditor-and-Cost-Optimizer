import typer
from rich import print
from app.aws import get_caller_identity, get_region, get_profile
from app.ebs import get_unattached_volumes
from app.eip import get_unassociated_eips

app = typer.Typer()


@app.command()
def audit():
    print("[bold blue]Scanning AWS Infrastructure...[/bold blue]\n")
    try:
        volumes = get_unattached_volumes()

        if not volumes:
            print("[green]✓ No unattached EBS volumes found.[/green]")
        else:
            print(
                f"[yellow]Found {len(volumes)} unattached volume(s)[/yellow]\n")

            for volume in volumes:
                print(
                    f"ID: {volume['VolumeId']} | "
                    f"Size: {volume['Size']} GB | "
                    f"AZ: {volume['AvailabilityZone']}"
                )
    except RuntimeError as e:
        print(f"[red]Error scanning EBS volumes: {e}[/red]")

    print()

    try:
        eips = get_unassociated_eips()

        if not eips:
            print("[green]✓ No unassociated Elastic IPs found.[/green]")
        else:
            print(
                f"[yellow]Found {len(eips)} unassociated Elastic IP(s):[/yellow]")

            for ip in eips:
                print(f"  • {ip['PublicIp']}")
    except RuntimeError as e:
        print(f"[red]{e}[/red]")


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
