from prefect import flow

@flow
def my_flow():
    return 1

# prefect --no-prompt deploy --all

# prefect deployment run 'my-flow/idc'

# prefect worker start --pool 'docker-work'