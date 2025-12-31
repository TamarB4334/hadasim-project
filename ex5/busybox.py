import docker

client = docker.from_env()


container = client.containers.run(
    "busybox",
    "sleep 3600",
    detach=True
)

result = container.exec_run("hostname")

print(result.output.decode())