import click

GLOBAL_VARABLE = 100


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')

@click.option('--do_magic', is_flag=True,
              help='Enables magic option')
def hello(count, name, do_magic):
    """Simple program that greets NAME for a total of COUNT times."""
    if do_magic:
        print('magic option enabled!')

    for x in range(count):
        click.echo('Hello %s!' % name)





if __name__ == '__main__':
    x= 5
    hello()

    print(GLOBAL_VARABLE)