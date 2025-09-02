FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    firefox \
    xvfb \
    libx11-xcb1 \
    libxcb1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libcairo-gobject2 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libdrm2 \
    libxss1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpulse0 \
    libatspi2.0-0 \
    libcups2 \
    wget \
    tar \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install geckodriver
RUN GECKO_VERSION="v0.33.0" && \
    wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-linux64.tar.gz" && \
    tar -xzf "geckodriver-${GECKO_VERSION}-linux64.tar.gz" && \
    mv geckodriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm "geckodriver-${GECKO_VERSION}-linux64.tar.gz"

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN python3 -m venv instapy_env && \
    . instapy_env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p logs db

# Set permissions
RUN chmod +x *.sh

# Expose port (if needed)
EXPOSE 8080

# Start Xvfb and run InstaPy
CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x24 & sleep 2 && source instapy_env/bin/activate && python quickstart.py"]
