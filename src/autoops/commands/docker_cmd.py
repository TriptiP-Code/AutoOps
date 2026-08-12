import docker


def docker_ps():

    try:

        client = docker.from_env()

        containers = client.containers.list()

        if len(containers) == 0:
            print("No running containers.")
            return

        print("=" * 80)
        print(f"{'NAME':25} {'STATUS':15} IMAGE")
        print("=" * 80)

        for container in containers:

            image = (
                container.image.tags[0]
                if container.image.tags
                else "Unknown"
            )

            print(
                f"{container.name:25}"
                f"{container.status:15}"
                f"{image}"
            )

    except Exception as e:
        print(f"❌ {e}")