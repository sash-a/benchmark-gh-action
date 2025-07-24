FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
# Disable Python downloads, because we want to use the system interpreter
# across both images. If using a managed Python version, it needs to be
# copied from the build image into the final image; see `standalone.Dockerfile`
# for an example.
ENV UV_PYTHON_DOWNLOADS=0
WORKDIR /app

COPY pyproject.toml /app
COPY uv.lock /app

RUN uv sync --locked --no-dev

FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy the virtual environment and application from the builder stage
COPY --from=builder /app /app
COPY app.py /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
