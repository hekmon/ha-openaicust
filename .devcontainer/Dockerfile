FROM mcr.microsoft.com/vscode/devcontainers/base:debian

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install system dependencies required by Home Assistant
RUN \
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        bluez \
        ffmpeg \
        libudev-dev \
        libavformat-dev \
        libavcodec-dev \
        libavdevice-dev \
        libavutil-dev \
        libswscale-dev \
        libswresample-dev \
        libavfilter-dev \
        libpcap-dev \
        libturbojpeg0 \
        libyaml-dev \
        libxml2 \
        git \
        cmake \
        autoconf \
        pkg-config \
        libffi-dev \
        libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add go2rtc binary for WebRTC support
COPY --from=ghcr.io/alexxit/go2rtc:latest /usr/local/bin/go2rtc /bin/go2rtc

# Copy uv (Python package manager) for fast dependency resolution
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /usr/src

USER vscode

# Set up Python virtual environment
ENV VIRTUAL_ENV="/home/vscode/.local/ha-venv"
ENV PYTHON_VERSION="3.13"

RUN uv python install ${PYTHON_VERSION} \
    && uv venv ${VIRTUAL_ENV}

ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

# Clone Home Assistant Core for development
# This provides type hints, completions, and ability to debug into HA Core
WORKDIR /workspaces/core
RUN git clone --depth 1 https://github.com/home-assistant/core.git .

# Create config directory structure for custom component
RUN mkdir -p /workspaces/core/config/custom_components

WORKDIR /workspaces

# Set environment variables
ENV SHELL=/bin/bash \
    PYTHONASYNCIODEBUG=1 \
    CONTAINER_WORKSPACE_FOLDER="/workspaces/ha-openaicust"

# Default command
CMD ["/bin/bash"]
