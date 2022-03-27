import os
from subprocess import call


def set_environment_values():
    with open("docker.env", "w") as docker_env:
        kaggle_username = input("Input Kaggle Username: ")
        kaggle_key = input("Input Kaggle API Key: ")
        docker_env.write(f"KAGGLE_USERNAME={kaggle_username}\n")
        docker_env.write(f"KAGGLE_KEY={kaggle_key}\n")
        docker_env.write("MINIO_ROOT_USER=minioadmin\n")
        docker_env.write("MINIO_ROOT_PASSWORD=minioadmin\n")
        docker_env.write(
            "DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres\n"
        )


def build_images():
    call(["docker-compose", "build"])


if __name__ == "__main__":
    set_environment_values()
    build_images()
