# The AI Munshi - Backend

## Set up

1. Build the image:

   ```bash
   docker build -t theaimunshi-backend .
   ```
2. Run the container in development mode:

   ```bash
   docker run -p 8000:80 -v "$(pwd)":/app -v /app/.venv theaimunshi-backend
   ``` 


## Dockerfile


```dockerfile
FROM python:3.12-slim-trixie
```

  * **What it does:** Sets the base operating system.
  * **Details:** Uses Python 3.12 running on a lightweight version ("slim") of Debian Trixie. This ensures the image is small and secure.

<!-- end list -->

```dockerfile
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
```

  * **What it does:** Installs the `uv` package manager.
  * **Details:** Instead of using `pip install`, this copies the pre-compiled `uv` binary directly from Astral's official image into our container's `/bin` folder.

<!-- end list -->

```dockerfile
ADD . /app
```

  * **What it does:** Moves your code.
  * **Details:** Copies all files from your local project directory into a directory named `/app` inside the container.

<!-- end list -->

```dockerfile
WORKDIR /app
```

  * **What it does:** Sets the context.
  * **Details:** Tells Docker that all subsequent commands (like `RUN` or `CMD`) should be executed inside the `/app` folder.

<!-- end list -->

```dockerfile
RUN uv sync --locked
```

  * **What it does:** Installs dependencies.
  * **Details:** Uses `uv` to create a virtual environment and install the packages listed in `pyproject.toml`/`uv.lock`. The `--locked` flag ensures the installation exactly matches your lockfile versioning.

<!-- end list -->

```dockerfile
CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "80", "--reload"]
```

  * **What it does:** Starts the application.
  * **Details:**
      * `uv run`: Runs the command inside the managed virtual environment.
      * `fastapi run`: Starts the FastAPI server.
      * `--port 80`: The internal container port.
      * `--reload`: Enables auto-reloading when code changes are detected.

-----

## Building the Image

To create the Docker image from the Dockerfile, use the following command:

```bash
docker build -t theaimunshi-backend .
```

**Flag Breakdown:**

  * **`docker build`**: The command to generate an image.
  * **`-t theaimunshi-backend`**: "Tags" (names) the image `theaimunshi-backend` so you can easily refer to it later.
  * **`.`**: Tells Docker to look for the `Dockerfile` in the **current directory**.

-----

## Running the Container (Development Mode)

To run the container with **hot-reloading enabled** (so you don't have to restart Docker when you change code), use this command:

```bash
docker run -p 8000:80 -v "$(pwd)":/app -v /app/.venv theaimunshi-backend
```

**Flag Breakdown:**

  * **`-p 8000:80` (Port Mapping)**

      * Maps port **8000** on your computer (Host) to port **80** inside the container.
      * You can access the API at `http://localhost:8000`.

  * **`-v "$(pwd)":/app` (Code Sync)**

      * **What it does:** Mounts your current local directory (`pwd`) to the `/app` folder inside the container.
      * **Why:** This creates a live link. When you save a file in VS Code, it instantly updates inside the container, triggering FastAPI to reload.

  * **`-v /app/.venv` (Environment Protection)**

      * **What it does:** Creates an "anonymous volume" for the virtual environment folder.
      * **Why:** This is critical\! Without this, the previous flag (`-v "$(pwd)":/app`) would overwrite the container's installed dependencies with your local folder (which might not have the correct Linux dependencies). This flag tells Docker: *"Sync my code, but keep the container's internal `.venv` folder safe and untouched."*

  * **`theaimunshi-backend`**

      * The name of the image to run (must match the tag you used in the build step).