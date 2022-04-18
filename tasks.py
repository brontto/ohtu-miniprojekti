from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def initialize(ctx):
    ctx.run("python3 src/initialize_database.py", pty=True)

@task
def robot_test(ctx):
    ctx.run("robot src/tests/robot", pty=True)

@task
def robot_start(ctx):
    ctx.run("dotenv -f .env.test run -- python3 src/index.py", pty=True)